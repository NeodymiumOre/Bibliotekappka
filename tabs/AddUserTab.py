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
        self.warning = QLabel("")
        self.labelName = QLabel("Imię")
        self.lineEditName = QLineEdit()
        self.labelSurname = QLabel("Nazwisko")
        self.lineEditSurname = QLineEdit()
        self.labelCity = QLabel("Miasto")
        self.lineEditCity = QLineEdit()
        self.labelPostcode = QLabel("Kod pocztowy")
        self.lineEditPostCode = QLineEdit()
        self.labelStreet = QLabel("Ulica")
        self.lineEditStreet = QLineEdit(
        self.labelNumber = QLabel("Numer")
        self.lineEditNumber = QLineEdit()
        self.labelPhone = QLabel("Telefon")
        self.lineEditPhone = QLineEdit()
        self.labelEmail = QLabel("Email")
        self.lineEditEmail = QLineEdit()

        # mniejszy layout
        self.dy = QWidget()
        self.xdForm = QFormLayout()
        self.xdForm.addWidget(self.warning)
        self.xdForm.addWidget(self.labelName)
        self.xdForm.addWidget(self.lineEditName)
        self.xdForm.addWidget(self.labelSurname)
        self.xdForm.addWidget(self.lineEditSurname)
        self.xdForm.addWidget(self.labelCity)
        self.xdForm.addWidget(self.lineEditCity)
        self.xdForm.addWidget(self.labelPostcode)
        self.xdForm.addWidget(self.lineEditPostCode)
        self.xdForm.addWidget(self.labelStreet)
        self.xdForm.addWidget(self.lineEditStreet)
        self.xdForm.addWidget(self.labelNumber)
        self.xdForm.addWidget(self.lineEditNumber)
        self.xdForm.addWidget(self.labelPhone)
        self.xdForm.addWidget(self.lineEditPhone)
        self.xdForm.addWidget(self.labelEmail)
        self.xdForm.addWidget(self.lineEditEmail)
        self.dy.setLayout(self.xdForm)

        # bardziej ogólny layout
        self.dy = QWidget()
        self.ll = QHBoxLayout()
        self.ll.addWidget(self.dy)
        self.dy.setLayout(self.ll)

        self.buttonAdd = QPushButton("Dodaj użytkownika")
        self.buttonAdd.clicked.connect(self.on_buttonAdd_clicked)

        # creating main layout
        layout = QVBoxLayout()
        layout.addWidget(self.dy)
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

        if Imie=='' or Nazwisko=='' or Miasto=='' or Kod=='' or Ulica=='' or Numer=='' or Telefon=='' or Email=='':
            self.warning.setText("Don't leave blank lines!")
            self.warning.setStyleSheet("QLabel {color : red; }")
        else:
            self.db.DodawanieCzytelnika(Imie, Nazwisko, Miasto, Kod, Ulica, Numer, Telefon, Email)
            self.warning.setText("User added")
            self.warning.setStyleSheet("QLabel {color : black; }")

