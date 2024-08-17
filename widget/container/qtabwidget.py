from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QTabWidget()
        widget.addTab(QtWidgets.QWidget(), 'TAB1')
        widget.addTab(QtWidgets.QWidget(), 'TAB2')

        widget.setTabText(0, 'OLDTAB1')
        widget.setTabText(1, 'OLDTAB2')

        widget.removeTab(0)
        widget.insertTab(0, QtWidgets.QWidget(), 'UPDATED TAB1')
        widget.removeTab(1)
        widget.insertTab(1, QtWidgets.QWidget(), 'UPDATED TAB2')
        widget.insertTab(2, QtWidgets.QWidget(), 'NEW TAB2')

        tab_infos = list()
        for idx in range(widget.count()):
            tab_name = widget.tabText(idx)
            tab_widget = widget.widget(idx)
            tab_idx = widget.indexOf(tab_widget)
            tab_infos.append([idx, tab_name, tab_widget, tab_idx])

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
