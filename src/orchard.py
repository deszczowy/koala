from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from datetime import datetime

from tool import *
from tree import *
from task import *
from style import *
from timer import *
from directory import *

class Orchard(QMainWindow):

    def __init__(self):
        super(Orchard, self).__init__()
        self.directory = Directory()
        self.create_window()

        self.create_toolbar()
        self.create_buttons()
        self.compose_toolbar()

        self.create_workspace()
       
        self.compose_window()
        self.update_components()
        self.setup_window()

        self.timer = Timer(self)

    def create_buttons(self):
        self.button_add = QPushButton("\u271A") #+
        self.button_add.setObjectName("ToolBarButton")
        self.button_add.clicked.connect(self.action_add)
        self.button_add.setCursor(Qt.PointingHandCursor)
        self.button_add.setToolTip("Create new task")

        self.button_remove = QPushButton("\u2715") #x
        self.button_remove.setObjectName("ToolBarButton")
        self.button_remove.clicked.connect(self.action_delete)
        self.button_remove.setCursor(Qt.PointingHandCursor)
        self.button_remove.setToolTip("Remove selected task")

        self.button_recycle = QPushButton("\u2B6F") #recycle
        self.button_recycle.setObjectName("ToolBarButton")
        self.button_recycle.clicked.connect(self.action_recycle)
        self.button_recycle.setCursor(Qt.PointingHandCursor)
        self.button_recycle.setToolTip("Remove all done tasks")

        self.button_record = QPushButton("\U0001F5AD") #tape
        self.button_record.setObjectName("ToolBarButton")
        self.button_record.clicked.connect(self.action_record)
        self.button_record.setCursor(Qt.PointingHandCursor)
        self.button_record.setToolTip("Create new tape record snapshot backup")

    def create_toolbar(self):
        self.toolbar = QWidget()
        self.toolbar_layout = QVBoxLayout()
        self.toolbar_layout.setContentsMargins(0, 0, 0, 0)
        self.toolbar_layout.setSpacing(0)
        self.toolbar.setLayout(self.toolbar_layout)
        self.toolbar.setObjectName("ToolBar")

    def compose_toolbar(self):
        self.toolbar_layout.addWidget(self.button_add)
        self.toolbar_layout.addWidget(self.button_remove)
        self.toolbar_layout.addWidget(self.button_recycle)
        self.toolbar_layout.addWidget(self.button_record)
        self.toolbar_layout.addStretch()

    def create_window(self):
        self.window = QWidget()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def compose_window(self):
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.task)
        self.layout.addLayout(self.workspace)
        self.window.setLayout(self.layout)

    def create_workspace(self):
        self.workspace = QVBoxLayout()
        self.tree = Tree()
        self.task = Task()
        self.status = QLabel()
        self.status.setObjectName("StatusBar")
        self.status.setAlignment(Qt.AlignRight)
        self.workspace.addWidget(self.tree)
        self.workspace.addWidget(self.status)

    def setup_window(self):
        self.setWindowIcon(QIcon("./icon.png"))
        self.setMinimumSize(700, 500)
        self.setWindowTitle("Koala")
        self.setCentralWidget(self.window)
        self.setStyleSheet(application_stylesheet)
        self.tree.setFocus()

    def update_components(self):
        data = read_file(self.directory.storage)
        self.tree.fill(data)

    # buttons
    def action_add(self):
        item = None
        if len(self.tree.selectedItems()) > 0:
            item = self.tree.selectedItems()[0]
        self.task.show_window(self.tree, item)

    def action_delete(self):
        self.tree.remove_leaf()

    def action_recycle(self):
        self.tree.recycle()

    def action_record(self):
        file_name = self.directory.tapes + "tape_{}".format(datetime.now().strftime('%Y%m%d%H%M%S%f'))
        save_file(self.get_file_content(), file_name)
    #

    def action_save(self):
        if self.tree.modified:
            save_file(self.get_file_content(), self.directory.storage)
            self.tree.modified = False
            self.set_message("Saved")

    def get_file_content(self):
        return self.tree.get_data_sheet()

    def closeEvent(self, event):
        self.action_save()
        event.accept()

    def set_message(self, message):
        self.status.setText(message)
        self.timer.start()
    
    def clear_message(self):
        self.status.setText("")


