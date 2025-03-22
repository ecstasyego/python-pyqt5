## Server

```python
from PyQt5.QtSql import QSqlDatabase

QSqlDatabase.drivers() # 'QSQLITE', 'QMARIADB', 'QMYSQL', 'QMYSQL3', 'QPSQL', 'QPSQL7', ...
```


### Local File System: Sqlite3
```python
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

db = QSqlDatabase.addDatabase( "QSQLITE" )
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
`TCP/IP Socket Account`
```mysql
CREATE USER 'root'@'127.0.0.1' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'127.0.0.1' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

```mysql
CREATE DATABASE example;
```

```python
```
