from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
sys.path.insert(0, '../customWidgets')
from customWidgets.ListItem import *
from enums import User

class RemoveUserTab(QWidget):
    def __init__(self, userAccount):
        self.userAccount = userAccount
        super().__init__()

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
        print(self.lineEditSearch.displayText())

        # creating list of items (maybe for operating on db in mirai)
        # searchingResults = []

        # adding items to QListWidget
        for number in range(1, 12):
            item = QListWidgetItem(self.listResults)
            self.listResults.addItem(item)
            row = ListItem(self.lineEditSearch.displayText() + str(number), item, User.Librarian)
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


