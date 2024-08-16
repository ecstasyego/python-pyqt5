from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QToolBox()
        widget.addItem(QtWidgets.QWidget(), "ITEM1")
        widget.addItem(QtWidgets.QWidget(), "ITEM2")
        widget.addItem(QtWidgets.QWidget(), "ITEM3")
        widget.setStyleSheet("""
            QToolBox {
                border: 2px solid #333;
                background-color: #f0f0f0;
            }
            QToolBox::tab {
                background-color: #c0c0c0;
                padding: 5px;
                border: 1px solid #aaa;
            }
            QToolBox::tab:selected {
                background-color: #e0e0e0;
                border: 1px solid #555;
            }
        """)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
