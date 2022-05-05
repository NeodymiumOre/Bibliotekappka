from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from palette import *

class LoginPanel(QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # creating layout elements
        self.buttonLogin = QPushButton("Zaloguj")
        self.buttonLogin.clicked.connect(self.on_buttonLogin_clicked)

        self.buttonShow = QPushButton("Pokaż")
        self.buttonShow.setCheckable(True)
        self.buttonShow.clicked.connect(self.on_buttonShow_clicked)

        self.labelName = QLabel("Login")
        self.lineEditUsername = QLineEdit()

        self.labelPasswd = QLabel("Hasło")
        self.lineEditPasswd = QLineEdit()
        self.lineEditPasswd.setEchoMode(QLineEdit.EchoMode.Password)

        # creating layout with labels
        widgetName = QWidget()
        layoutName = QHBoxLayout()
        layoutName.addWidget(self.labelName)
        layoutName.addWidget(self.lineEditUsername)
        widgetName.setLayout(layoutName)

        widgetPasswd = QWidget()
        layoutPasswd = QHBoxLayout()
        layoutPasswd.addWidget(self.labelPasswd)
        layoutPasswd.addWidget(self.lineEditPasswd)
        layoutPasswd.addWidget(self.buttonShow)
        widgetPasswd.setLayout(layoutPasswd)

        # creating layout in groupBoxLogin
        groupBoxLogin = QGroupBox("Login")
        groupLayout = QVBoxLayout()
        groupLayout.addWidget(widgetName)
        groupLayout.addWidget(widgetPasswd)
        groupLayout.addWidget(self.buttonLogin)
        groupBoxLogin.setLayout(groupLayout)
        groupBoxLogin.setMaximumHeight(300)
        groupBoxLogin.setMaximumWidth(300)
        #sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        #sizePolicy.setHeightForWidth(True)
        #groupBoxLogin.setSizePolicy(sizePolicy)
        # groupBoxLogin.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding, QSizePolicy.setHeightForWidth(True))

        # creating final layout
        # layout = QVBoxLayout()
        # layout.addWidget(groupBoxLogin)
        # self.setLayout(layout)
        vSpacerUp = QSpacerItem(20, 40, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        vSpacerBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        hSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        hSpacerRight = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layoutLoginBox = QGridLayout()
        layoutLoginBox.addWidget(groupBoxLogin, 1, 1)
        layoutLoginBox.addItem(vSpacerUp, 0, 1)
        layoutLoginBox.addItem(vSpacerBottom, 2, 1)
        layoutLoginBox.addItem(hSpacerLeft, 1, 0)
        layoutLoginBox.addItem(hSpacerRight, 1, 2)
        self.setLayout(layoutLoginBox)

    def UiWizard(self):
        self.buttonLogin.setStyleSheet("background-color: {}".format(Pallete.buttonColor))

    def on_buttonLogin_clicked(self):
        print(self.lineEditUsername.displayText())
        print(self.lineEditPasswd.displayText())
        self.MainWindow.Stack.setCurrentIndex(self.MainWindow.LibrarianPIndex)
        self.setWindowFlag(Qt.WindowType.WindowTitleHint)

    def on_buttonShow_clicked(self):
        if self.buttonShow.isChecked():
            self.lineEditPasswd.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEditPasswd.setEchoMode(QLineEdit.EchoMode.Password)
