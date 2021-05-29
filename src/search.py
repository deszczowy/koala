from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit

class SearchInput(QLineEdit):
    def __init__(self, parent):
        super(SearchInput, self).__init__(parent)
        self.setText("")
        self.setPlaceholderText("search")
    
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if self.text() != "":
            self.parent().show_button()
        else:
            self.parent().hide_button()
        

class Search(QWidget):

    def __init__(self):
        super(Search, self).__init__()
        self.phrase = ""

        self.field = SearchInput(self)
        self.button = QPushButton("X")
        self.button.setObjectName("SearchButton")
        self.button.clicked.connect(self.click)

        self.bar = QHBoxLayout()
        self.bar.addWidget(self.field)
        self.bar.addWidget(self.button)
        self.bar.setSpacing(0)
        self.bar.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.bar)
        
        self.hide_button()

    def hide_button(self):
        self.button.hide()

    def show_button(self):
        self.button.show()

    def click(self):
        self.field.setText("")
        self.hide_button()
        self.focus()

    def has_new_phrase(self):
        if self.phrase != self.field.text().strip().lower():
            self.phrase = self.field.text().strip().lower()
            return True
        return False

    def new_phrase(self):
        return self.phrase

    def focus(self):
        self.field.setFocus(True)
