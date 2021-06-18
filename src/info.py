from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

class Info(QWidget):

    def __init__(self):
        super(Info, self).__init__()

        myPixmap = QtGui.QPixmap('./icon.png')
        self.setMinimumSize(300, 300)
        self.setWindowTitle("I am Koala")

        layout = QVBoxLayout()
        logo = QLabel()
        logo.setFixedWidth(80)
        myScaledPixmap = myPixmap.scaled(logo.size(), QtCore.Qt.KeepAspectRatio)
        logo.setPixmap(myScaledPixmap)
        layout.addWidget(logo)

        about = QLabel()
        about.setText(self.content())
        about.setOpenExternalLinks(True)
        about.setWordWrap(True)
        layout.addWidget(about)

        layout.addStretch()

        buttons = QHBoxLayout()
        buttons.addStretch()
        ok = QPushButton("Ok")
        ok.clicked.connect(self.close)
        buttons.addWidget(ok)
        buttons.addStretch()
        layout.addLayout(buttons)

        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)
        self.center_window()
    
    def show_info(self):
        self.show()

    def content(self):
        return """
        This simple todo app is created by <a href=\"https://github.com/deszczowy\">Deszczowy</a>
        <br /><br />
        Version 0.8
        <br /><br />

        Icon was made by <a href=\"https://www.freepik.com\" title=\"Freepik\">Freepik</a> 
        from <a href=\"https://www.flaticon.com/\" title=\"Flaticon\">www.flaticon.com</a>.
        <br /><br />

        Ctrl+N - add task<br />
        Ctrl+E - edit task<br />
        Ctrl+D - delete task<br />
        Ctrl+R - remove all done tasks<br />
        Ctrl+B - save backup tape<br />
        """

    def close(self):
        self.hide()

    def center_window(self):
        geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        geometry.moveCenter(centerPoint)
        self.move(geometry.topLeft())