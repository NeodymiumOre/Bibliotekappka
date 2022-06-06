from csv import list_dialects
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
sys.path.insert(0, '../customWidgets')
from customWidgets.ListItem import *
from enums import Mode
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.engine import *

class SearchTab(QWidget):
    def __init__(self, MainWindow, mode):
        super().__init__()
        self.mode = mode
        self.MainWindow = MainWindow
        self.db = self.MainWindow.db
        self.results = None

        self.options = {
            'Tytuł':0,
            'Autor':1,
            'Kategoria':2,
            'Wydawnictwo':3
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
        phrase = self.lineEditSearch.displayText()

        # getting list of items from database
        if self.comboBoxSearch.currentIndex() == 0:
            self.results = self.db.session.query(self.db.Ksiazki).filter(self.db.Ksiazki.Tytul.like(f"%{phrase}%")).all()
        # elif self.comboBoxSearch.currentIndex() == 1:
        #     # s = select([self.db.Autorzy, self.db.Ksiazki]).where(self.db.Autorzy.Id_ == self.db.Osoby.Id_osoby)
        #     # temp_list = self.db.conn.execute(s)
        #     # for i in temp_list:
        #     #     if i.Imie.lower() == phrase.lower():
        #     #         self.results.append(i)
        #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #     print(inspect(self.db.Autorzy).relationships.items())
        #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #     print(inspect(self.db.Ksiazki).relationships.items())
        #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #     #print(inspect(self.db.Ksiazki.autorzy_collection).columns.items())
        #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        #     s = select([self.db.Autorzy.ksiazki_collection, self.db.Ksiazki.autorzy_collection]).\
        #     where(self.db.Ksiazki.autorzy_collection.Id_ksiazki == phrase)
        #     self.results = self.db.conn.execute(s)

        #     #self.results = self.db.session.query(self.db.Ksiazki.autorzy_collection).filter(self.db.Ksiazki.autorzy_collection.Id_ksiazki.like(f"%{phrase}%"))
        #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #     num = 1
        #     for i in self.results:
        #         if i[0] == i[1] == True:
        #             print(num,   i)
        #         num += 1
        #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        # elif self.comboBoxSearch.currentIndex() == 2:
        #     self.results = self.db.session.query(self.db.Ksiazki).filter(self.db.Ksiazki.Kategoria.like(f"{phrase}%")).all()
        # elif self.comboBoxSearch.currentIndex() == 3:
        #     self.results = self.db.session.query(self.db.Ksiazki).filter(self.db.Ksiazki.Wydawnictwo.like(f"{phrase}%")).all()

        # if there are any items, print them
        if True: #len(self.results) != 0:
            # adding items to QListWidget
            for book in self.results:
                # adding ItemWidget to the ListWidget
                print("dfg", book)
                item = QListWidgetItem(self.listResults)
                self.listResults.addItem(item)
                row = ListItem(self.db, book.Tytul, item, self.mode, self.MainWindow.LibrarianName)
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


