from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase( "QSQLITE" )
db.setDatabaseName(":memory:") # example.db, example.sqlite3, ...
db.open()

query = QtSql.QSqlQuery()
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """
)
query.exec_("INSERT INTO users (name, age) VALUES ('Alice', 30)")
query.exec_("INSERT INTO users (name, age) VALUES ('Bob', 25)")

query.exec_("SELECT * FROM users")
while query.next():
    user_id = query.value(0)  # First column (ID)
    name = query.value(1)     # Second column (name)
    age = query.value(2)      # Third column (age)
    print(f"ID: {user_id}, Name: {name}, Age: {age}")


db.close()
