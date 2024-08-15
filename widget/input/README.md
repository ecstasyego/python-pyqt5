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
  - Signals: widget.textChanged[str].connect(self.callback)
  - Value: widget.text()
- [QDateEdit](https://doc.qt.io/qt-5/qdateedit.html)
  - Widget: widget = QtWidgets.QDateEdit()
  - Signals: widget.dateChanged.connect(self.callback)
  - Value: widget.date().toString('yyyy-MM-dd')
- [QTimeEdit](https://doc.qt.io/qt-5/qtimeedit.html)
  - Widget: widget = QtWidgets.QTimeEdit()
  - Signals: widget.timeChanged.connect(self.callback)
  - Value: widget.time().toString('HH:mm:ss')
- [QDateTimeEdit](https://doc.qt.io/qt-5/qdatetimeedit.html)
  - Widget: widget = QtWidgets.QDateTimeEdit()
  - Signals: widget.dateTimeChanged.connect(self.callback)
  - Signals: widget.dateChanged.connect(self.callback)
  - Signals: widget.timeChanged.connect(self.callback)
  - Value: widget.dateTime().toString('yyyy-MM-dd HH:mm:ss')
- [QSpinBox](https://doc.qt.io/qt-5/qspinbox.html)
  - Widget: widget = QtWidgets.QSpinBox()
  - Signals: widget.valueChanged.connect(self.callback)
  - Value: widget.value()
- [QDoubleSpinBox](https://doc.qt.io/qt-5/qdoublespinbox.html)
  - Widget: widget = QtWidgets.QDoubleSpinBox()
  - Signals: widget.valueChanged.connect(self.callback)
  - Value: widget.value()
- [QCheckBox](https://doc.qt.io/qt-5/qcheckbox.html)
  - Widget: widget = QtWidgets.QCheckBox()
  - Signals: widget.stateChanged.connect(self.callback)
  - Value: widget.checkState()
- [QComboBox](https://doc.qt.io/qt-5/qcombobox.html)
  - Widget: widget = QtWidgets.QComboBox()
  - Signals: widget.currentIndexChanged.connect(self.callback)
  - Signals: widget.currentTextChanged.connect(self.callback)
  - Signals: widget.activated.connect(self.callback)
  - Signals: widget.highlighted.connect(self.callback)
  - Value: widget.currentText()
- [QPushButton](https://doc.qt.io/qt-5/qpushbutton.html)
  - Widget: widget = QtWidgets.QPushButton()
  - Signals: widget.clicked.connect(self.callback)
  - Signals: widget.pressed.connect(self.callback)
  - Signals: widget.released.connect(self.callback)
  - Value: -
- [QRadioButton](https://doc.qt.io/qt-5/qradiobutton.html)
  - Widget: widget = QtWidgets.QRadioButton()
  - Signals: widget.toggled.connect(self.callback)
  - Value: widget.isChecked()
- [QSlider](https://doc.qt.io/qt-5/qslider.html)
  - Widget: widget = QtWidgets.QSlider()
  - Signals: widget..connect(self.callback)
  - Value: widget.()
- [QDial](https://doc.qt.io/qt-5/qdial.html)
  - Widget: widget = QtWidgets.QDial()
  - Signals: widget..connect(self.callback)
  - Value: widget.()
- [Q](https://doc.qt.io/qt-5/q.html)
  - Widget: widget = QtWidgets.()
  - Signals: widget..connect(self.callback)
  - Value: widget.()



