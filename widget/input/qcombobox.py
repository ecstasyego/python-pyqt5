from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QComboBox(self)
        widget.addItem('Option1')
        widget.addItem('Option2')
        widget.addItem('Option3')
        widget.addItem('Option4')

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
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
