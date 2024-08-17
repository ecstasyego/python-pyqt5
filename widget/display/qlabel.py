from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QLabel('First Label', self)
        self.widgets['widget2'] = QtWidgets.QLabel('Second Label', self)
        self.widgets['widget3'] = QtWidgets.QLabel(self)

        # WIDGETS: Properties
        font1 = self.widgets['widget1'].font(); font1.setPointSize(20)
        font2 = self.widgets['widget2'].font(); font2.setFamily('Times New Roman'); font2.setBold(True)
        self.widgets['widget1'].setFont(font1)
        self.widgets['widget2'].setFont(font2)
        self.widgets['widget3'].setFrameShape(QtWidgets.QFrame.Panel)
        self.widgets['widget1'].setAlignment(QtCore.Qt.AlignCenter)
        self.widgets['widget2'].setAlignment(QtCore.Qt.AlignVCenter)
        self.widgets['widget3'].setText('Third Label')

        # LAYOUTS
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
