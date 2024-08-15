## Widgets
`QtWidgets.QWidget`
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
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
        layout = QtWidgets.QVBoxLayout()
        widget = QtWidgets.QWidget()
        layout.addWidget(widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        pass

    def get_widgets(self):
        layout = self.layout()
        widgets = list()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widgets.append(widget)
        return widgets

    def get_sublayouts(self):
        layout = self.layout()
        sublayouts = list()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item is not None:
                sublayout = item.layout()
                if sublayout is not None:
                    sublayouts.append(sublayout)
        return sublayouts

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

**[Check Box]**
```python
```

**[Command Link Button]**
```python
```

**[Dialog Button Box]**
```python
```
