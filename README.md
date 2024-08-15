# python-pyqt5

**Display**  
xming xserver: https://sourceforge.net/projects/xming/
```bash
export LIBGL_ALWAYS_INDIRECT=
export DISPLAY=:0
```

  
**Installation**  
qt-designer: https://build-system.fman.io/qt-designer-download
```bash
pip install PyQt5
```

  
**Execution**  
/usr/lib/qt5/bin/designer
```bash
designer
```

## Application
**Window**
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setCentralWidget(QtWidgets.QWidget(MainWindow))
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

### Layouts
**Vertical Layout**
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)
    verticalLayoutWidget = QtWidgets.QWidget(centralwidget)
    verticalLayout = QtWidgets.QVBoxLayout(verticalLayoutWidget)

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
  
  
### Spacers

  
### Buttons

  
### Item Views

  
### Item Widgets

  
### Container

  
### Input Widgets

  
### Display Widgets
  



