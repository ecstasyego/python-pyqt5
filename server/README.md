## Server

```python
from PyQt5.QtSql import QSqlDatabase

QSqlDatabase.drivers() # 'QSQLITE', 'QMARIADB', 'QMYSQL', 'QMYSQL3', 'QPSQL', 'QPSQL7', ...
```


### Local File System: Sqlite3
```python
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

useable_dbs = QSqlDatabase.drivers() 
db = QSqlDatabase.addDatabase( useable_dbs[useable_dbs.index("QSQLITE")] )
db.setDatabaseName("example.db")

if not db.open():
    print("DB Connection: Fail")
else:
    print("DB COnnection: Sucess")

query = QSqlQuery()
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """
)

db.close()
```

### Remote: MySQL
```python
```
