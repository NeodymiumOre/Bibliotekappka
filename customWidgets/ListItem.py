from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from enums import User

class ListItem(QWidget):
    def __init__(self, ItemName, item, userType, parent=None):
        self.ItemName = ItemName
        self.item = item
        self.userType = userType
        super(ListItem, self).__init__(parent)

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # creating basic elements
        self.labelName = QLabel(self.ItemName)
        self.buttonReserve = QPushButton("Rezerwuj")
        self.buttonReserve.setCheckable(True)
        self.buttonReserve.clicked.connect(self.on_buttonReserve_clicked)
        self.buttonLend = QPushButton("Wypożycz")
        self.buttonLend.setCheckable(True)
        self.buttonLend.clicked.connect(self.on_buttonLend_clicked)
        if self.userType == User.Reader:
            self.buttonLend.setHidden(True)

        # creating items for reserving enrollment
        self.lineEditUserIdR = QLineEdit()
        self.buttonReserveAccept = QPushButton("Zatwierdź rezerwację")

        # creating items for lending enrollment
        self.lineEditUserIdL = QLineEdit()
        self.buttonLendAccept = QPushButton("Zatwierdź wypożyczenie")

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

        # creating basic widget
        self.basic = QWidget()
        self.layoutListItem = QHBoxLayout()
        self.layoutListItem.addWidget(self.labelName)
        self.layoutListItem.addWidget(self.buttonLend)
        self.layoutListItem.addWidget(self.buttonReserve)
        self.basic.setLayout(self.layoutListItem)

        # creating final layout
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
        



