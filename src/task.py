from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QTextEdit, QInputDialog, QShortcut, QLabel

from tool import *
from leaf import *
from reminder import *

class Task(QWidget):

    def __init__(self, parent):
        super(Task, self).__init__(parent)
        self.parent = parent
        self.setFixedWidth(300)
        self.layout = QHBoxLayout()
        self.parent_node_identifier = "_"
        self.edited = None

        self.buttons = QHBoxLayout()
        self.button_confirm = QPushButton("Add")
        self.button_confirm.clicked.connect(self.confirm)
        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.clicked.connect(self.cancel)
        self.buttons.addWidget(self.button_confirm)
        self.buttons.addStretch()
        self.buttons.addWidget(self.button_cancel)

        self.form = QVBoxLayout()
        self.caption = QLineEdit()
        self.caption.returnPressed.connect(self.go_to_comment)
        self.reminder = Reminder(self)
        self.comment = QTextEdit()
        self.parent_info = QLabel()
        self.form.addLayout(self.buttons)
        self.form.addWidget(self.caption)
        self.form.addWidget(self.reminder)
        self.form.addWidget(self.comment)
        self.form.addWidget(self.parent_info)

        shortcut_cfm = QShortcut(QKeySequence("Ctrl+Q"), self)
        shortcut_cnl = QShortcut(QKeySequence("Esc"), self)
        shortcut_cfm.activated.connect(self.confirm)
        shortcut_cnl.activated.connect(self.cancel)
        
        self.setLayout(self.form)
        self.reset()
        self.hide()        

    def reset(self):
        self.caption.setText("")
        self.comment.setText("")
        self.reminder.clear()
        self.parent_info.setText("")
        self.edited = None

    def show_add(self, parent_node):
        self.button_confirm.setText("Add")
        title = "New task"       
        if parent_node != None:
            title = "New task for '{}'".format(parent_node.caption)
            self.parent_node_identifier = parent_node.identifier
        else:
            self.parent_node_identifier = "_"
        self.parent_info.setText(title)
        self.reminder.set_date()
        self.caption.setFocus()
        self.show()

    def show_edit(self, leaf):
        self.button_confirm.setText("Save")
        self.edited = leaf
        self.caption.setText(leaf.caption)
        self.comment.setText(leaf.comment)
        self.reminder.set_date(leaf.reminder)
        self.caption.setFocus()
        self.show()

    def confirm(self):
        if self.edited == None:
            leaf = (
                new_id(), 
                self.parent_node_identifier, 
                self.caption.text(), 
                self.comment.toPlainText(), 
                self.reminder.date(),
                "0"
            )
            self.parent.tree.add_leaf(leaf)
        else:
            self.edited.preview_mode = not self.edited.preview_mode
            self.edited.update(
                (
                    self.edited.identifier,
                    self.edited.parent_id,
                    self.caption.text(),
                    self.comment.toPlainText(),
                    self.reminder.date(),
                    "0" if self.edited.checkState(0) == Qt.Unchecked else "1"
                )
            )

        self.cancel()
    
    def cancel(self):
        self.parent.unlock_workspace()
        self.reset()
        self.hide()

    def go_to_comment(self):
        self.comment.setFocus()

