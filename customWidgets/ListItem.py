from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from enums import Mode

class ListItem(QWidget):
    def __init__(self, db, ItemName, item, mode, LibrarianName, parent=None):
        self.db = db
        self.ItemName = ItemName
        self.item = item
        self.mode = mode
        self.LibrarianName = LibrarianName
        super(ListItem, self).__init__(parent)

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # creating basic elements
        self.labelName = QLabel(self.ItemName)
        self.buttonDelete = QPushButton("Usuń użytkownika")
        self.buttonDelete.clicked.connect(self.on_buttonDelete_clicked)
        self.labelName2 = QLabel(self.ItemName)
        self.buttonReserve = QPushButton("Rezerwuj")
        self.buttonReserve.setCheckable(True)
        self.buttonReserve.clicked.connect(self.on_buttonReserve_clicked)
        self.buttonLend = QPushButton("Wypożycz")
        self.buttonLend.setCheckable(True)
        self.buttonLend.clicked.connect(self.on_buttonLend_clicked)
        if self.mode == Mode.Reader:
            self.buttonLend.setHidden(True)

        # creating items for reserving enrollment
        self.lineEditUserIdR = QLineEdit()
        self.buttonReserveAccept = QPushButton("Zatwierdź rezerwację")
        self.buttonReserveAccept.clicked.connect(self.on_buttonReserveAccept_clicked)

        # creating items for lending enrollment
        self.lineEditUserIdL = QLineEdit()
        self.buttonLendAccept = QPushButton("Zatwierdź wypożyczenie")
        self.buttonLendAccept.clicked.connect(self.on_buttonLendAccept_clicked)

        # creating widget for reserving enrollment
        self.enrollmentR = QWidget()
        self.layoutEnrollR = QHBoxLayout()
        self.layoutEnrollR.addWidget(self.lineEditUserIdR)
        self.layoutEnrollR.addWidget(self.buttonReserveAccept)
        self.enrollmentR.setLayout(self.layoutEnrollR)

        # creating widget for lending enrollment
        self.enrollmentL = QWidget()
        self.layoutEnrollL = QHBoxLayout()
        self.layoutEnrollL.addWidget(self.lineEditUserIdL)
        self.layoutEnrollL.addWidget(self.buttonLendAccept)
        self.enrollmentL.setLayout(self.layoutEnrollL)

        # creating basic widget for lending and reserving
        self.basic = QWidget()
        self.layoutListItem = QHBoxLayout()
        self.layoutListItem.addWidget(self.labelName)
        print(self.labelName.text())
        self.layoutListItem.addWidget(self.buttonLend)
        self.layoutListItem.addWidget(self.buttonReserve)
        self.basic.setLayout(self.layoutListItem)

        self.delete = QWidget()
        self.layoutDelete = QHBoxLayout()
        self.layoutDelete.addWidget(self.labelName2)
        self.layoutDelete.addWidget(self.buttonDelete)
        self.delete.setLayout(self.layoutDelete)

        # creating final layout
        if self.mode == Mode.Delete:
            self.layoutFinal = QVBoxLayout()
            self.layoutFinal.addWidget(self.delete)
            self.setLayout(self.layoutFinal)
        else:
            self.layoutFinal = QVBoxLayout()
            self.layoutFinal.addWidget(self.basic)
            self.layoutFinal.addWidget(self.enrollmentR)
            self.layoutFinal.addWidget(self.enrollmentL)
            self.enrollmentR.setHidden(True)
            self.enrollmentL.setHidden(True)
            self.setLayout(self.layoutFinal)

    def UiWizard(self):
        pass

    def on_buttonReserve_clicked(self):
        if self.buttonLend.isChecked():
            self.enrollmentL.setHidden(True)
            self.buttonLend.setChecked(False)
        # self.enrollmentR is shown
        if self.buttonReserve.isChecked():
            #self.buttonReserve.setText("Zwiń")
            self.enrollmentR.setHidden(False)
            self.setMinimumSize(self.basic.sizeHint() + self.enrollmentR.sizeHint())
            self.item.setSizeHint(self.minimumSizeHint())
        # self.enrollmentR is hidden
        else:
            #self.buttonEnroll.setText("Rozwiń")
            self.enrollmentR.setHidden(True)
            self.setMinimumSize(self.basic.sizeHint())
            self.item.setSizeHint(self.minimumSizeHint())

    def on_buttonLend_clicked(self):
        if self.buttonReserve.isChecked():
            self.enrollmentR.setHidden(True)
            self.buttonReserve.setChecked(False)
        # self.enrollmentL is shown
        if self.buttonLend.isChecked():
            #self.buttonReserve.setText("Zwiń")
            self.enrollmentL.setHidden(False)
            self.setMinimumSize(self.basic.sizeHint() + self.enrollmentL.sizeHint())
            self.item.setSizeHint(self.minimumSizeHint())
        # self.enrollmentL is hidden
        else:
            #self.buttonEnroll.setText("Rozwiń")
            self.enrollmentL.setHidden(True)
            self.setMinimumSize(self.basic.sizeHint())
            self.item.setSizeHint(self.minimumSizeHint())

    def on_buttonDelete_clicked(self):
        karta = self.labelName.text().split(' ')[2]
        imie = self.labelName.text().split(' ')[0]
        self.db.UsunCzytelnika(karta, imie)

    def on_buttonReserveAccept_clicked(self):
        self.db.DodawanieRezerwacji(self.lineEditUserIdR.text(), self.ItemName)

    def on_buttonLendAccept_clicked(self):
        result = self.db.session.query(self.db.Bibliotekarze).filter(self.db.Bibliotekarze.Login.like(f"{self.LibrarianName}")).one()
        self.db.DodawanieWypozyczenia(self.lineEditUserIdL.text(), 1, result.Id_bibliotekarza)
        



