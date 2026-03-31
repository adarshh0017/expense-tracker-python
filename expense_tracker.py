import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
""")

conn.commit()

# ADD EXPENSE
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    cursor.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
        (date, category, amount, description)
    )

    conn.commit()
    print("✅ Expense added!")

# VIEW EXPENSES
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\n📋 All Expenses:")
    for row in rows:
        print(row)

# TOTAL EXPENSE
def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0] or 0
    print("\n💰 Total Expense:", total)

# MENU SYSTEM
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

conn.close()
   