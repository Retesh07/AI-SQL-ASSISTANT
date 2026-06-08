import mysql.connector


def get_mysql_schema(host, port, user, password, database):
    conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()

        schema += f"Table: {table_name}\nColumns: {', '.join([col[0] for col in columns])}\n\n"

    conn.close()
    return schema


def execute_mysql_query(host, port, user, password, database, sql):
    conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    cursor.execute(sql)

    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    conn.close()

    return {
        "columns": columns,
        "rows": rows
    }