from ctypes import LibraryLoader
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
sys.path.insert(0, './panels')
from panels.StartPanel import *
from panels.LoginPanel import *
from panels.UserPanel import *
from panels.LibrarianPanel import *
from palette import *
sys.path.insert(0, './db')
from db.database import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db = Database()
        self.LibrarianName = None

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Bibliotekappka")

    def UiSetup(self):
        # centering window
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # creating panels for stacking
        self.startPanel = StartPanel(self)
        self.loginPanel = LoginPanel(self)
        self.userPanel = UserPanel(self)
        self.librarianPanel = LibrarianPanel(self)

        # creating stacked widget and index of the panels
        self.Stack = QStackedWidget(self)
        self.StartPIndex = self.Stack.addWidget(self.startPanel)
        self.LoginPIndex = self.Stack.addWidget(self.loginPanel)
        self.UserPIndex = self.Stack.addWidget(self.userPanel)
        self.LibrarianPIndex = self.Stack.addWidget(self.librarianPanel)

        # adding stacked widget to mainwindow widget
        self.setCentralWidget(self.Stack)

    def UiWizard(self):
        self.setStyleSheet("background-color: {}".format(Pallete.backgroundColor))

        # set size and placement of top-left corner
        self.setGeometry(480, 270, 960, 540)