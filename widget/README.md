
## Buttons
**[Push Button]: QtWidgets.QPushButton**
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)
    pushButton = QtWidgets.QPushButton(centralwidget)

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

**[Tool Button]**
```python
```

**[Radio Button]**
```python
```

**[Check Box]**
```python
```

**[Check Box]**
```python
```

**[Command Link Button]**
```python
```

**[Dialog Button Box]**
```python
```
