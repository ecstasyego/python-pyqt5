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

<br/><br/><br/>
## Application
### Window
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
  
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

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


<br/><br/>
### Layouts
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

    # Layouts
    layoutwidget = QtWidgets.QWidget(centralwidget)
    verticalLayout = QtWidgets.QVBoxLayout(layoutwidget)
    horizontalLayout = QtWidgets.QHBoxLayout(layoutwidget)
    gridLayout = QtWidgets.QGridLayout(layoutwidget)
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

  
<br/><br/>
### Spacers

  
<br/><br/>
### Buttons
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

    # Buttons
    pushButton = QtWidgets.QPushButton(centralwidget)
    toolButton = QtWidgets.QToolButton(centralwidget)
    radioButton = QtWidgets.QRadioButton(centralwidget)
    checkBox = QtWidgets.QCheckBox(centralwidget)
    commandLinkButton = QtWidgets.QCommandLinkButton(centralwidget)
    buttonBox = QtWidgets.QDialogButtonBox(centralwidget)
    buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)

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


<br/><br/>
### Item Views

  
<br/><br/>
### Item Widgets

  
<br/><br/>
### Container
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

    # Containers
    widget = QtWidgets.QWidget(centralwidget)
    mdiArea = QtWidgets.QMdiArea(centralwidget)
    groupBox = QtWidgets.QGroupBox(centralwidget)
    toolBox = QtWidgets.QToolBox(centralwidget)
    toolBox.addItem(QtWidgets.QWidget(), "")
    toolBox.addItem(QtWidgets.QWidget(), "")
    tabWidget = QtWidgets.QTabWidget(centralwidget)
    tabWidget.addTab(QtWidgets.QWidget(), "")
    tabWidget.addTab(QtWidgets.QWidget(), "")
    stackedWidget = QtWidgets.QStackedWidget(centralwidget)
    stackedWidget.addWidget(QtWidgets.QWidget())
    stackedWidget.addWidget(QtWidgets.QWidget())
    scrollArea = QtWidgets.QScrollArea(centralwidget)
    scrollArea.setWidget(QtWidgets.QWidget())
    frame = QtWidgets.QFrame(centralwidget)
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)

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
  
<br/><br/>
### Input Widgets
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

    # Input Widgets
    comboBox = QtWidgets.QComboBox(centralwidget)
    fontComboBox = QtWidgets.QFontComboBox(centralwidget)
    lineEdit = QtWidgets.QLineEdit(centralwidget)
    textEdit = QtWidgets.QTextEdit(centralwidget)
    plainTextEdit = QtWidgets.QPlainTextEdit(centralwidget)
    spinBox = QtWidgets.QSpinBox(centralwidget)
    doubleSpinBox = QtWidgets.QDoubleSpinBox(centralwidget)
    timeEdit = QtWidgets.QTimeEdit(centralwidget)
    dateEdit = QtWidgets.QDateEdit(centralwidget)
    dateTimeEdit = QtWidgets.QDateTimeEdit(centralwidget)
    dial = QtWidgets.QDial(centralwidget)
    horizontalScrollBar = QtWidgets.QScrollBar(centralwidget)
    horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
    verticalScrollBar = QtWidgets.QScrollBar(centralwidget)
    verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
    horizontalSlider = QtWidgets.QSlider(centralwidget)
    horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
    verticalSlider = QtWidgets.QSlider(centralwidget)
    verticalSlider.setOrientation(QtCore.Qt.Vertical)
    keySequenceEdit = QtWidgets.QKeySequenceEdit(centralwidget)

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

  
<br/><br/>
### Display Widgets
```python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtQuickWidgets, QtWebEngineWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

    # Display Widgets
    label = QtWidgets.QLabel(centralwidget)
    textBrowser = QtWidgets.QTextBrowser(centralwidget)
    graphicsView = QtWidgets.QGraphicsView(centralwidget)
    calendarWidget = QtWidgets.QCalendarWidget(centralwidget)
    lcdNumber = QtWidgets.QLCDNumber(centralwidget)
    progressBar = QtWidgets.QProgressBar(centralwidget)
    progressBar.setProperty("value", 24)
    hline = QtWidgets.QFrame(centralwidget)
    hline.setFrameShape(QtWidgets.QFrame.HLine)
    hline.setFrameShadow(QtWidgets.QFrame.Sunken)
    vline = QtWidgets.QFrame(centralwidget)
    vline.setFrameShape(QtWidgets.QFrame.VLine)
    vline.setFrameShadow(QtWidgets.QFrame.Sunken)
    openGLWidget = QtWidgets.QOpenGLWidget(centralwidget)
    quickWidget = QtQuickWidgets.QQuickWidget(centralwidget)
    quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
    webEngineView = QtWebEngineWidgets.QWebEngineView(centralwidget)
    webEngineView.setUrl(QtCore.QUrl("about:blank"))


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
  



