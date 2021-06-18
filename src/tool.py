import re
import uuid

from PyQt5.QtWidgets import QMessageBox

def new_id():
    return str(uuid.uuid4().hex)

def decompose_leaf(line):
    if line != "":
        m = re.match(r"(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*)", line)
        if m != None and len(m.groups()) == 6:
            return (
                m.group(1),
                m.group(2),
                m.group(3),
                m.group(4),
                m.group(5),
                m.group(6)
            )
        return (new_id(), "_", "", "", "", "0")

def read_file(file_name):
    if file_name == None:
        file_name = "./leafs.txt"

    section = 0
    with open (file_name, mode="r", encoding="utf-8") as tree_file:
        lines=tree_file.readlines()

    leafs = []

    for line in lines:
        leafs.append(decompose_leaf(line.strip()))

    return leafs

def save_file(content, file_name):
    if file_name == None:
        file_name = "./leafs.txt"
    with open(file_name, mode="w+", encoding="utf-8") as _file:
        _file.write(content)

def get_file_contents(path):
    content = []
    with open(path, mode="r", encoding="utf-8") as _file:
        content = _file.readlines() 
    return content

def ask(title, question):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)

    msg.setText(question)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    if msg.exec() == QMessageBox.Yes:
        return True
    else:
        return False

def sanitize(text):
    return text.replace("\n", "\u0003").replace("\r", "\u0002").replace("|", "\u0019")

def desanitize(text):
    return text.replace("\u0003", "\n").replace("\u0002", "\r").replace("\u0019", "|")

def shorten(text):
    limit = 50
    line_end = text.find("\n")

    if line_end < 0 and len(text) < limit:
        return text

    if line_end < 0 or line_end > limit:
        line_end = limit
    return text[:line_end] + "..."

def date_empty(date):
    return date.replace(":", "").replace("-", "").strip() == ""