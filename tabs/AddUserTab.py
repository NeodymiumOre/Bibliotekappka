from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class AddUserTab(QWidget):
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
        self.labelCity = QLabel("Miasto")
        self.lineEditCity = QLineEdit()
        self.labelPostcode = QLabel("Kod pocztowy")
        self.lineEditPostCode = QLineEdit()
        self.labelStreet = QLabel("Ulica")
        self.lineEditStreet = QLineEdit()
        self.labelNumber = QLabel("Numer")
        self.lineEditNumber = QLineEdit()
        self.labelPhone = QLabel("Telefon")
        self.lineEditPhone = QLineEdit()
        self.labelEmail = QLabel("Email")
        self.lineEditEmail = QLineEdit()

        # mniejszy layout
        self.cycki = QWidget()
        self.dupaForm = QFormLayout()
        self.dupaForm.addWidget(self.labelName)
        self.dupaForm.addWidget(self.lineEditName)
        self.dupaForm.addWidget(self.labelSurname)
        self.dupaForm.addWidget(self.lineEditSurname)
        self.dupaForm.addWidget(self.labelCity)
        self.dupaForm.addWidget(self.lineEditCity)
        self.dupaForm.addWidget(self.labelPostcode)
        self.dupaForm.addWidget(self.lineEditPostCode)
        self.dupaForm.addWidget(self.labelStreet)
        self.dupaForm.addWidget(self.lineEditStreet)
        self.dupaForm.addWidget(self.labelNumber)
        self.dupaForm.addWidget(self.lineEditNumber)
        self.dupaForm.addWidget(self.labelPhone)
        self.dupaForm.addWidget(self.lineEditPhone)
        self.dupaForm.addWidget(self.labelEmail)
        self.dupaForm.addWidget(self.lineEditEmail)
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

        self.buttonAdd = QPushButton("Dodaj użytkownika")
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
        Miasto = self.lineEditCity.text()
        Kod = self.lineEditPostCode.text()
        Ulica = self.lineEditStreet.text()
        Numer = self.lineEditNumber.text()
        Telefon = self.lineEditPhone.text()
        Email = self.lineEditEmail.text()

        self.db.DodawanieCzytelnika(Imie, Nazwisko, Miasto, Kod, Ulica, Numer, Telefon, Email)

