import os
import re
# pyrefly: ignore [missing-import]
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set in .env")

client = Groq(api_key=api_key)


def clean_sql(sql_text: str) -> str:
    sql_text = sql_text.strip()
    sql_text = re.sub(r"```sql\s*", "", sql_text, flags=re.IGNORECASE)
    sql_text = re.sub(r"```", "", sql_text)
    return sql_text.strip()


def generate_sql(user_question, schema, db_type="sqlite"):
    prompt = f"""
You are an expert SQL generator.

Database Type: {db_type}

Database Schema:
{schema}

User Question:
{user_question}

Rules:
1. Return ONLY SQL query
2. No explanations
3. No markdown
4. No ``` blocks
5. Use correct SQL for given DB type
6. Use LOWER() for case-insensitive matching
7. Use real column names from schema only
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    sql = clean_sql(response.choices[0].message.content)
    return sql

def check_question_relevance(user_question, schema):
    prompt = f"""
You are a database relevance checker.

Database Schema:
{schema}

User Question:
{user_question}

Task:
Determine whether the question can be answered using ONLY the available tables and columns.

Return ONLY valid JSON.

Example:
{{
    "relevant": true,
    "confidence": 95,
    "reason": "Question matches available tables and columns."
}}

OR

{{
    "relevant": false,
    "confidence": 5,
    "reason": "Question is unrelated to the database schema."
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    # Strip markdown code fences the LLM sometimes wraps around JSON
    import re as _re
    cleaned = _re.sub(r"```(?:json)?\s*", "", content, flags=_re.IGNORECASE).replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except Exception:
        import logging as _log
        _log.warning(f"[relevance] Could not parse LLM response as JSON. Raw content: {repr(content)}")
        return {
            "relevant": True,
            "confidence": 50,
            "reason": "Could not determine relevance"
        }


def explain_sql(sql):
    prompt = f"""
Explain this SQL in simple words:

{sql}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()