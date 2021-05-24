import re
import uuid

def new_id():
    return str(uuid.uuid4().hex)

def decompose_leaf(line):
    if line != "":
        m = re.match(r"(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*)", line)
        if len(m.groups()) == 6:
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
    with open (file_name, "r") as tree_file:
        lines=tree_file.readlines()

    leafs = []

    for line in lines:
        leafs.append(decompose_leaf(line.strip()))

    return leafs

def save_file(content, file_name):
    if file_name == None:
        file_name = "./leafs.txt"
    with open(file_name, "w+") as _file:
        _file.write(content)

def get_file_contents(path):
    content = []
    with open(path, 'r') as _file:
        content = _file.readlines() 
    return content