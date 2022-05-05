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

        self.buttonShow = QPushButton("Pokaz")
        self.buttonShow.setCheckable(True)
        self.buttonShow.clicked.connect(self.on_buttonShow_clicked)

        self.labelName = QLabel("Login")
        self.lineEditUsername = QLineEdit()

        self.labelPasswd = QLabel("Haslo")
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

        # creating final layout
        layout = QVBoxLayout()
        layout.addWidget(groupBoxLogin)
        self.setLayout(layout)

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

