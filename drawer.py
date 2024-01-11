import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_file import Ui_MainWindow
from PyQt5 import QtCore


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        data = self.cur.execute(f'''SELECT * from info''').fetchall()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ('Номер', "Название", "Прожарка", "Тип", "Описание", "Цена", "Объем (мл)")
        )
        row = 0
        for a, b, c, d, e, f, g in data:
            col = 0
            for item in (str(a), str(b), str(c), str(d), str(e), str(f), str(g)):
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())