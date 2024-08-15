from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget1 = QtWidgets.QPushButton('&Button1', self); widget1.setCheckable(True); widget1.toggle()
        widget2 = QtWidgets.QPushButton(self); widget2.setText('Button&2')
        widget3 = QtWidgets.QPushButton('Button3', self); widget3.setEnabled(False)

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        layout.addWidget(widget3)
        layout.addStretch(1)
        layout.addWidget(QtWidgets.QStatusBar())
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        status_widget = self.get_widgets()[-1]
        status_widget.showMessage("CallBack", 1000)

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
