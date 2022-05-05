from csv import list_dialects
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class SearchTab(QWidget):
    def __init__(self):
        super().__init__()

        self.options = {
            'Tytul':0,
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
        # this section is temporary
        listResults = QListWidget()

        widgetResults = QWidget()
        layoutResults = QVBoxLayout()
        layoutResults.addWidget(listResults)
        widgetResults.setLayout(layoutResults)

        # creating main layout
        layout = QVBoxLayout()
        layout.addWidget(groupBoxSearch)
        layout.addWidget(widgetResults)
        self.setLayout(layout)

    def UiWizard(self):
        pass

    def comboBoxSearch_changedCurrentIndex(self):
        print(self.comboBoxSearch.currentIndex())

    def lineEditSearch_pressed(self):
        print(self.lineEditSearch.displayText())

    def on_buttonSearch_clicked(self):
        self.lineEditSearch_pressed()