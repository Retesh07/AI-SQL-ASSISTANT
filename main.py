from fastapi import FastAPI, HTTPException, UploadFile, File
import os
import shutil
from pydantic import BaseModel
from typing import Optional
import sqlite3
from llm import generate_sql, explain_sql
from validator import validate_sql
from database import init_db, save_query_history
from fastapi.middleware.cors import CORSMiddleware
import logging
import time
import uuid
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from mysql_connector import get_mysql_schema, execute_mysql_query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="."), name="static")


@app.get("/app")
def frontend():
    return FileResponse("index.html")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QueryRequest(BaseModel):
    question: str
    db_type: str
    db_id: str = None
    host: str = None
    port: int = 3306
    user: str = None
    password: str = None
    database: str = None


class MySQLConnRequest(BaseModel):
    host: str
    port: int = 3306
    user: Optional[str] = None
    password: Optional[str] = None
    database: Optional[str] = None


def cleanup_old_files():
    if not os.path.exists("uploads"):
        return

    for file in os.listdir("uploads"):
        file_path = f"uploads/{file}"
        if time.time() - os.path.getmtime(file_path) > 86400:
            os.remove(file_path)


@app.on_event("startup")
def startup_event():
    init_db()
    cleanup_old_files()


@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {"message": "AI SQL Assistant is running!"}


@app.get("/history")
def get_history():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT question, sql_query, db_id, created_at 
        FROM query_history 
        ORDER BY created_at DESC 
        LIMIT 10
    """)
    history = cursor.fetchall()
    conn.close()
    return {"history": history}


@app.post("/upload-db")
def upload_database(file: UploadFile = File(...)):
    if not file.filename.endswith(".db"):
        raise HTTPException(status_code=400, detail="Only .db files are allowed")

    os.makedirs("uploads", exist_ok=True)

    db_id = str(uuid.uuid4())
    file_path = f"uploads/{db_id}.db"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"db_id": db_id, "message": "Database uploaded successfully"}


@app.post("/use-mysql")
def use_mysql(request: MySQLConnRequest):
    try:
        # Try fetching schema as a connectivity test
        schema = get_mysql_schema(
            request.host, request.port,
            request.user, request.password,
            request.database
        )
        return {"detail": "Connected", "schema": schema}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


# ========================= QUERY ENGINE =========================
@app.post("/query")
def query_database(request: QueryRequest):
    start = time.time()
    logger.info(f"Question received: {request.question}")

    conn = None
    cursor = None
    schema = ""

    try:
        # ---------------- SQLITE ----------------
        if request.db_type == "sqlite":
            db_path = f"uploads/{request.db_id}.db"

            if not os.path.exists(db_path):
                raise HTTPException(status_code=404, detail="DB not found")

            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                cursor.execute(f"PRAGMA table_info({table_name})")
                cols = cursor.fetchall()

                schema += f"{table_name}(" + ", ".join([c[1] for c in cols]) + ")\n"

        # ---------------- MYSQL ----------------
        else:
            from mysql_connector import get_mysql_schema, execute_mysql_query

            schema = get_mysql_schema(
                request.host, request.port,
                request.user, request.password,
                request.database
            )

        # ---------------- LLM ----------------
        sql = generate_sql(request.question, schema, request.db_type)
        explanation = explain_sql(sql)

        # ---------------- VALIDATION ----------------
        is_valid, message = validate_sql(sql)
        if not is_valid:
            raise HTTPException(status_code=400, detail=message)

        # ---------------- EXECUTE ----------------
        if request.db_type == "sqlite":
            cursor.execute(sql)

            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            conn.close()

            results = {
                "columns": columns,
                "rows": rows
            }

        else:
            results = execute_mysql_query(
                request.host, request.port,
                request.user, request.password,
                request.database,
                sql
            )

        execution_time = round(time.time() - start, 3)

        save_query_history(
            request.question,
            sql,
            request.db_id or request.database
        )

        return {
            "question": request.question,
            "sql": sql,
            "explanation": explanation,
            "results": results,
            "execution_time": f"{execution_time}s"
        }

    except Exception as exc:
        if conn:
            conn.close()
        raise HTTPException(status_code=500, detail=str(exc))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)