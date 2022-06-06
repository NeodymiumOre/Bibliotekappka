from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class AddBookTab(QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.db = self.MainWindow.db

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # adding elements to QFormLayout
        self.labelName = QLabel("Imię")
        self.lineEditName = QLineEdit()
        self.labelSurname = QLabel("Nazwisko")
        self.lineEditSurname = QLineEdit()
        self.labelTitle = QLabel("Tytuł")
        self.lineEditTitle = QLineEdit()
        self.labelISBN = QLabel("Numer ISBN")
        self.lineEditISBN = QLineEdit()
        self.labelYear = QLabel("Rok wydania")
        self.lineEditYear = QLineEdit()
        self.labelCategory = QLabel("Kategoria")
        self.lineEditCategory = QLineEdit()
        self.labelPublisher = QLabel("Wydawnictwo")
        self.lineEditPublisher = QLineEdit()

        # mniejszy layout
        self.cycki = QWidget()
        self.dupaForm = QFormLayout()
        self.dupaForm.addWidget(self.labelName)
        self.dupaForm.addWidget(self.lineEditName)
        self.dupaForm.addWidget(self.labelSurname)
        self.dupaForm.addWidget(self.lineEditSurname)
        self.dupaForm.addWidget(self.labelTitle)
        self.dupaForm.addWidget(self.lineEditTitle)
        self.dupaForm.addWidget(self.labelISBN)
        self.dupaForm.addWidget(self.lineEditISBN)
        self.dupaForm.addWidget(self.labelYear)
        self.dupaForm.addWidget(self.lineEditYear)
        self.dupaForm.addWidget(self.labelCategory)
        self.dupaForm.addWidget(self.lineEditCategory)
        self.dupaForm.addWidget(self.labelPublisher)
        self.dupaForm.addWidget(self.lineEditPublisher)
        self.cycki.setLayout(self.dupaForm)

        # bardziej ogólny layout
        self.cycekMniejszy = QWidget()
        self.dupa = QHBoxLayout()
        # self.spacerL = QSpacerItem(40, 10)
        # self.dupa.addWidget(self.spacerL)
        self.dupa.addWidget(self.cycki)
        # self.spacerR = QSpacerItem(40, 10)
        # self.dupa.addWidget(self.spacerR)
        self.cycekMniejszy.setLayout(self.dupa)

        self.buttonAdd = QPushButton("Dodaj książkę")
        self.buttonAdd.clicked.connect(self.on_buttonAdd_clicked)

        # creating main layout
        layout = QVBoxLayout()
        layout.addWidget(self.cycekMniejszy)
        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def UiWizard(self):
        pass

    def on_buttonAdd_clicked(self):
        Imie = self.lineEditName.text()
        Nazwisko = self.lineEditSurname.text()
        Tytul = self.lineEditTitle.text()
        ISBN = self.lineEditISBN.text()
        Rok = self.lineEditYear.text()
        Kategoria = self.lineEditCategory.text()
        Wydawnictwo = self.lineEditPublisher.text()

        self.db.DodawanieKsiazki(Imie, Nazwisko, Tytul, ISBN, Rok, Kategoria, Wydawnictwo)
