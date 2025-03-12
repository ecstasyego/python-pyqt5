from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Database
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("example.db")
        db.open()

        # Model
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

    def callback(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
