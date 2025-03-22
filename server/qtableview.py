from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # DATABASE
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(":memory:")
        db.open()

        # Query
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

        # Query(1): Insert
        query.prepare("INSERT INTO users (name, age) VALUES (?, ?)")
        query.addBindValue("Alice")
        query.addBindValue(25)
        query.exec_()

        query.addBindValue("Bob")
        query.addBindValue(30)
        query.exec_()

        # Query(2): Search
        while query.next():
            user_id = query.value(0)
            name = query.value(1)
            age = query.value(2)
            print(f"ID: {user_id}, Name: {name}, Age: {age}")


        # MODEL
        model = QtSql.QSqlTableModel()
        model.setTable("users")
        model.select()

        # WIDGETS
        widget = QtWidgets.QTableView()
        widget.setModel(model)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        db.close()
    
    def callback(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
