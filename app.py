import sys
from MainWindow import *

app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec()