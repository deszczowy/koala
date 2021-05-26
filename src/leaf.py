from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QTreeWidgetItem

from tool import *

class Leaf(QTreeWidgetItem):
    def __init__(self, parent, data):
        super(Leaf, self).__init__(parent)
        self.setFlags(self.flags() | Qt.ItemIsUserCheckable)
        self.setExpanded(True)

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
        self.setText(1, self.comment)

    def are_all_children_checked(self):
        for i in range(self.childCount()):
            if self.child(i).checkState(0) == Qt.Unchecked:
                return False
        return True