from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItemIterator, QHeaderView
from leaf import *

class Tree(QTreeWidget):
    def __init__(self):
        super(Tree, self).__init__()
        self.setHeaderLabels(["Label", "Description"])
        self.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.model().dataChanged.connect(self.data_changed)
        self.modified = False

    def data_changed(self):
        self.modified = True

    def fill(self, leafs):
        for leaf in leafs:
            self.add_leaf(leaf)
        self.modified = False

    def add_leaf(self, leaf):
        parent = None
        if leaf[1] != "_":
            parent = self.find_node(leaf[1])
        
        if parent != None:
            node = Leaf(parent, leaf)
        else:
            node = Leaf(self, leaf)
        self.modified = True

    def remove_leaf(self):
        if len(self.selectedItems()) > 0:
            item = self.selectedItems()[0]

            if item != None:
                return self.remove_specified_leaf(item)
        return False

    def remove_specified_leaf(self, leaf):
        if not leaf.are_all_children_checked():
            return False
            
        if leaf.parent() is not None:
            leaf.parent().removeChild(leaf)
        else:
            self.takeTopLevelItem(self.indexOfTopLevelItem(leaf))
        self.modified = True
        return True

    def find_node(self, identifier):
        iterator = QTreeWidgetItemIterator(self)
        while iterator.value():
            item = iterator.value()
            if item.identifier == identifier:
                return item
            iterator += 1
        return None

    def get_data_sheet(self):
        sheet = ""
        iterator = QTreeWidgetItemIterator(self)
        while iterator.value():
            item = iterator.value()
            line = "{}|{}|{}|{}|{}|{}\n".format(
                item.identifier,
                item.parent_id,
                item.caption,
                sanitize(item.comment),
                item.reminder,
                "1" if item.checkState(0) == Qt.Checked else "0"
            )
            sheet += line
            iterator += 1
        return sheet

    def recycle(self):
        checked_list = []
        iterator = QTreeWidgetItemIterator(self)
        while iterator.value():
            item = iterator.value()
            if item.checkState(0) == Qt.Checked:
                checked_list.append(item)
            iterator += 1
        
        for i in range(len(checked_list)-1, -1, -1):
            if checked_list[i].are_all_children_checked():
                self.remove_specified_leaf(checked_list[i])

    def mousePressEvent(self, event):
        self.clearSelection()
        super().mousePressEvent(event)