from PySide6.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow
from PySide6.QtCore import Qt
import sys

from pathlib import Path
import datetime
from docxtpl import DocxTemplate


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(
            Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.pushButton.clicked.connect(self.report_generetor)
        self.pushButton_2.clicked.connect(self.close)

    def report_generetor(self):
        document_path = Path(__file__).parent / "report" / "template.docx"
        doc = DocxTemplate(document_path)

        name = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        date_time = datetime.datetime.today()
        today = date_time.strftime("%Y_%m_%d")

        context = {
            "NAME": name,
            "LAST_NAME": last_name,
            "EMAIL": email,
            "PASSWORD": password,
            "DATE_TIME": date_time.strftime("%Y-%m-%d")
        }

        doc.render(context)
        doc.save(Path(__file__).parent / f"contract_{today}.docx")


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    # widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
