# AI SQL Assistant 🤖

An AI-powered SQL assistant that converts natural language questions into SQL queries and executes them on any SQLite database.

## 🔴 Live Demo
[ai-sql-assistant-93qc.onrender.com/app](https://ai-sql-assistant-93qc.onrender.com/app)

## 🏗️ Architecture
User Question (Plain English)
↓
FastAPI Backend
↓
Groq AI (Natural Language → SQL)
↓
SQL Validation Layer
↓
SQLite Database Execution
↓
Results + Explanation → Frontend

## ✨ Features
- **Natural Language to SQL** — Ask questions in plain English
- **Dynamic Database Upload** — Upload any `.db` file and query it instantly
- **Auto Schema Detection** — Reads database structure automatically
- **SQL Explanation** — AI explains generated SQL in simple English
- **SQL Validation** — Blocks dangerous queries (DROP, DELETE, ALTER)
- **Query History** — Tracks last 10 queries with timestamps
- **CSV Export** — Download query results as CSV
- **Execution Time** — Shows query performance
- **Auto File Cleanup** — Removes uploaded files older than 24 hours

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | FastAPI (Python) |
| Database | SQLite |
| AI Model | Groq API (Llama 3.3 70B) |
| Deployment | Render |

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Retesh07/AI-SQL-ASSISTANT.git
cd AI-SQL-ASSISTANT
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add environment variables**
```bash
# Create .env file
GROQ_API_KEY=your_groq_api_key_here
```

**5. Initialize database**
```bash
python database.py
```

**6. Run the server**
```bash
uvicorn main:app --reload
```

**7. Open frontend**
http://127.0.0.1:8000/app

## 📁 Project Structure
ai_sql_assistant/
├── main.py          # FastAPI application and endpoints
├── llm.py           # Groq AI integration
├── database.py      # SQLite database setup
├── validator.py     # SQL validation layer
├── index.html       # Frontend UI
├── .env             # Environment variables (not pushed)
├── requirements.txt
└── uploads/         # Uploaded database files

## 🔒 Security
- API keys stored in environment variables
- SQL validation blocks destructive queries
- Parameterized queries prevent SQL injection
- Uploaded files auto-deleted after 24 hours

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/app` | Frontend UI |
| POST | `/upload-db` | Upload SQLite database |
| POST | `/query` | Ask natural language question |
| GET | `/history` | Get recent query history |





