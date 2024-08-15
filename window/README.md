## Window
`QtWidgets.QMainWindow`
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.setMenuBar(QtWidgets.QMenuBar(self))
        self.setStatusBar(QtWidgets.QStatusBar(self))
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```


```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window Title')
        self.setGeometry(300, 300, 300, 200)

        statusbar = self.statusBar()
        statusbar.showMessage('Ready')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        menubar.addMenu('&File')

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(QtWidgets.QAction(QtGui.QIcon('exit.png'), 'Exit', self))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
