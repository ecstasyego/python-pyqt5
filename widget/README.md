## Widgets
`QtWidgets.QWidget`
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        widget = QtWidgets.QWidget() # WIDGETS
        layout = QtWidgets.QVBoxLayout() # LAYOUT
        layout.addWidget(widget)
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
  

**Widget Properties**
 - widget.setGeometry(QtCore.QRect(200, 490, 118, 23))
 - widget.setProperty("value", 24)
 - widget.setObjectName("progressBar")


<br/><br/><br/>
### Template
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QWidget()

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        layout.addStretch(1)

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
```
  
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.widgets = dict()
        self.layouts = dict()

        # WIDGETS
        self.widgets['widget1'] = QtWidgets.QWidget()

        # LAYOUTS
        self.layouts['layout0'] = QtWidgets.QVBoxLayout()
        self.layouts['layout0'].addWidget(self.widgets['widget1'])
        self.layouts['layout0'].addStretch(1)

        layout = self.layouts['layout0']
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
```


<br/><br/><br/>
### Layout
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QPushButton('OK', self).move(50,50)
        QtWidgets.QPushButton('Cancel', self).move(50,70)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
    
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


<br/><br/><br/>
### Buttons
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

    window = Window()
    window.show()
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

**[Combo Box]**
```python
```

**[Command Link Button]**
```python
```

**[Dialog Button Box]**
```python
```
