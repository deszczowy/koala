from PyQt5.QtWidgets import QApplication, QStyleFactory
import sys
from orchard import *

def main(): 
    app = QApplication (sys.argv)
    window = Orchard()
    window.show()
    sys.exit(app.exec_())

    """
        print ("Item: {}, Parent: {}".format(
            item.caption(), 
            "_" if item.parent() == None else item.parent().caption())
        )
    """

if __name__ == '__main__':
    main()