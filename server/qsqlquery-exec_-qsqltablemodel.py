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
query.exec_("DELETE FROM users")
query.exec_("INSERT INTO users (name, age) VALUES ('Alice', 30)")
query.exec_("INSERT INTO users (name, age) VALUES ('Bob', 25)")

model = QtSql.QSqlTableModel()
model.setTable("users") # model.setQuery( QSqlQuery("SELECT * FROM users") )
model.select()  # Automatically executes "SELECT * FROM users"

# Print the query result (data from the model)
for row in range(model.rowCount()):
    user_id = model.data(model.index(row, 0))  # First column (ID)
    name = model.data(model.index(row, 1))     # Second column (name)
    age = model.data(model.index(row, 2))      # Third column (age)
    print(f"ID: {user_id}, Name: {name}, Age: {age}")

db.close()
