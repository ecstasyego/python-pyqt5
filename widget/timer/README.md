## Timer

**Datetime Format**
- Date
  - d:   The day as a number without a leading zero (1 to 31)
  - dd:  The day as a number with a leading zero (01 to 31)
  - ddd: The abbreviated day name ('Mon' to 'Sun').
  - dddd:    The long day name ('Monday' to 'Sunday').
  - M:   The month as a number without a leading zero (1 to 12)
  - MM:  The month as a number with a leading zero (01 to 12)
  - MMM: The abbreviated month name ('Jan' to 'Dec').
  - MMMM:    The long month name ('January' to 'December').
  - yy:  The year as a two digit number (00 to 99)
  - yyyy:    The year as a four digit number. If the year is negative, a minus sign is prepended, making five characters.
- Time
  - h:   The hour without a leading zero (0 to 23 or 1 to 12 if AM/PM display)
  - hh:  The hour with a leading zero (00 to 23 or 01 to 12 if AM/PM display)
  - H:   The hour without a leading zero (0 to 23, even with AM/PM display)
  - HH:  The hour with a leading zero (00 to 23, even with AM/PM display)
  - m:   The minute without a leading zero (0 to 59)
  - mm:  The minute with a leading zero (00 to 59)
  - s:   The whole second, without any leading zero (0 to 59)
  - ss:  The whole second, with a leading zero where applicable (00 to 59)
  - z or zz: The fractional part of the second, to go after a decimal point, without trailing zeroes. Thus "s.z" reports the seconds to full available (millisecond) precision without trailing zeroes (0 to 999). For example, "s.z" would produce "0.25" for a time a quarter second into a minute.
  - zzz: The fractional part of the second, to millisecond precision, including trailing zeroes where applicable (000 to 999). For example, "ss.zzz" would produce "00.250" for a time a quarter second into a minute.
  - AP or A: Use AM/PM display. A/AP will be replaced by 'AM' or 'PM'. In localized forms (only relevant to QLocale::toString()), the locale-appropriate text is converted to upper-case.
  - ap or a: Use am/pm display. a/ap will be replaced by 'am' or 'pm'. In localized forms (only relevant to QLocale::toString()), the locale-appropriate text is converted to lower-case.
  - aP or Ap:    Use AM/PM display (since 6.3). aP/Ap will be replaced by 'AM' or 'PM'. In localized forms (only relevant to QLocale::toString()), the locale-appropriate text (returned by QLocale::amText() or QLocale::pmText()) is used without change of case.
  - t:   The timezone abbreviation (for example "CEST"). Note that time zone abbreviations are not unique. In particular, toString() cannot parse this.
  - tt:  The timezone's offset from UTC with no colon between the hours and minutes (for example "+0200").
  - ttt: The timezone's offset from UTC with a colon between the hours and minutes (for example "+02:00").
  - tttt:    The timezone name (for example "Europe/Berlin"). Note that this gives no indication of whether the datetime was in daylight-saving time or standard time, which may lead to ambiguity if the datetime falls in an hour repeated by a transition between the two. The name used is the one provided by QTimeZone::displayName() with the QTimeZone::LongName type. This may depend on the operating system in use.


```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # TIME
        time = QtCore.QTime.currentTime().toString('HH:mm:ss')

        # WIDGETS
        widget = QtWidgets.QLabel(self)
        widget.setText(f'Current Time: {time}')

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
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
