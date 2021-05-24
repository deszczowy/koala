from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QTreeWidgetItem

class Leaf(QTreeWidgetItem):
    def __init__(self, parent, data):
        super(Leaf, self).__init__(parent)
        self.setFlags(self.flags() | Qt.ItemIsUserCheckable)
        self.setExpanded(True)

        self.update(data)

    def update(self, data):
        self.identifier = data[0]
        self.parent_id = data[1]
        self.caption = data[2]
        self.comment = data[3]
        self.reminder = data[4]
        if data[5] == "1":
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