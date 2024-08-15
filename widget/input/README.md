## Input Widgets
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QWidget()
        self.widgets['widget2'] = QtWidgets.QWidget()
        self.widgets['widget3'] = QtWidgets.QWidget()

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addWidget(self.widgets['widget2'])
        layout.addWidget(self.widgets['widget3'])
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
        # WIDGETS
        widget1 = QtWidgets.QWidget()
        widget2 = QtWidgets.QWidget()
        widget3 = QtWidgets.QWidget()

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        layout.addWidget(widget3)
        layout.addStretch(1)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        pass

    def get_widgets(self, layout=None):
        layout = self.layout() if layout is None else layout
        widgets = list()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widgets.append(widget)
        return widgets

    def get_sublayouts(self, layout=None):
        layout = self.layout() if layout is None else layout
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

### Callbacks
- [QLineEdit](https://doc.qt.io/qt-5/qlineedit.html)
  - Widget: widget = QtWidgets.QLineEdit()
  - Callback: widget.textChanged[str].connect(self.callback)
  - Value: widget.text()
- [QDateEdit](https://doc.qt.io/qt-5/qdateedit.html)
  - Widget: widget = QtWidgets.QDateEdit()
  - Callback: widget.dateChanged.connect(self.callback)
  - Value: widget.date().toString('yyyy-MM-dd')
- [QTimeEdit](https://doc.qt.io/qt-5/qtimeedit.html)
  - Widget: widget = QtWidgets.QTimeEdit()
  - Callback: widget.timeChanged.connect(self.callback)
  - Value: widget.time().toString('HH:mm:ss')
- [QDateTimeEdit](https://doc.qt.io/qt-5/qdatetimeedit.html)
  - Widget: widget = QtWidgets.QDateTimeEdit()
  - Callback: widget.dateTimeChanged.connect(self.callback)
  - Value: widget.dateTime().toString('yyyy-MM-dd HH:mm:ss')
- [QSpinBox](https://doc.qt.io/qt-5/qspinbox.html)
  - Widget: widget = QtWidgets.QSpinBox()
  - Callback: widget.valueChanged.connect(self.callback)
  - Value: widget.value()
- [QDoubleSpinBox](https://doc.qt.io/qt-5/qdoublespinbox.html)
  - Widget: widget = QtWidgets.QDoubleSpinBox()
  - Callback: widget.valueChanged.connect(self.callback)
  - Value: widget.value()



