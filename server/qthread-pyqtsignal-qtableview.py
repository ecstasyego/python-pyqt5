from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

class Worker(QtCore.QThread):
    signal = QtCore.pyqtSignal(bool)  # Signal to send fetched data

    def __init__(self):
        super().__init__()
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(":memory:")
        self.db.open()

    def run(self):
        query = QtSql.QSqlQuery(self.db)
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

        self.signal.emit(True)  # Emit the signal for fetched data


    def close(self):
        self.db.close()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # DATABASE
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(":memory:")
        self.db.open()

        # MODEL
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("users")
        self.model.select()

        # WIDGET
        self.widget = QtWidgets.QTableView()
        self.widget.setModel(self.model)

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widget)
        self.setLayout(layout)

        # Database Worker
        self.worker = Worker()  # Pass the main thread DB to the worker
        self.worker.signal.connect(self.update_table)  # Connect signal to slot
        self.worker.start()  # Start the worker thread

    def update_table(self, *values):
        query = QtSql.QSqlQuery(self.db)  # Use the main thread's db connection
        query.exec_("SELECT * FROM users")  # Execute the query to fetch all users
        self.model.setQuery(query)  # Pass the QSqlQuery object to setQuery

    def closeEvent(self, event):
        # Ensure the database connection is closed properly
        self.db.close()
        self.worker.close()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())

