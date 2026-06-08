# AI SQL Assistant 🤖

AI-powered SQL assistant that converts natural language questions into SQL queries and executes them on SQLite databases or live MySQL servers using Groq Llama 3.3 70B.

## Live Demo

https://ai-sql-assistant-93qc.onrender.com/app

## Features

* Natural Language → SQL conversion
* SQLite file upload support
* Live MySQL database connection
* AI-generated SQL explanations
* Automatic schema detection
* Interactive query results
* Auto-generated charts
* CSV export
* Query history tracking
* SQL safety validation

## Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: FastAPI, Python
* AI: Groq (Llama 3.3 70B)
* Databases: SQLite, MySQL
* Deployment: Render

## Project Flow

User Question → Groq AI → SQL Generation → Validation → Database Execution → Results & Explanation

## Run Locally

```bash
git clone https://github.com/Retesh07/AI-SQL-ASSISTANT.git
cd AI-SQL-ASSISTANT

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

Start the server:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/app
```

## Security

* SQL Injection Protection
* Read-only query execution
* Dangerous SQL commands blocked
* Environment variable based API key management

## Future Enhancements

* PostgreSQL support
* Advanced visualizations
* Query optimization suggestions
* Multi-database support

## Author

Retesh G.S

## License

MIT License
