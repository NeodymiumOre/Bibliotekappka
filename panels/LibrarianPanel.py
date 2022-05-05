from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
from tabs.AddBookTab import AddBookTab
from tabs.AddItemTab import AddItemTab
from tabs.RemoveUserTab import RemoveUserTab
sys.path.append('../tabs')
from tabs.SearchTab import *
from tabs.AddUserTab import *
from tabs.RemoveUserTab import *
from tabs.AddItemTab import *
from tabs.AddBookTab import *

class LibrarianPanel(QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # creating buttons
        buttonSearch = QPushButton("Szukaj")
        buttonSearch.clicked.connect(self.on_buttonSearch_clicked)
        buttonAddUser = QPushButton("Dodaj uzytkownika")
        buttonAddUser.clicked.connect(self.on_buttonAddUser_clicked)
        buttonRemoveUser = QPushButton("Usun uzytkownika")
        buttonRemoveUser.clicked.connect(self.on_buttonRemoveUser_clicked)
        buttonAddItem = QPushButton("Dodaj egzemplarz ksiazki")
        buttonAddItem.clicked.connect(self.on_buttonAddItem_clicked)
        buttonAddBook = QPushButton("Dodaj ksiazke")
        buttonAddBook.clicked.connect(self.on_buttonAddBook_clicked)

        # creating side menu
        groupBoxMenu = QGroupBox()
        layoutMenu = QVBoxLayout()
        layoutMenu.addWidget(buttonSearch)
        layoutMenu.addWidget(buttonAddUser)
        layoutMenu.addWidget(buttonRemoveUser)
        layoutMenu.addWidget(buttonAddItem)
        layoutMenu.addWidget(buttonAddBook)
        groupBoxMenu.setLayout(layoutMenu)

        # creating tabs for stacking
        self.searchTab = SearchTab()
        self.addUserTab = AddUserTab()
        self.removeUserTab = RemoveUserTab()
        self.addItemTab = AddItemTab()
        self.addBookTab = AddBookTab()

        # creating stacked widget and index of the panels
        self.Stack = QStackedWidget(self)
        self.SearchTIndex = self.Stack.addWidget(self.searchTab)
        self.AddUserTIndex = self.Stack.addWidget(self.addUserTab)
        self.RemoveUserTIndex = self.Stack.addWidget(self.removeUserTab)
        self.AddItemTIndex = self.Stack.addWidget(self.addItemTab)
        self.AddBookTIndex = self.Stack.addWidget(self.addBookTab)

        # creating main layout
        layout = QHBoxLayout()
        layout.addWidget(groupBoxMenu)
        layout.addWidget(self.Stack)
        self.setLayout(layout)

    def UiWizard(self):
        pass

    def on_buttonSearch_clicked(self):
        self.Stack.setCurrentIndex(self.SearchTIndex)

    def on_buttonAddUser_clicked(self):
        self.Stack.setCurrentIndex(self.AddUserTIndex)

    def on_buttonRemoveUser_clicked(self):
        self.Stack.setCurrentIndex(self.RemoveUserTIndex)

    def on_buttonAddItem_clicked(self):
        self.Stack.setCurrentIndex(self.AddItemTIndex)

    def on_buttonAddBook_clicked(self):
        self.Stack.setCurrentIndex(self.AddBookTIndex)
