from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.uic import loadUi

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('Ui_MainWindow.ui', self)
        self.show()

        # centering window on screen
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # connecting signals and slots
        self.setupUi()
        self.makeConnection()

    def setupUi(self):
        ##################### StartPanel setup ####################################

        # creating indexes for panels
        self.StartPIndex = 0
        self.LoginPIndex = 1
        self.UserPIndex = 2
        self.LibrarianPIndex = 3

        ##################### LibrarianPanel setup ####################################

        # creating indexes for tabs
        self.SearchTIndex = 0
        self.AddUserTIndex = 1
        self.DelUserTIndex = 2
        self.AddBkCpyTIndex = 3
        self.AddBookTIndex = 4

    def makeConnection(self):
        ##################### StartPanel connections ####################################
        # self.pushButtonLibrarian.clicked.connect(self.on_pushButtonLibrarian_clicked)
        pass

    ######################### StartPanel Slots ##########################################

    def on_pushButtonLibrarian_clicked(self):
        self.Stack.setCurrentIndex(self.LoginPIndex)

    def on_pushButtonUser_clicked(self):
        self.Stack.setCurrentIndex(self.UserPIndex)

    ######################### LoginPanel Slots ##########################################

    def on_pushButtonSignIn_clicked(self):
        self.Stack.setCurrentIndex(self.LibrarianPIndex)
        print(self.lineEditName.displayText())
        print(self.lineEditPasswd.displayText())

    def on_pushButtonShowPasswd_clicked(self):
        if self.pushButtonShowPasswd.isChecked():
            self.lineEditPasswd.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEditPasswd.setEchoMode(QLineEdit.EchoMode.Password)

    ######################### LibrarianPanel Slots ##########################################

    def on_pushButtonSearchTab_clicked(self):
        self.stackedWidgetFunctions.setCurrentIndex(self.SearchTIndex)

    def on_pushButtonAddUserTab_clicked(self):
        self.stackedWidgetFunctions.setCurrentIndex(self.AddUserTIndex)

    def on_pushButtonDelUser_clicked(self):
        self.stackedWidgetFunctions.setCurrentIndex(self.DelUserTIndex)

    def on_pushButtonAddBkCpyTab_clicked(self):
        self.stackedWidgetFunctions.setCurrentIndex(self.AddBkCpyTIndex)

    def on_pushButtonAddBookTab(self):
        self.stackedWidgetFunctions.setCurrentIndex(self.AddBookTIndex)

    ######################### UserPanel Slots ##########################################

