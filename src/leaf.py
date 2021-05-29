from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QTreeWidgetItem

from tool import *

class Leaf(QTreeWidgetItem):
    def __init__(self, parent, data):
        super(Leaf, self).__init__(parent)
        self.setFlags(self.flags() | Qt.ItemIsUserCheckable)
        self.setExpanded(True)
        self.preview_mode = True
        self.update(data)

    def update(self, data):
        self.identifier = str(data[0])
        self.parent_id = str(data[1])
        self.caption = str(data[2])
        self.comment = desanitize(str(data[3]))
        self.reminder = str(data[4])
        if str(data[5]) == "1":
            self.setCheckState(0, Qt.Checked)
        else:
            self.setCheckState(0, Qt.Unchecked)

        self.setText(0, self.caption)
        self.update_mode()

    def update_mode(self):
        self.preview_mode = not self.preview_mode
        if self.preview_mode:
            self.setText(1, self.comment)
        else:
            self.setText(1, shorten(self.comment))

    def are_all_children_checked(self):
        for i in range(self.childCount()):
            if self.child(i).checkState(0) == Qt.Unchecked:
                return False
        return True

    def find(self, phrase):
        result = 0
        if self.caption.lower().find(phrase) >= 0:
            result += 1
        if self.comment.lower().find(phrase) >= 0:
            result += 2
        return result