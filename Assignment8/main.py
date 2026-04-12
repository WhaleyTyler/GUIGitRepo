import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from asn8_ui import Ui_root


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_root()
        self.ui.setupUi(self)

        self.ui.btnS.clicked.connect(self.displayData)
        self.ui.btnR.clicked.connect(self.Clear)
        self.ui.btnQ.clicked.connect(self.close)

    def displayData(self):
        # Use the .text() method on the line edit objects
        first = self.ui.entFirst.text()
        last = self.ui.entLast.text()
        email = self.ui.entEmail.text()
        phone = self.ui.entPhone.text()

        output = (
            f"Welcome to PySide6, {first} \n"
            "You entered:\n"
            f"Name: {first} {last}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
        )

        QMessageBox.information(self, "PySide6 Welcome Message", output)

    def Clear(self):
        """Deletes all characters in the entry boxes."""
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()


app = QApplication(sys.argv)
root = MainWindow()
root.show()
sys.exit(app.exec())