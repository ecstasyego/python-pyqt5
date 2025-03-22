## Server

```python
from PyQt5.QtSql import QSqlDatabase

QSqlDatabase.drivers() # 'QSQLITE', 'QMARIADB', 'QMYSQL', 'QMYSQL3', 'QPSQL', 'QPSQL7', ...
```


### Local File System: Sqlite3
```python
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

db = QSqlDatabase.addDatabase( "QSQLITE" )
db.setDatabaseName(":memory:") # example.db, example.sqlite3, ...

if not db.open():
    print("DB Connection: Fail", db.lastError().text())
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
CREATE USER 'testuser'@'127.0.0.1' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'testuser'@'127.0.0.1' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

```mysql
CREATE DATABASE example;
```

```python
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

db = QSqlDatabase.addDatabase( "QMYSQL" )
db.setHostName("127.0.0.1")
db.setPort(3306)
db.setDatabaseName("example")
db.setUserName("testuser")
db.setPassword("PASSWORD")

if not db.open():
    print("DB Connection: Fail", db.lastError().text())
else:
    print("DB COnnection: Sucess")

query = QSqlQuery()
query.exec_(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    """
)
db.close()
```


### ViewModel
`setTable`+`select`
```python
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QTableView

db = QSqlDatabase.addDatabase("QSQLITE") # [DB DRIVER]
db.setDatabaseName(":memory:")           # In-memory database
db.open()

model = QSqlTableModel() # Setting up the table model (automatically uses the active db connection)
model.setTable("users")  # [DB TABLE] This will use the db connection created above
model.select()           # [DB QUERY]

widget = QTableView()
widget.setModel(model)
```

`setQuery`
```python
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QTableView

db = QSqlDatabase.addDatabase("QSQLITE") # [DB DRIVER]
db.setDatabaseName(":memory:")           # In-memory database
db.open()

model = QSqlTableModel()                           # Setting up the table model (automatically uses the active db connection)
model.setQuery( QSqlQuery("SELECT * FROM users") ) # [DB TABLE QUERY]

widget = QTableView()
widget.setModel(model)
```

