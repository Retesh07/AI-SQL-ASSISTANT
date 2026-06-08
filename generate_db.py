import sqlite3
import random

conn = sqlite3.connect("test_company.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT,
        salary REAL,
        age INTEGER,
        experience INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        price REAL,
        stock INTEGER
    )
""")

# Random data
departments = ["HR", "Engineering", "Sales", "Marketing", "Finance"]
names = ["Amit", "Priya", "Rahul", "Sneha", "Kiran", "Deepa", "Raj", "Anita", "Vijay", "Meera"]

for i in range(20):
    cursor.execute("INSERT INTO employees (name, department, salary, age, experience) VALUES (?, ?, ?, ?, ?)", (
        random.choice(names),
        random.choice(departments),
        round(random.uniform(30000, 150000), 2),
        random.randint(22, 55),
        random.randint(1, 20)
    ))

categories = ["Electronics", "Clothing", "Food", "Sports", "Books"]
products = ["Laptop", "Phone", "Shirt", "Rice", "Bat", "Novel", "Shoes", "Tablet"]

for i in range(15):
    cursor.execute("INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)", (
        random.choice(products),
        random.choice(categories),
        round(random.uniform(100, 50000), 2),
        random.randint(5, 500)
    ))

conn.commit()
conn.close()
print("test_company.db created successfully!")