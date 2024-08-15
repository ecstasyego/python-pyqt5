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
