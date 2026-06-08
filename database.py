import sqlite3

def init_db():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            department TEXT,
            marks REAL
        )
    """)
    cursor.executemany("""
        INSERT OR IGNORE INTO students (id, name, age, department, marks)
        VALUES (?, ?, ?, ?, ?)
    """, [
        (1, "Rahul", 21, "CSE", 85.5),
        (2, "Priya", 22, "ECE", 90.0),
        (3, "Arjun", 21, "CSE", 78.3),
        (4, "Sneha", 23, "MECH", 88.1),
        (5, "Kiran", 22, "IT", 76.9)
    ])
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS query_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            sql_query TEXT,
            db_id TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")
  

def save_query_history(question, sql_query, db_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    from datetime import datetime
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
        INSERT INTO query_history (question, sql_query, db_id, created_at)
        VALUES (?, ?, ?, ?)
    """, (question, sql_query, db_id, created_at))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
  
