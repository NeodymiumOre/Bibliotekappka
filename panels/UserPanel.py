from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
sys.path.insert(0, './tabs')
from tabs.SearchTab import *
from enums import User

class UserPanel(QWidget):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.db = self.MainWindow.db
        self.userType = User.Reader

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # creating searching widget
        searchWidget = SearchTab(self.MainWindow, self.userType)
        layout = QVBoxLayout()
        layout.addWidget(searchWidget)
        self.setLayout(layout)

    def UiWizard(self):
        pass


