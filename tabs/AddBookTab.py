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
        self.warning = QLabel("")
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
        self.xdForm = QFormLayout()
        self.xdForm.addWidget(self.warning)
        self.xdForm.addWidget(self.labelName)
        self.xdForm.addWidget(self.lineEditName)
        self.xdForm.addWidget(self.labelSurname)
        self.xdForm.addWidget(self.lineEditSurname)
        self.xdForm.addWidget(self.labelTitle)
        self.xdForm.addWidget(self.lineEditTitle)
        self.xdForm.addWidget(self.labelISBN)
        self.xdForm.addWidget(self.lineEditISBN)
        self.xdForm.addWidget(self.labelYear)
        self.xdaForm.addWidget(self.lineEditYear)
        self.xdForm.addWidget(self.labelCategory)
        self.xdForm.addWidget(self.lineEditCategory)
        self.xdForm.addWidget(self.labelPublisher)
        self.xdForm.addWidget(self.lineEditPublisher)
        self.de.setLayout(self.xdForm)

        # bardziej ogólny layout
        self.cf = QWidget()
        self.ll = QHBoxLayout()
        self.ll.addWidget(self.de)
        self.cf.setLayout(self.ll)

        self.buttonAdd = QPushButton("Dodaj książkę")
        self.buttonAdd.clicked.connect(self.on_buttonAdd_clicked)

        # creating main layout
        layout = QVBoxLayout()
        layout.addWidget(self.cf)
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

        if Imie=='' or Nazwisko=='' or Tytul=='' or ISBN=='' or Rok=='' or Kategoria=='' or Wydawnictwo=='':
            self.warning.setText("Don't leave blank lines!")
            self.warning.setStyleSheet("QLabel {color : red; }")
        else:
            self.db.DodawanieKsiazki(Imie, Nazwisko, Tytul, ISBN, Rok, Kategoria, Wydawnictwo)
            self.warning.setText("Book added to library!")
            self.warning.setStyleSheet("QLabel {color : black; }")
