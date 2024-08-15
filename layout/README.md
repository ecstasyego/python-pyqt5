## Layouts
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(QtWidgets.QPushButton('OK'))
        layout.addWidget(QtWidgets.QPushButton('Cancel'))
        layout.addLayout(QtWidgets.QVBoxLayout())
        layout.addStretch(1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
  

**[Vertical Layout]: QtWidgets.QVBoxLayout**
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)
    layoutwidget = QtWidgets.QWidget(centralwidget)
    verticalLayout = QtWidgets.QVBoxLayout(layoutwidget)

    MainWindow.setCentralWidget(centralwidget)
    MainWindow.setMenuBar(QtWidgets.QMenuBar(MainWindow))
    MainWindow.setStatusBar(QtWidgets.QStatusBar(MainWindow))
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    return MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
```

**[Horizental Layout]: QtWidgets.QHBoxLayout**
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)
    layoutwidget = QtWidgets.QWidget(centralwidget)
    horizontalLayout = QtWidgets.QHBoxLayout(layoutwidget)

    MainWindow.setCentralWidget(centralwidget)
    MainWindow.setMenuBar(QtWidgets.QMenuBar(MainWindow))
    MainWindow.setStatusBar(QtWidgets.QStatusBar(MainWindow))
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    return MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
```

**[Grid Layout]: QtWidgets.QGridLayout**
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)
    layoutwidget = QtWidgets.QWidget(centralwidget)
    gridLayout = QtWidgets.QGridLayout(layoutwidget)

    MainWindow.setCentralWidget(centralwidget)
    MainWindow.setMenuBar(QtWidgets.QMenuBar(MainWindow))
    MainWindow.setStatusBar(QtWidgets.QStatusBar(MainWindow))
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    return MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
```

**[Form Layout]: QtWidgets.QFormLayout**
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)
    layoutwidget = QtWidgets.QWidget(centralwidget)
    formLayout = QtWidgets.QFormLayout(layoutwidget)

    MainWindow.setCentralWidget(centralwidget)
    MainWindow.setMenuBar(QtWidgets.QMenuBar(MainWindow))
    MainWindow.setStatusBar(QtWidgets.QStatusBar(MainWindow))
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    return MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
```
