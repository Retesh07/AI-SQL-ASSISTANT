# AI SQL Assistant 🤖

An AI-powered SQL assistant that converts natural language questions into SQL queries and executes them on **SQLite databases or live MySQL servers**. Powered by Groq's Llama 3.3 70B for fast, accurate SQL generation.

## 🔴 Live Demo
🌐 **[ai-sql-assistant-93qc.onrender.com/app](https://ai-sql-assistant-93qc.onrender.com/app)**

## 🏗️ Architecture
```
User Question (Plain English)
        ↓
    FastAPI Backend
        ↓
 Groq AI (Llama 3.3 70B)
  Natural Language → SQL
        ↓
  SQL Validation Layer
        ↓
SQLite / MySQL Execution
        ↓
Query Results + AI Explanation → Frontend
```

## ✨ Features

### 🧠 AI & Query Generation
- **Natural Language to SQL** — Ask questions in plain English, get SQL queries instantly
- **Groq AI Integration** — Uses Llama 3.3 70B for intelligent SQL generation
- **SQL Explanation** — AI explains generated SQL in simple English

### 📊 Database Support
- **SQLite File Upload** — Upload any `.db` file and query it instantly
- **MySQL Live Connection** — Connect to remote MySQL databases in real-time
- **Dual-Mode Operation** — Switch seamlessly between SQLite uploads and MySQL connections
- **Auto Schema Detection** — Automatically reads database structure (tables, columns, data types)

### 📈 Results & Visualization
- **Interactive Tables** — View results in formatted table view
- **Auto-Generated Charts** — Visualize data with automatic chart detection (bar charts for numeric columns)
- **Tab-Based Interface** — Switch between Table and Chart views
- **Execution Time Display** — See query performance metrics

### 🛡️ Safety & History
- **SQL Validation Layer** — Blocks dangerous queries (DROP, DELETE, UPDATE, INSERT, ALTER, TRUNCATE)
- **Query History** — Auto-saves last 10 queries with:
  - Original question
  - Generated SQL
  - Database source (SQLite file ID or MySQL label)
  - Execution timestamp
- **Parameterized Queries** — Prevents SQL injection attacks

### 🔧 Utility Features
- **CSV Export** — Download query results as CSV files
- **Auto File Cleanup** — Uploaded SQLite files auto-delete after 24 hours
- **Real-Time History Refresh** — Query history updates immediately after execution
- **Error Messages** — Clear, helpful error feedback for debugging

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript (vanilla) |
| Charting | Chart.js |
| Backend | FastAPI, Uvicorn (Python 3.9+) |
| Databases | SQLite 3, MySQL 8.0+ |
| AI Model | Groq API (Llama 3.3 70B) |
| Connectors | python-dotenv, mysql-connector-python |
| Deployment | Render (auto-deploy from GitHub) |
| Data Format | JSON, CSV

## � API Endpoints

### Core Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/app` | Serves frontend UI (index.html) |

### Database & Query Operations
| Method | Endpoint | Description | Payload |
|--------|----------|-------------|---------|
| POST | `/upload-db` | Upload SQLite database file | `{ "file": File }` |
| POST | `/use-mysql` | Connect to MySQL database | `{ "host": string, "user": string, "password": string, "database": string }` |
| POST | `/query` | Execute natural language query | `{ "question": string, "db_type": "sqlite" \| "mysql", "db_id": string }` |
| GET | `/history` | Get recent 10 queries | Returns: `{ "history": [[question, sql, db_id, timestamp], ...] }` |

### Response Format
**Successful Query Response:**
```json
{
  "question": "What are the top 5 students?",
  "sql": "SELECT * FROM students LIMIT 5",
  "explanation": "This query fetches the first 5 records from the students table...",
  "columns": ["id", "name", "email"],
  "rows": [[1, "Alice", "alice@example.com"], ...],
  "execution_time": "0.012s"
}
```

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Retesh07/AI-SQL-ASSISTANT.git
cd AI-SQL-ASSISTANT
```

**2. Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
# Create .env file in project root
echo GROQ_API_KEY=your_groq_api_key_here > .env
```
Get your Groq API key from [console.groq.com](https://console.groq.com)

**5. Initialize SQLite database**
```bash
python database.py
```

**6. Start the server**
```bash
uvicorn main:app --reload
```

**7. Open in browser**
Navigate to: **http://127.0.0.1:8000/app**

## 🔐 Environment Variables
```env
# Required
GROQ_API_KEY=sk_...your_key_here...

# Optional (for MySQL features)
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DATABASE=yourdatabase
```

## 🔒 Security Features

✅ **API Key Protection**
- Groq API keys stored in `.env` (never committed to Git)
- Loaded via `python-dotenv` at runtime

✅ **SQL Injection Prevention**
- All user inputs validated before query execution
- Parameterized queries used throughout

✅ **Query Safety**
- SQL validation layer blocks dangerous operations:
  - `DROP` (prevent table deletion)
  - `DELETE` (prevent data deletion)
  - `UPDATE` / `INSERT` (prevent data modification)
  - `ALTER` (prevent schema changes)
  - `TRUNCATE` (prevent bulk deletion)

✅ **File Management**
- Uploaded SQLite files stored in `uploads/` directory
- Auto-cleanup removes files older than 24 hours
- Unique file IDs prevent conflicts

✅ **Database Isolation**
- Each SQLite upload gets unique UUID
- MySQL connections require explicit credentials
- Query history tracks data source for audit trail

## 🎯 Usage Examples

### Example 1: Query SQLite File
1. Click **"Upload Database"**
2. Select your `.db` file
3. Ask: *"How many students are there?"*
4. Get instant SQL + results + chart

### Example 2: Connect to MySQL
1. Click **"Use MySQL"**
2. Enter connection details (host, user, password, database)
3. Click **"Connect"**
4. Ask: *"Show me all orders from last month"*
5. Results displayed with auto-generated chart if applicable

### Example 3: Export Results
1. Execute any query
2. Click **"Download CSV"** below results
3. Open in Excel, Google Sheets, etc.

## 📊 Feature Breakdown

| Feature | SQLite | MySQL | Details |
|---------|--------|-------|---------|
| Upload files | ✅ | ❌ | Upload `.db` files directly |
| Live connection | ❌ | ✅ | Connect to remote servers |
| Auto schema detection | ✅ | ✅ | Detects tables and columns |
| Natural language queries | ✅ | ✅ | Works on both sources |
| Query history | ✅ | ✅ | Tracks all queries |
| Chart visualization | ✅ | ✅ | Auto-detects numeric data |
| CSV export | ✅ | ✅ | Download any results |
| Data modification | ❌ | ❌ | Read-only (by design) |

## 🚀 Deployment

### Deploy to Render (Free Tier)
1. Push code to GitHub
2. Connect repo to Render
3. Set `GROQ_API_KEY` environment variable in Render dashboard
4. Deploy with auto-deploy on git push

**Deployment note:** SQLite files (`.db`) are ephemeral on free Render instances and reset when the container restarts. Use MySQL for persistent storage in production.

## 🛠️ Requirements
- Python 3.9+
- pip or conda
- Groq API key (free account at [console.groq.com](https://console.groq.com))
- For MySQL: MySQL 8.0+ server (or MariaDB)
- For local testing: Any modern browser

## 📦 Dependencies
See [requirements.txt](requirements.txt) for full list. Key packages:
- `fastapi` - Web framework
- `groq` - LLM API
- `mysql-connector-python` - MySQL connections
- `python-dotenv` - Environment management

## 🤝 Contributing
Pull requests welcome! Areas for enhancement:
- Support for PostgreSQL, MongoDB
- Advanced charting options (pie, line, scatter)
- Query optimization suggestions
- Multi-table joins with auto-detection
- Saved query templates

## ❓ Troubleshooting

### Issue: "GROQ_API_KEY not found"
- **Solution:** Ensure `.env` file exists in project root with your Groq API key
- Restart the server after creating `.env`

### Issue: "ModuleNotFoundError: No module named 'groq'"
- **Solution:** Run `pip install -r requirements.txt` again
- Use `pip list` to verify `groq` is installed

### Issue: MySQL connection fails
- **Solution:** Verify connection details:
  - Host is accessible from your location
  - User has correct permissions
  - Database name is correct
  - MySQL port (default 3306) is open

### Issue: Uploaded `.db` file not found
- **Solution:** File may have been auto-cleaned (24-hour expiry)
- Re-upload the file

### Issue: Charts not displaying
- **Solution:** Ensure results contain numeric columns
- Chart.js library loads from CDN (check internet connection)

### Issue: Query takes too long on Render
- **Solution:** Render free tier is limited; add indexes to large tables
- For MySQL: Consider upgrading to a dedicated server

## 📚 Resources & Documentation

### External Links
- [Groq Console](https://console.groq.com) - Get your API key
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [SQLite Official](https://www.sqlite.org)
- [MySQL Documentation](https://dev.mysql.com/doc)
- [Chart.js Docs](https://www.chartjs.org)

### Related Articles
- [SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security)
- [Natural Language to SQL](https://huggingface.co/spaces/gradio/SQL_Query_Generator)

## 📊 Performance Tips

✅ **For SQLite:**
- Keep database files under 100MB for best performance
- Use indexes on frequently queried columns
- Upload once and reuse for multiple queries

✅ **For MySQL:**
- Ensure proper database indexing
- Use connection pooling for high-traffic
- Query on production servers during off-peak hours

✅ **For LLM Queries:**
- Keep table schemas simple and well-named
- Avoid extremely large result sets (1000+ rows)
- Use LIMIT clauses for performance testing

## 🐛 Debugging

Enable debug mode for detailed logs:
```bash
# In main.py, set debug=True
uvicorn main:app --reload --log-level debug
```

Check browser console for frontend errors:
- Press `F12` in browser
- Go to **Console** tab
- Look for red error messages

## 📄 License
This project is open-source and available under the MIT License.


---

### ⭐ If you found this helpful, please consider giving it a star!

**Repository:** [github.com/Retesh07/AI-SQL-ASSISTANT](https://github.com/Retesh07/AI-SQL-ASSISTANT)

**Live Demo:** [ai-sql-assistant-93qc.onrender.com/app](https://ai-sql-assistant-93qc.onrender.com/app)





