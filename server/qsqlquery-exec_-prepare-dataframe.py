import pandas as pd
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

# INSERT
df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
query.prepare("INSERT INTO users (name, age) VALUES (?, ?)")
for idx, row in df.iterrows():
    query.addBindValue(row["name"])
    query.addBindValue(row["age"])
    query.exec_()

# SELECT
query.exec_("SELECT * FROM users")
columns = [query.record().fieldName(i) for i in range(query.record().count())]
df = pd.DataFrame(columns=columns)
while query.next():
    row = [[query.value(i) for i in range(query.record().count())]]
    df = pd.concat([df, pd.DataFrame(row, columns=df.columns)], ignore_index=True)

db.close()
