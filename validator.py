def validate_sql(query: str):
    query_stripped = query.strip().lower()
    
    if not query_stripped.startswith("select"):
        return False, "Only SELECT queries are allowed"
    
    forbidden = ["drop", "delete", "update", "insert", "alter", "truncate"]
    
    for word in forbidden:
        if word in query_stripped:
            return False, f"Forbidden keyword detected: {word}"
    
    return True, "Valid query"