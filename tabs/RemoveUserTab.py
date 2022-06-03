from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
sys.path.insert(0, '../customWidgets')
from customWidgets.ListItem import *
from enums import User

class RemoveUserTab(QWidget):
    def __init__(self, MainWindow, userAccount):
        super().__init__()
        self.userAccount = userAccount
        self.MainWindow = MainWindow
        self.db = self.MainWindow.db
        self.results

        self.options = {
            'ID':0,
            'Imię':1,
            'Nazwisko':2,
            'Adres':3
        }

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # creating searching elements
        self.comboBoxSearch = QComboBox()
        self.comboBoxSearch.currentIndexChanged.connect(self.comboBoxSearch_changedCurrentIndex)
        self.lineEditSearch = QLineEdit()
        self.lineEditSearch.returnPressed.connect(self.lineEditSearch_pressed)
        self.buttonSearch = QPushButton("Szukaj")
        self.buttonSearch.clicked.connect(self.on_buttonSearch_clicked)

        for option in self.options:
            self.comboBoxSearch.addItem(option)

        # creating top section for searching
        groupBoxSearch = QGroupBox()
        layoutSearch = QHBoxLayout()
        layoutSearch.addWidget(self.comboBoxSearch)
        layoutSearch.addWidget(self.lineEditSearch)
        layoutSearch.addWidget(self.buttonSearch)
        groupBoxSearch.setLayout(layoutSearch)

        # creating bottom section for searching results
        self.listResults = QListWidget()

        # creating main layout
        layout = QVBoxLayout()
        layout.addWidget(groupBoxSearch)
        layout.addWidget(self.listResults)
        self.setLayout(layout)

    def UiWizard(self):
        pass

    def comboBoxSearch_changedCurrentIndex(self):
        print(self.comboBoxSearch.currentIndex())

    def lineEditSearch_pressed(self):
        self.on_buttonSearch_clicked()

    def on_buttonSearch_clicked(self):
        self.listResults.clear()
        phrase = self.lineEditSearch.displayText()

        # getting list of items from database
        if self.comboBoxSearch.currentIndex() == 0:
            self.results = self.db.session.query(self.db.Czytelnicy).filter(self.db.Czytelnicy.Id_karty.like(f"{phrase}%")).all()
        elif self.comboBoxSearch.currentIndex() == 1:
            self.results = self.db.session.query(self.db.Czytelnicy).filter(self.db.Czytelnicy.Imie.like(f"{phrase}%")).all()
        elif self.comboBoxSearch.currentIndex() == 2:
            self.results = self.db.session.query(self.db.Czytelnicy).filter(self.db.Czytelnicy.Nazwisko.like(f"{phrase}%")).all()
        elif self.comboBoxSearch.currentIndex() == 3:
            self.results = self.db.session.query(self.db.Czytelnicy).filter(self.db.Czytelnicy.Adres.like(f"{phrase}%")).all()

        # if there are any items, print them
        if len(self.results) != 0:
            # adding items to QListWidget
            for user in self.results:
                item = QListWidgetItem(self.listResults)
                self.listResults.addItem(item)
                row = ListItem(user.Imie, item, User.Librarian)
                row.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
                item.setSizeHint(row.minimumSizeHint())
                self.listResults.setItemWidget(item, row)

        # # creating item of type QListWidgetItem
        # self.item1 = QListWidgetItem(self.listResults)
        # # adding item1 to listResults
        # self.listResults.addItem(self.item1)
        # # creating row of type ListItem
        # self.row = ListItem(self.lineEditSearch.displayText())
        # # setting size of item1
        # self.item1.setSizeHint(self.row.minimumSizeHint())
        # # displays row in item
        # self.listResults.setItemWidget(self.item1, self.row)


