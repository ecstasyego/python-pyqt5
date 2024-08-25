"""
[PyQt5.QtCore.Qt]
- Window States: Qt.WindowNoState, Qt.WindowMinimizeda, Qt.WindowMaximized, Qt.WindowFullScreen
- Window Flags: Qt.Window, Qt.Dialog, Qt.Popup, Qt.Tool, Qt.Sheet, Qt.FramelessWindowHint, Qt.WindowStaysOnTopHint
- Widget States(1): Qt.Active, Qt.Inactive
- Widget States(2): Qt.Widget, Qt.Tool, Qt.Dialog, Qt.Popup, Qt.Sheet
- Alignment: Qt.AlignLeft, Qt.AlignRight, Qt.AlignTop, Qt.AlignBottom, Qt.AlignCenter, Qt.AlignHCenter, Qt.AlignVCenter
- Button States: Qt.Checked, Qt.Unchecked, Qt.PartiallyChecked
- Modes: Qt.NormalMode, Qt.CompactMode
_ Register Modes: Qt.LeftToRight, Qt.RightToLeft
- Key Codes: Qt.Key_Enter, Qt.Key_Escape, Qt.Key_Space, Qt.Key_Tab

[PyQt5.QtCore.QEvent]
- QEvent.None, QEvent.FocusIn, QEvent.FocusOut,
- QEvent.MouseButtonPress, QEvent.MouseButtonRelease, QEvent.MouseButtonDblClick, QEvent.MouseMove,
- QEvent.KeyPress, QEvent.KeyRelease,
- QEvent.Enter, QEvent.Close, QEvent.Leave, QEvent.Resize, QEvent.Move, QEvent.Paint, QEvent.Wheel,
- QEvent.WindowStateChange,
- QEvent.Show, QEvent.Hide, QEvent.ContextMenu
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMaximized:
                print("Window maximized")
            elif self.windowState() & QtCore.Qt.WindowNoState:
                print("Window restored")
        super().changeEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
