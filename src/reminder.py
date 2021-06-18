from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLineEdit
import datetime
from tool import *

class Reminder(QWidget):
    def __init__(self, parent):
        super(Reminder, self).__init__(parent)
        self.date_and_time = QLineEdit()
        self.date_and_time.setInputMask("9999-99-99 99:99:99")
        self.check = QCheckBox()
        self.check.stateChanged.connect(self.enable)
        self.enable()

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.check)
        layout.addWidget(self.date_and_time)
        self.setLayout(layout)

    def enable(self):
        self.date_and_time.setEnabled(self.check.checkState() == Qt.Checked)

    def set_date(self, date=None):
        enabled = True
        if date is None or date_empty(date):
            enabled = False
            date = datetime.datetime.now().isoformat()
        
        if enabled:
            self.check.setCheckState(Qt.Checked)
        else:
            self.check.setCheckState(Qt.Unchecked)
        self.enable()
        
        self.date_and_time.setText(date)
    
    def clear(self):
        self.date_and_time.setText("")

    def date(self):
        if self.check.checkState() == Qt.Checked:
            return self.date_and_time.text()
        return ""