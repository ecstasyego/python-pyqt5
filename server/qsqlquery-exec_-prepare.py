from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase( "QSQLITE" )
db.setDatabaseName(":memory:") # example.db, example.sqlite3, ...
db.open()

query = QtSql.QSqlQuery(db)
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """
)
query.exec_("DELETE FROM users")
query.prepare("INSERT INTO users (name, age) VALUES (?, ?)")

query.addBindValue("Alice")
query.addBindValue(25)
query.exec_()

query.addBindValue("Bob")
query.addBindValue(30)
query.exec_()

query.exec_("SELECT * FROM users")
while query.next():
    user_id = query.value(0)  # First column (ID)
    name = query.value(1)     # Second column (name)
    age = query.value(2)      # Third column (age)
    print(f"ID: {user_id}, Name: {name}, Age: {age}")

db.close()
