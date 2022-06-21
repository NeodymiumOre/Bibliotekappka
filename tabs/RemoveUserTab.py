from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
sys.path.insert(0, '../customWidgets')
from customWidgets.ListItem import *
from enums import Mode
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.engine import *

class RemoveUserTab(QWidget):
    def __init__(self, MainWindow, userAccount):
        super().__init__()
        self.userAccount = userAccount
        self.MainWindow = MainWindow
        self.db = self.MainWindow.db
        self.results = []
        self.counter = 0

        self.options = {
            'ID':0,
            'Imię':1,
            'Nazwisko':2
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
        self.db.conn.close()
        self.db.connect("librarian", "librarian")
        self.db.get_tables()
        self.listResults.clear()
        self.results.clear()
        phrase = self.lineEditSearch.displayText()

        # getting list of items from database
        if self.comboBoxSearch.currentIndex() == 0:
            res = self.db.session.query(self.db.Czytelnicy).filter(self.db.Czytelnicy.Id_karty.like(f"{phrase}")).all()
            s = select([self.db.Osoby, self.db.Czytelnicy]).where(self.db.Czytelnicy.Id_osoby == self.db.Osoby.Id_osoby)
            temp_list = self.db.conn.execute(s)
            for i in res:
                for j in temp_list:
                    if i.Id_osoby == j.Id_osoby:
                        self.results.append(j)
        elif self.comboBoxSearch.currentIndex() == 1:
            s = select([self.db.Osoby, self.db.Czytelnicy]).where(self.db.Czytelnicy.Id_osoby == self.db.Osoby.Id_osoby)
            temp_list = self.db.conn.execute(s)
            for i in temp_list:
                if i.Imie.lower() == phrase.lower():
                    self.results.append(i)
        elif self.comboBoxSearch.currentIndex() == 2:
            s = select([self.db.Osoby, self.db.Czytelnicy]).where(self.db.Czytelnicy.Id_osoby == self.db.Osoby.Id_osoby)
            temp_list = self.db.conn.execute(s)
            for i in temp_list:
                if i.Nazwisko.lower() == phrase.lower():
                    self.results.append(i)

        # s = select([self.db.Osoby, self.db.Czytelnicy]).where(self.db.Czytelnicy.Id_osoby == self.db.Osoby.Id_osoby)
        # result = self.db.conn.execute(s)

        # if there are any items, print them
        if True:#self.counter != 0:
            # adding items to QListWidget
            for user in self.results:
                item = QListWidgetItem(self.listResults)
                self.listResults.addItem(item)
                row = ListItem(self.db, f"{user.Imie} {user.Nazwisko} {user.Id_karty}", item, Mode.Delete, self.MainWindow.LibrarianName)
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


