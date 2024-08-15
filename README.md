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
## Modules
SEARCH:`https://doc.qt.io/qt-5/[].html`  
[Reference](https://doc.qt.io/qt-5/qtwidgets-module.html)     
  - Window
    - [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html)
  - Layouts
    - [QBoxLayout](https://doc.qt.io/qt-5/qboxlayout.html)
    - [QGridLayout](https://doc.qt.io/qt-5/qgridlayout.html)
    - [QFormLayout](https://doc.qt.io/qt-5/qformlayout.html)
  - Spacers
  - Buttons
    - [QPushButton](https://doc.qt.io/qt-5/qpushbutton.html)
    - [QToolButton](https://doc.qt.io/qt-5/qtoolbutton.html)
    - [QRadioButton](https://doc.qt.io/qt-5/qradiobutton.html)
  - Item Views: Model-Based
  - Item Widgets: Item-Based
  - Containers
    - [QWidget](https://doc.qt.io/qt-5/qwidget.html)
    - [QMdiArea](https://doc.qt.io/qt-5/qmdiarea.html)
    - [QToolBox](https://doc.qt.io/qt-5/qtoolbox.html)
    - [QGroupBox](https://doc.qt.io/qt-5/qgroupbox.html)
    - [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html)
    - [QScrollArea](https://doc.qt.io/qt-5/qscrollarea.html)
    - [QStackedWidget](https://doc.qt.io/qt-5/qstackedwidget.html)
    - [QFrame](https://doc.qt.io/qt-5/qframe.html)
  - Input Widgets
    - [QComboBox](https://doc.qt.io/qt-5/qcombobox.html)
    - [QFontComboBox](https://doc.qt.io/qt-5/qfontcombobox.html)
    - [QLineEdit](https://doc.qt.io/qt-5/qlineedit.html)
    - [QTextEdut](https://doc.qt.io/qt-5/qtextedit.html)
    - [QPlainTextEdit](https://doc.qt.io/qt-5/qplaintextedit.html)
    - [QSpinBox](https://doc.qt.io/qt-5/qspinbox.html)
    - [QDoubleSpinBox](https://doc.qt.io/qt-5/qdoublespinbox.html)
    - [QTimeEdit](https://doc.qt.io/qt-5/qtimeedit.html)
    - [QDateEdit](https://doc.qt.io/qt-5/qdateedit.html)
    - [QDateTimeEdit](https://doc.qt.io/qt-5/qdatetimeedit.html)
    - [QDial](https://doc.qt.io/qt-5/qdial.html)
    - [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html)
    - [QSlider](https://doc.qt.io/qt-5/qslider.html)
    - [QKeySequenceEdit](https://doc.qt.io/qt-5/qkeysequenceedit.html)
  - Display Widgets


<br/><br/><br/>
## Application
![image](https://doc.qt.io/qt-5/images/mainwindowlayout.png)  

### Window
`QtWidgets.QMainWindow`
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

    window = Window()
    window.show()
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

    window = Window()
    window.show()
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

    window = Window()
    window.show()
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

    window = Window()
    window.show()
    sys.exit(app.exec_())
```


<br/><br/>
### Item Views: Model-Based
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

    # Item Views[Model-Based]
    listView = QtWidgets.QListView(centralwidget)
    treeView = QtWidgets.QTreeView(centralwidget)
    tableView = QtWidgets.QTableView(centralwidget)
    columnView = QtWidgets.QColumnView(centralwidget)
    undoView = QtWidgets.QUndoView(centralwidget)

    MainWindow.setCentralWidget(centralwidget)
    MainWindow.setMenuBar(QtWidgets.QMenuBar(MainWindow))
    MainWindow.setStatusBar(QtWidgets.QStatusBar(MainWindow))
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    return MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
  
<br/><br/>
### Item Widgets: Item-Based
```python
from PyQt5 import QtCore, QtGui, QtWidgets

def Window():
    MainWindow = QtWidgets.QMainWindow()
    centralwidget = QtWidgets.QWidget(MainWindow)

    # Item Widgets[Item-Based]
    listWidget = QtWidgets.QListWidget(centralwidget)
    treeWidget = QtWidgets.QTreeWidget(centralwidget)
    treeWidget.headerItem().setText(0, "1")
    tableWidget = QtWidgets.QTableWidget(centralwidget)
    tableWidget.setColumnCount(0)
    tableWidget.setRowCount(0)

    MainWindow.setCentralWidget(centralwidget)
    MainWindow.setMenuBar(QtWidgets.QMenuBar(MainWindow))
    MainWindow.setStatusBar(QtWidgets.QStatusBar(MainWindow))
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    return MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
  
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

    window = Window()
    window.show()
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

    window = Window()
    window.show()
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

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
  



