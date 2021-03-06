#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# See http://doc.qt.io/qt-5/qcalendarwidget.html#details
# See also http://doc.qt.io/qt-5/qtwidgets-widgets-calendarwidget-example.html

import sys

from PyQt5.QtWidgets import QApplication, QCalendarWidget


def printValue():
    print(calendar.selectedDate())

app = QApplication(sys.argv)

calendar = QCalendarWidget()

calendar.selectionChanged.connect(printValue)

calendar.show()

# The mainloop of the application. The event handling starts from this point.
# The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.
exit_code = app.exec_()

# The sys.exit() method ensures a clean exit.
# The environment will be informed, how the application ended.
sys.exit(exit_code)
