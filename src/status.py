from PyQt5.QtWidgets import QLabel

class Status(QLabel):

    def __init__(self, parent):
        super(Status, self).__init__(parent)
        self.p = parent

    def mousePressEvent(self, event):
        if self.p != None:
            self.p.tree.clearSelection()