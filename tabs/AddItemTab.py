from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class AddItemTab(QWidget):
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
        self.labelTitle = QLabel("Tytuł")
        self.lineEditTite = QLineEdit()
        self.labelPublisher = QLabel("Wydawnictwo")
        self.lineEditPublisher = QLineEdit()

        # mniejszy layout
        self.lilWidget = QWidget()
        self.formLayout = QFormLayout()
        self.formLayout.addWidget(self.warning)
        self.formLayout.addWidget(self.labelTitle)
        self.formLayout.addWidget(self.lineEditTite)
        self.formLayout.addWidget(self.labelPublisher)
        self.formLayout.addWidget(self.lineEditPublisher)
        self.lilWidget.setLayout(self.formLayout)

        # bardziej ogólny layout
        self.tabWidget = QWidget()
        self.tabLayout = QHBoxLayout()
        self.tabLayout.addWidget(self.lilWidget)
        self.tabWidget.setLayout(self.tabLayout)

        self.buttonAdd = QPushButton("Dodaj Egzemplarz")
        self.buttonAdd.clicked.connect(self.on_buttonAdd_clicked)

    def UiWizard(self):
        pass

        # creating main layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabWidget)
        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)

    def on_buttonAdd_clicked(self):
        Tytul = self.lineEditTite.text()
        Wydawnictwo = self.lineEditPublisher.text()

        if Tytul == '' or Wydawnictwo == '':
            self.warning.setText("Don't leave blank lines!")
            self.warning.setStyleSheet("QLabel {color : red; }")
        else:
            self.db.Add_egzemplarz(Tytul, Wydawnictwo)
            self.warning.setText("Position added to library!")
            self.warning.setStyleSheet("QLabel {color : black; }")
