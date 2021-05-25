from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QTextEdit, QInputDialog, QShortcut, QLabel
from tool import *

class Task(QWidget):

    def __init__(self):
        super(Task, self).__init__()
        self.layout = QHBoxLayout()
        self.parent_node_identifier = "_"
        self.tree = None

        self.buttons = QHBoxLayout()
        self.button_add = QPushButton("Add")
        self.button_add.clicked.connect(self.add)
        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.clicked.connect(self.cancel)
        self.buttons.addWidget(self.button_add)
        self.buttons.addStretch()
        self.buttons.addWidget(self.button_cancel)

        self.form = QVBoxLayout()
        self.caption = QLineEdit()
        self.comment = QTextEdit()
        self.parent_info = QLabel()
        self.form.addLayout(self.buttons)
        self.form.addWidget(self.caption)
        self.form.addWidget(self.comment)
        self.form.addWidget(self.parent_info)

        shortcut_add = QShortcut(QKeySequence("Ctrl+Q"), self)
        shortcut_cnl = QShortcut(QKeySequence("Esc"), self)
        shortcut_add.activated.connect(self.add)
        shortcut_cnl.activated.connect(self.cancel)
        
        self.setLayout(self.form)
        self.reset()
        self.hide()

    def reset(self):
        self.caption.setText("")
        self.comment.setText("")
        self.parent_info.setText("")
        self.tree = None

    def show_window(self, tree, parent_node):
        title = "New task"
        self.tree = tree        
        if parent_node != None:
            title = "New task for '{}'".format(parent_node.caption)
            self.parent_node_identifier = parent_node.identifier
        self.parent_info.setText(title)
        self.caption.setFocus()
        self.show()

    def add(self):
        leaf = (
            new_id(), 
            self.parent_node_identifier, 
            self.caption.text(), 
            self.comment.toPlainText(), 
            "",
            "0"
        )
        self.tree.add_leaf(leaf)
        self.cancel()
    
    def cancel(self):
        self.reset()
        self.hide()

