from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 529, 341))
        self.widget.setObjectName("widget")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 4, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)
        
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 5, 1, 1, 1)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 4, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)
        
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 5)
        
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.clearFields)
        self.pushButton.clicked.connect(self.openNewWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "KELAS:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "06.00"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "10.00"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "15.00"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "18.00"))
        self.label_5.setText(_translate("MainWindow", "TUJUAN:"))
        self.label.setText(_translate("MainWindow", "PEMESANAN TIKET KERETA STASIUN BALAPAN"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Semarang"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Jakarta"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Surabaya"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Madiun"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "NAMA:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VIP"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bisnis"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ekonomi"))
        self.label_4.setText(_translate("MainWindow", "PUKUL:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAMA"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "KELAS"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PUKUL"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TUJUAN"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "HARGA"))

    def clearFields(self):
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

    def openNewWindow(self):
        name = self.lineEdit.text()
        kelas = self.comboBox.currentText()
        waktu = self.comboBox_2.currentText()
        tujuan = self.comboBox_3.currentText()
        harga = self.calculatePrice(kelas)

        # Insert data into table
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(name))
        self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(kelas))
        self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(waktu))
        self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(tujuan))
        self.tableWidget.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(str(harga)))

    def calculatePrice(self, kelas):
        prices = {"VIP": 500000, "Bisnis": 350000, "Ekonomi": 80000}
        return prices.get(kelas, 80000)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
