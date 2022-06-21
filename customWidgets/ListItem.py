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
        self.errorsR = QLabel("")
        self.errorsL = QLabel("")
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
        self.ad = QWidget()
        self.ld = QVBoxLayout()
        self.layoutEnrollR = QHBoxLayout()
        self.layoutEnrollR.addWidget(self.lineEditUserIdR)
        self.layoutEnrollR.addWidget(self.buttonReserveAccept)
        self.ad.setLayout(self.layoutEnrollR)
        self.ld.addWidget(self.errorsR)
        self.ld.addWidget(self.ad)
        self.enrollmentR.setLayout(self.ld)

        # creating widget for lending enrollment
        self.enrollmentL = QWidget()
        self.yd = QWidget()
        self.xd = QVBoxLayout()
        self.layoutEnrollL = QHBoxLayout()
        self.layoutEnrollL.addWidget(self.lineEditUserIdL)
        self.layoutEnrollL.addWidget(self.buttonLendAccept)
        self.yd.setLayout(self.layoutEnrollL)
        self.xd.addWidget(self.errorsL)
        self.xd.addWidget(self.yd)
        self.enrollmentL.setLayout(self.xd)

        # creating basic widget for lending and reserving
        self.basic = QWidget()
        self.layoutListItem = QHBoxLayout()
        self.layoutListItem.addWidget(self.labelName)
        print(self.labelName.text())
        self.layoutListItem.addWidget(self.buttonLend)
        self.layoutListItem.addWidget(self.buttonReserve)
        self.basic.setLayout(self.layoutListItem)

        self.delete = QWidget()
        self.temp = QWidget()
        self.warning = QLabel("")
        self.templay = QVBoxLayout()
        self.layoutDelete = QHBoxLayout()
        self.layoutDelete.addWidget(self.labelName2)
        self.layoutDelete.addWidget(self.buttonDelete)
        self.temp.setLayout(self.layoutDelete)
        self.templay.addWidget(self.warning)
        self.templay.addWidget(self.temp)
        self.delete.setLayout(self.templay)

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

        if karta=='' or imie=='':
            self.warning.setText("Don't leave blank lines!")
            self.warning.setStyleSheet("QLabel {color : red; }")
        elif int(karta) > 11 or int(karta) < 0:
            self.warning.setText("Invalid card number!")
            self.warning.setStyleSheet("QLabel {color : red; }")
        else:
            self.warning.setText("User successfully deleted!")
            self.warning.setStyleSheet("QLabel {color : black; }")
            self.db.UsunCzytelnika(karta, imie)

    def on_buttonReserveAccept_clicked(self):
        if self.lineEditUserIdR.text() == "" or int(self.lineEditUserIdR.text()) > 3 or int(self.lineEditUserIdR.text()) < 0:
            self.errorsR.setText("Invalid card number!")
            self.errorsR.setStyleSheet("QLabel {color : red; }")
        else:
            self.db.DodawanieRezerwacji(self.lineEditUserIdR.text(), self.ItemName)
            self.errorsR.setText("Reserving is done!")
            self.errorsR.setStyleSheet("QLabel {color : black; }")

    def on_buttonLendAccept_clicked(self):
        result = self.db.session.query(self.db.Bibliotekarze).filter(self.db.Bibliotekarze.Login.like(f"{self.LibrarianName}")).one()
        if self.lineEditUserIdL.text() == "" or int(self.lineEditUserIdL.text()) > 3 or int(self.lineEditUserIdL.text()) < 0:
            self.errorsL.setText("Invalid card number!")
            self.errorsL.setStyleSheet("QLabel {color : red; }")
        else:
            self.db.DodawanieWypozyczenia(self.lineEditUserIdL.text(), 1, result.Id_bibliotekarza)
            self.errorsL.setText("Lendong is done!")
            self.errorsL.setStyleSheet("QLabel {color : black; }")
        



