import sqlite3, sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUi()

    def initUi(self):
        self.pbn.clicked.connect(self.show_info)

    def show_info(self):
        con = sqlite3.connect("coffe.sqlite")
        cur = con.cursor()
        title = ""
        if self.rad.isChecked():
            title = "Название"
        elif self.rad2.isChecked():
            title = "Степень"
        elif self.rad3.isChecked():
            title = "Молотый"
        elif self.rad4.isChecked():
            title = "Описание"
        elif self.rad5.isChecked():
            title = "Цена"
        elif self.rad6.isChecked():
            title = "Объём"

        text = self.text1.toPlainText()
        text = text.split("\n")[0]
        text = text.lower().capitalize()
        zap = f"SELECT * FROM coffe WHERE {title} = '{text}'"
        con.commit()
        res = cur.execute(zap).fetchall()
        self.table.setRowCount(len(res))
        for i in range(len(res)):
            for j in range(7):
                self.table.setItem(i, j, QTableWidgetItem(str(res[i][j])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())