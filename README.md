# 🚀 AI SQL Assistant

Transform natural language into SQL queries using AI.

AI SQL Assistant allows users to interact with SQLite and MySQL databases using plain English. Instead of writing SQL manually, users can ask questions naturally, and the system generates, validates, explains, and executes SQL queries while presenting results through tables and visualizations.

---

Live:
[https://github.com/Retesh07](https://ai-sql-assistant-93qc.onrender.com/app)

## 🌟 Features

### 🤖 Natural Language to SQL

Convert plain English questions into executable SQL queries using LLMs.

**Example**

```text
Show all students in the CSE department with marks above 80
```

Generated SQL:

```sql
SELECT * FROM students
WHERE department = 'CSE'
AND marks > 80;
```

---

### 🗄️ Multi-Database Support

✅ SQLite (.db uploads)

✅ MySQL Connections

Switch seamlessly between local SQLite databases and remote MySQL databases.

---

### 📊 Schema Explorer

Automatically extracts and displays database schema after upload.

```text
students
 ├── id
 ├── name
 ├── department
 └── marks
```

This helps users understand available tables and columns before querying.

---

### 🔍 Relevance Detection

The system checks whether a question can be answered using the connected database.

Example:

```text
Question:
Who won IPL 2025?
```

Response:

```text
Question cannot be answered using this database.
```

This prevents unnecessary SQL generation.

---

### 🛡️ SQL Validation Layer

Generated SQL is validated before execution to reduce errors and improve reliability.

Checks include:

* SQL structure validation
* Query safety checks
* Execution readiness verification

---

### 💡 SQL Explanation

Every generated query includes a human-readable explanation.

Example:

```sql
SELECT department, AVG(marks)
FROM students
GROUP BY department;
```

Explanation:

```text
Calculates the average marks for each department and groups the results by department.
```

---

### 📈 Data Visualization

Results can be viewed as:

* Tables
* Interactive Charts

Supported visualizations:

* Bar Charts
* Comparative Views
* Aggregated Insights

---

### 📥 CSV Export

Download query results instantly as CSV files for reporting and analysis.

---

## 🏗️ System Architecture

```text
┌─────────────────────┐
│     User Query      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Schema Extraction   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Relevance Detection │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Groq LLM Engine   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ SQL Validation      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Query Execution     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ SQL Explanation     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Visualization Layer │
└─────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLite
* MySQL
* Uvicorn

### AI Layer

* Groq API
* Llama 3.3

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Database Utilities

* sqlite3
* mysql-connector-python

---

## 📂 Project Structure

```text
AI_SQL_ASSISTANT/
│
├── main.py
├── llm.py
├── validator.py
├── database.py
├── mysql_connector.py
│
├── uploads/
│
├── index.html
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Retesh07/AI-SQL-ASSISTANT.git
cd AI-SQL-ASSISTANT
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\\Scripts\\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

### Run Application

```bash
uvicorn main:app --reload
```

Open:

```text
http://localhost:8000/app
```

---

## 🎯 Example Workflow

1. Upload SQLite database
2. View schema explorer
3. Ask a question in plain English
4. Generate SQL automatically
5. Validate SQL
6. Execute query
7. View explanation
8. Analyze results through charts
9. Export results as CSV

---

## 🔮 Future Improvements

* PostgreSQL Support
* Query Optimization Suggestions
* User Authentication
* Dashboard Analytics
* Query Caching
* Role-Based Access Control

---

## 👨‍💻 Author

**Retesh**

Computer Science Student | AI & Backend Development Enthusiast



---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
