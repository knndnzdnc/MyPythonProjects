import sys
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon  # app iconu değiştirmek için
from PyQt5 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('First APP')  # title
        self.setGeometry(200, 200, 500, 500)  # (Soldan pixel, üstten pixel, Yatay, dikey)
        self.setWindowIcon(QIcon('icon.png'))  # app iconu değiştirdik
        self.setToolTip("My Tooltip")  # App üstüne gelince bu text yazar
        self.initUI()
        self.radio_value()
        self.btn_save.clicked.connect(self.radio_value)

    def initUI(self):  # Program içi tüm itemler
        self.lbl_kilo = QtWidgets.QLabel( self)  # QLabel = yazı
        self.lbl_kilo.setText("Kilonuz :")
        self.lbl_kilo.move(50, 30)  # soldan 50px, üstten 30px

        self.lbl_boy = QtWidgets.QLabel(self)  # QLabel = yazı
        self.lbl_boy.setText("Boyunuz: ")
        self.lbl_boy.move(50, 70)

        self.lbl_cinsiyet = QtWidgets.QLabel(self)  # QLabel = yazı
        self.lbl_cinsiyet.setText("Cinsiyetiniz: ")
        self.lbl_cinsiyet.move(50, 112)

        self.lbl_result1 = QtWidgets.QLabel(self)
        self.lbl_result1.resize(300, 50)
        self.lbl_result1.move(100, 210)

        self.lbl_result2 = QtWidgets.QLabel(self)
        self.lbl_result2.resize(300, 50)
        self.lbl_result2.move(100, 230)

        self.lbl_result3 = QtWidgets.QLabel(self)
        self.lbl_result3.resize(300, 50)
        self.lbl_result3.move(100, 260)

        self.lbl_result4 = QtWidgets.QLabel(self)
        self.lbl_result4.resize(300, 50)
        self.lbl_result4.move(100, 280)

        self.txt_kilo = QtWidgets.QLineEdit(self)  # QLineEdit = textbox
        self.txt_kilo.move(120, 30)  # soldan 120px, üstten 30px
        self.txt_kilo.resize(200, 32)  # boyutu

        self.txt_boy = QtWidgets.QLineEdit(self)  # QLineEdit = textbox
        self.txt_boy.move(120, 70)
        self.txt_boy.resize(200, 32)

        self.erkek = QtWidgets.QRadioButton(self)  # Radio butonlar
        self.erkek.setGeometry(120, 110, 120, 40)
        self.erkek.setText("Erkek")

        self.kadin = QtWidgets.QRadioButton(self)
        self.kadin.setGeometry(180, 110, 120, 40)
        self.kadin.setText("Kadın")

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Hesapla")
        self.btn_save.move(120, 150)
        self.btn_save.resize(200, 32)
        self.btn_save.clicked.connect(self.clicked)  # clicked fonk oluşturduk

    def radio_value(self):
        if self.erkek.isChecked():
            self.erkekHesapla()
        elif self.kadin.isChecked():
            self.kadinHesapla()
        else:
            self.lbl_result1.setText("Cinsiyet seçilmedi")

    def clicked(self):  # window içindeki txt_name, txt_surname elemanlarına erişmek için buraya aldık
        pass

    def erkekHesapla(self):

        self.erkek_ideal_kilo = float(50 + (2.3 * ((int(self.txt_boy.text()) * 0.39370) - 60)))

        self.lbl_result1.setText(f'İdeal Kilonuz: {str(round(self.erkek_ideal_kilo))} KG')

        self.evucut_kitle_indeksi = float(int(self.txt_kilo.text()) / (int(self.txt_boy.text()) / 100) ** 2)
        self.lbl_result2.setText(f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}')

        def calculatetovki():
            if (self.evucut_kitle_indeksi > 0 and self.evucut_kitle_indeksi <= 15):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Oldukça Ciddi derecede zayıf')
            elif (self.evucut_kitle_indeksi > 15 and self.evucut_kitle_indeksi <= 16):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Ciddi Derecede Zayıf')
            elif (self.evucut_kitle_indeksi > 16 and self.evucut_kitle_indeksi <= 18.5):
                self.lbl_result2.setText(f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Zayıf')
            elif (self.evucut_kitle_indeksi > 18.5 and self.evucut_kitle_indeksi <= 25):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Normal (Sağlıklı kilo)')
            elif (self.evucut_kitle_indeksi > 25 and self.evucut_kitle_indeksi <= 30):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Kilolu')
            elif (self.evucut_kitle_indeksi > 30 and self.evucut_kitle_indeksi <= 35):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Birinci Dereceden Obez')
            elif (self.evucut_kitle_indeksi > 35 and self.evucut_kitle_indeksi <= 40):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' İkinci Dereceden Obez')
            elif (self.evucut_kitle_indeksi > 40 and self.evucut_kitle_indeksi < 100):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Üçüncü Dereceden Obez')
            else:
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + 'Öngörülmeyen değer')

        calculatetovki()

        self.eyagsiz_vücut_agirligi = float(round(1.10 * int(self.txt_kilo.text())) - round(
            128 * ((int(self.txt_kilo.text()) ** 2) / ((100 * (int(self.txt_boy.text()) / 10000)) ** 2) / 10000)))
        self.lbl_result3.setText('Yağsız Vücut Ağırlığınız ' + str(round(self.eyagsiz_vücut_agirligi)) + ' KG')

        self.evucut_yuzey_alani = 0.20247 * ((int(self.txt_boy.text()) * 0.010000) ** 0.725) * (
                    int(self.txt_kilo.text()) ** 0.425)
        self.lbl_result4.setText(f'Vücut Yüzey Alanınız ' + str(round(self.evucut_yuzey_alani, 2)) + ' Metre Kare')

    def kadinHesapla(self):
        self.kadin_ideal_kilo = float(45.5 + (2.3 * ((int(self.txt_boy.text()) * 0.39370) - 60)))
        self.lbl_result1.setText(f'İdeal Kilonuz {str(round(self.kadin_ideal_kilo))} KG')

        self.evucut_kitle_indeksi = float(int(self.txt_kilo.text()) / (int(self.txt_boy.text()) / 100) ** 2)
        self.lbl_result2.setText(f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}')

        def calculatetovki2():
            if (self.evucut_kitle_indeksi > 0 and self.evucut_kitle_indeksi <= 15):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Oldukça Ciddi derecede zayıf')
            elif (self.evucut_kitle_indeksi > 15 and self.evucut_kitle_indeksi <= 16):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Ciddi Derecede Zayıf')
            elif (self.evucut_kitle_indeksi > 16 and self.evucut_kitle_indeksi <= 18.5):
                self.lbl_result2.setText(f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Zayıf')
            elif (self.evucut_kitle_indeksi > 18.5 and self.evucut_kitle_indeksi <= 25):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Normal (Sağlıklı kilo)')
            elif (self.evucut_kitle_indeksi > 25 and self.evucut_kitle_indeksi <= 30):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Kilolu')
            elif (self.evucut_kitle_indeksi > 30 and self.evucut_kitle_indeksi <= 35):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Birinci Dereceden Obez')
            elif (self.evucut_kitle_indeksi > 35 and self.evucut_kitle_indeksi <= 40):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' İkinci Dereceden Obez')
            elif (self.evucut_kitle_indeksi > 40 and self.evucut_kitle_indeksi < 100):
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + ' Üçüncü Dereceden Obez')
            else:
                self.lbl_result2.setText(
                    f'\nVücut Kitle Indexiniz: {str(round(self.evucut_kitle_indeksi))}' + 'Öngörülmeyen değer')

        calculatetovki2()

        self.kyagsiz_vücut_agirligi = float(round(1.10 * int(self.txt_kilo.text())) - round(
            148 * ((int(self.txt_kilo.text()) ** 2) / ((100 * (int(self.txt_boy.text()) / 10000)) ** 2) / 10000)))
        self.lbl_result3.setText('Yağsız Vücut Ağırlığınız ' + str(round(self.kyagsiz_vücut_agirligi)) + ' KG')

        self.kvucut_yuzey_alani = 0.20247 * ((int(self.txt_boy.text()) * 0.010000) ** 0.725) * (
                    int(self.txt_kilo.text()) ** 0.425)
        self.lbl_result4.setText(f'Vücut Yüzey Alanınız ' + str(round(self.kvucut_yuzey_alani, 2)) + ' Metre Kare')


def window():
    app = QApplication(sys.argv)
    win = MyWindow()  # Class'tan nesne üretiyoruz ve bu nesneye de beliri özellik atıyoruz..
    win.show()
    sys.exit(app.exec_())  # X butonuna tıklayınca çıkış


window()