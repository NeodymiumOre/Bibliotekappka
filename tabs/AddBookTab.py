from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class AddBookTab(QWidget):
    def __init__(self):
        super().__init__()

        # creating layout
        self.UiSetup()
        # setting up layout design
        self.UiWizard()

    def UiSetup(self):
        # xdxd
        button = QPushButton("Dodaj książkę")

        # creating main layout
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def UiWizard(self):
        pass
