from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from palette import *

class StartPanel(QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # creating buttons
        self.buttonUser = QPushButton("Uzytkownik")
        self.buttonUser.clicked.connect(self.on_buttonUser_clicked)
        self.buttonLibrarian = QPushButton("Bibliotekarz")
        self.buttonLibrarian.clicked.connect(self.on_buttonLibrarian_clicked)

        # creating layout, adding buttons
        layout = QVBoxLayout()
        layout.addWidget(self.buttonUser)
        layout.addWidget(self.buttonLibrarian)

        self.setLayout(layout)

    def UiWizard(self):
        self.buttonUser.setStyleSheet("background-color: {}".format(Pallete.buttonColor))
        self.buttonLibrarian.setStyleSheet("background-color: {}".format(Pallete.buttonColor))

    def on_buttonUser_clicked(self):
        self.MainWindow.Stack.setCurrentIndex(self.MainWindow.UserPIndex)

    def on_buttonLibrarian_clicked(self):
        self.MainWindow.Stack.setCurrentIndex(self.MainWindow.LoginPIndex)

