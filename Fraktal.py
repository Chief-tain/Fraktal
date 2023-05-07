from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import sys

from sympy.solvers import nsolve
from sympy import Symbol
from sympy import log
k = Symbol('k')

import random

from styles import button_style, text_box_style, table_style

try:
    # Включите в блок try/except, если вы также нацелены на Mac/Linux
    from PyQt5.QtWinExtras import QtWin                                         #  !!!
    myappid = 'mycompany.myproduct.subproduct.version'                          #  !!!
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)                      #  !!!    
except ImportError:
    pass

class Calculations:
    def swertka_po_2(self, p1, p2):
        f2 = nsolve((k*p1*(log(p1*p2)-log(k*p2))+k*p2*(log(p1*p2)-log(k*p1))+log(p1*p2))-log(k**2), k, 0.01)
        return f2


    def swertka_po_3(self, p1, p2, p3):

        if p1 > 0 and p2 > 0 and p3 > 0:

            for i in range(5):

                P12=nsolve((k*p1*(log(p1*p2)-log(k*p2))+k*p2*(log(p1*p2)-log(k*p1))+log(p1*p2))-log(k**2), k, 0.01)
                P13=nsolve((k*p1*(log(p1*p3)-log(k*p3))+k*p3*(log(p1*p3)-log(k*p1))+log(p1*p3))-log(k**2), k, 0.01)
                P23=nsolve((k*p2*(log(p2*p3)-log(k*p3))+k*p3*(log(p2*p3)-log(k*p2))+log(p2*p3))-log(k**2), k, 0.01)
                p1=P12
                p2=P13
                p3=P23

            f3 = (p1+p2+p3) / 3
            
        if p1 == 0 and p2 != 0 and p3 != 0:
            f3 = self.swertka_po_2(p2,p3)

        if p2 == 0 and p1 != 0 and p3 != 0:
            f3 = self.swertka_po_2(p1,p3)

        if p3 == 0 and p1 != 0 and p2 != 0:
            f3 = self.swertka_po_2(p1,p2)

        # else:
        #     print('Все показатели нулевые!')

        return f3
    
    def logic(self, b1, b2, b3, b4, b5, b6, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12):
        k1_1 = self.swertka_po_3(b1,m1,m2)
        k1_2 = self.swertka_po_3(b2,m2,m1)
        self.s1 = self.swertka_po_2(k1_2,k1_1)

        k2_1 = self.swertka_po_3(b3,m3,m4)
        k2_2 = self.swertka_po_3(b2,m3,m4)
        self.s2 = self.swertka_po_2(k2_2,k2_1)

        k3_1 = self.swertka_po_3(b3,m5,m6)
        k3_2 = self.swertka_po_3(b4,m5,m6)
        self.s3 = self.swertka_po_2(k3_2,k3_1)

        k4_1 = self.swertka_po_3(b4,m7,m8)
        k4_2 = self.swertka_po_3(b5,m7,m8)
        self.s4 = self.swertka_po_2(k4_2,k4_1)

        k5_1 = self.swertka_po_3(b5,m9,m10)
        k5_2 = self.swertka_po_3(b6,m9,m10)
        self.s5 = self.swertka_po_2(k5_2,k5_1)

        k6_1 = self.swertka_po_3(b6,m11,m12)
        k6_2 = self.swertka_po_3(b1,m11,m12)
        self.s6 = self.swertka_po_2(k6_2,k6_1)

        s123 = self.swertka_po_3(self.s1, self.s2, self.s3)
        s456 = self.swertka_po_3(self.s4, self.s5, self.s6)

        self.ef = self.swertka_po_2(s123,s456)
        return self.ef

    def exploration(self, b1, b2, b3, b4, b5, b6, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, delta):
        EF=[]
        self.EF_2=[]
        default = self.logic(b1, b2, b3, b4, b5, b6, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12)
        mas_1_krug=[b1, m1, m2, b2, m3, m4, b3, m5, m6, b4, m7, m8, b5, m9, m10, b6, m11, m12]

        for j in range(18):
            
            mas_1_krug[j] += delta

            if mas_1_krug[j] > 1:
                mas_1_krug[j] = 1

            k1_1 = self.swertka_po_3(mas_1_krug[0], mas_1_krug[1], mas_1_krug[2])
            k1_2 = self.swertka_po_3(mas_1_krug[3], mas_1_krug[1], mas_1_krug[2])
            s1 = self.swertka_po_2(k1_2,k1_1)

            k2_1 = self.swertka_po_3(mas_1_krug[6], mas_1_krug[4], mas_1_krug[5])
            k2_2 = self.swertka_po_3(mas_1_krug[3], mas_1_krug[4], mas_1_krug[5])
            s2 = self.swertka_po_2(k2_2,k2_1)

            k3_1 = self.swertka_po_3(mas_1_krug[6], mas_1_krug[7], mas_1_krug[8])
            k3_2 = self.swertka_po_3(mas_1_krug[9], mas_1_krug[7], mas_1_krug[8])
            s3 = self.swertka_po_2(k3_2,k3_1)

            k4_1 = self.swertka_po_3(mas_1_krug[9], mas_1_krug[10], mas_1_krug[11])
            k4_2 = self.swertka_po_3(mas_1_krug[12], mas_1_krug[10], mas_1_krug[11])
            s4 = self.swertka_po_2(k4_2,k4_1)

            k5_1 = self.swertka_po_3(mas_1_krug[12], mas_1_krug[13], mas_1_krug[14])
            k5_2 = self.swertka_po_3(mas_1_krug[15], mas_1_krug[10], mas_1_krug[11])
            s5 = self.swertka_po_2(k5_2,k5_1)

            k6_1 = self.swertka_po_3(mas_1_krug[15], mas_1_krug[16], mas_1_krug[17])
            k6_2 = self.swertka_po_3(mas_1_krug[0], mas_1_krug[10], mas_1_krug[11])
            s6 = self.swertka_po_2(k6_2,k6_1)

            s123 = self.swertka_po_3(s1, s2, s3)
            s456 = self.swertka_po_3(s4, s5, s6)

            self.mas_ef = self.swertka_po_2(s123,s456)

            EF.append(self.mas_ef)
            self.EF_2.append(abs(1-(default/self.mas_ef))*10000)

            mas_1_krug[j] -= delta


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Оценивание эффективности фунционирования сложной технической системы")
        self.setFixedSize(1600, 900)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(fon.jpg)}")
        self.setWindowIcon(QIcon('14.jpg'))

        self.result = QLineEdit(self)
        self.result.move(480, 422)
        self.result.resize(100, 50)
        self.result.setFont(QFont('San Francisco', 14))
        self.result.setStyleSheet(text_box_style)
        self.result.setAlignment(Qt.AlignCenter)

        self.textbox_s2 = QLineEdit(self)
        self.textbox_s2.move(295, 430)
        self.textbox_s2.resize(70, 40)
        self.textbox_s2.setFont(QFont('San Francisco', 14))
        self.textbox_s2.setStyleSheet(text_box_style)
        self.textbox_s2.setAlignment(Qt.AlignCenter)

        self.textbox_s3 = QLineEdit(self)
        self.textbox_s3.move(382, 261)
        self.textbox_s3.resize(70, 40)
        self.textbox_s3.setFont(QFont('San Francisco', 14))
        self.textbox_s3.setStyleSheet(text_box_style)
        self.textbox_s3.setAlignment(Qt.AlignCenter)

        self.textbox_s4 = QLineEdit(self)
        self.textbox_s4.move(608, 260)
        self.textbox_s4.resize(70, 40)
        self.textbox_s4.setFont(QFont('San Francisco', 14))
        self.textbox_s4.setStyleSheet(text_box_style)
        self.textbox_s4.setAlignment(Qt.AlignCenter)

        self.textbox_s5 = QLineEdit(self)
        self.textbox_s5.move(695, 428)
        self.textbox_s5.resize(70, 40)
        self.textbox_s5.setFont(QFont('San Francisco', 14))
        self.textbox_s5.setStyleSheet(text_box_style)
        self.textbox_s5.setAlignment(Qt.AlignCenter)

        self.textbox_s6 = QLineEdit(self)
        self.textbox_s6.move(608, 592)
        self.textbox_s6.resize(70, 40)
        self.textbox_s6.setFont(QFont('San Francisco', 14))
        self.textbox_s6.setStyleSheet(text_box_style)
        self.textbox_s6.setAlignment(Qt.AlignCenter)

        self.textbox_s1 = QLineEdit(self)
        self.textbox_s1.move(381, 592)
        self.textbox_s1.resize(70, 40)
        self.textbox_s1.setFont(QFont('San Francisco', 14))
        self.textbox_s1.setStyleSheet(text_box_style)
        self.textbox_s1.setAlignment(Qt.AlignCenter)

        self.textbox_b1 = QLineEdit(self)
        self.textbox_b1.move(502, 760)
        self.textbox_b1.resize(55, 40)
        self.textbox_b1.setFont(QFont('San Francisco', 14))
        self.textbox_b1.setStyleSheet(text_box_style)
        self.textbox_b1.setAlignment(Qt.AlignCenter)

        self.textbox_b2 = QLineEdit(self)
        self.textbox_b2.move(211, 577)
        self.textbox_b2.resize(55, 40)
        self.textbox_b2.setFont(QFont('San Francisco', 14))
        self.textbox_b2.setStyleSheet(text_box_style)
        self.textbox_b2.setAlignment(Qt.AlignCenter)

        self.textbox_b3 = QLineEdit(self)
        self.textbox_b3.move(210, 270)
        self.textbox_b3.resize(55, 40)
        self.textbox_b3.setFont(QFont('San Francisco', 14))
        self.textbox_b3.setStyleSheet(text_box_style)
        self.textbox_b3.setAlignment(Qt.AlignCenter)

        self.textbox_b4 = QLineEdit(self)
        self.textbox_b4.move(502, 96)
        self.textbox_b4.resize(55, 40)
        self.textbox_b4.setFont(QFont('San Francisco', 14))
        self.textbox_b4.setStyleSheet(text_box_style)
        self.textbox_b4.setAlignment(Qt.AlignCenter)

        self.textbox_b5 = QLineEdit(self)
        self.textbox_b5.move(803, 267)
        self.textbox_b5.resize(55, 40)
        self.textbox_b5.setFont(QFont('San Francisco', 14))
        self.textbox_b5.setStyleSheet(text_box_style)
        self.textbox_b5.setAlignment(Qt.AlignCenter)

        self.textbox_b6 = QLineEdit(self)
        self.textbox_b6.move(803, 575)
        self.textbox_b6.resize(55, 40)
        self.textbox_b6.setFont(QFont('San Francisco', 14))
        self.textbox_b6.setStyleSheet(text_box_style)
        self.textbox_b6.setAlignment(Qt.AlignCenter)

        self.textbox_m4 = QLineEdit(self)
        self.textbox_m4.move(176, 376)
        self.textbox_m4.resize(55, 35)
        self.textbox_m4.setFont(QFont('San Francisco', 14))
        self.textbox_m4.setStyleSheet(text_box_style)
        self.textbox_m4.setAlignment(Qt.AlignCenter)

        self.textbox_m5 = QLineEdit(self)
        self.textbox_m5.move(288, 180)
        self.textbox_m5.resize(55, 35)
        self.textbox_m5.setFont(QFont('San Francisco', 14))
        self.textbox_m5.setStyleSheet(text_box_style)
        self.textbox_m5.setAlignment(Qt.AlignCenter)

        self.textbox_m6 = QLineEdit(self)
        self.textbox_m6.move(386, 122)
        self.textbox_m6.resize(55, 35)
        self.textbox_m6.setFont(QFont('San Francisco', 14))
        self.textbox_m6.setStyleSheet(text_box_style)
        self.textbox_m6.setAlignment(Qt.AlignCenter)

        self.textbox_m7 = QLineEdit(self)
        self.textbox_m7.move(626, 122)
        self.textbox_m7.resize(55, 35)
        self.textbox_m7.setFont(QFont('San Francisco', 14))
        self.textbox_m7.setStyleSheet(text_box_style)
        self.textbox_m7.setAlignment(Qt.AlignCenter)

        self.textbox_m8 = QLineEdit(self)
        self.textbox_m8.move(725, 190)
        self.textbox_m8.resize(55, 35)
        self.textbox_m8.setFont(QFont('San Francisco', 14))
        self.textbox_m8.setStyleSheet(text_box_style)
        self.textbox_m8.setAlignment(Qt.AlignCenter)

        self.textbox_m9 = QLineEdit(self)
        self.textbox_m9.move(828, 375)
        self.textbox_m9.resize(55, 35)
        self.textbox_m9.setFont(QFont('San Francisco', 14))
        self.textbox_m9.setStyleSheet(text_box_style)
        self.textbox_m9.setAlignment(Qt.AlignCenter)

        self.textbox_m10 = QLineEdit(self)
        self.textbox_m10.move(828, 478)
        self.textbox_m10.resize(55, 35)
        self.textbox_m10.setFont(QFont('San Francisco', 14))
        self.textbox_m10.setStyleSheet(text_box_style)
        self.textbox_m10.setAlignment(Qt.AlignCenter)

        self.textbox_m11 = QLineEdit(self)
        self.textbox_m11.move(725, 678)
        self.textbox_m11.resize(55, 35)
        self.textbox_m11.setFont(QFont('San Francisco', 14))
        self.textbox_m11.setStyleSheet(text_box_style)
        self.textbox_m11.setAlignment(Qt.AlignCenter)

        self.textbox_m12 = QLineEdit(self)
        self.textbox_m12.move(626, 747)
        self.textbox_m12.resize(55, 35)
        self.textbox_m12.setFont(QFont('San Francisco', 14))
        self.textbox_m12.setStyleSheet(text_box_style)
        self.textbox_m12.setAlignment(Qt.AlignCenter)

        self.textbox_m1 = QLineEdit(self)
        self.textbox_m1.move(386, 747)
        self.textbox_m1.resize(55, 35)
        self.textbox_m1.setFont(QFont('San Francisco', 14))
        self.textbox_m1.setStyleSheet(text_box_style)
        self.textbox_m1.setAlignment(Qt.AlignCenter)

        self.textbox_m2 = QLineEdit(self)
        self.textbox_m2.move(272, 680)
        self.textbox_m2.resize(55, 35)
        self.textbox_m2.setFont(QFont('San Francisco', 14))
        self.textbox_m2.setStyleSheet(text_box_style)
        self.textbox_m2.setAlignment(Qt.AlignCenter)

        self.textbox_m3 = QLineEdit(self)
        self.textbox_m3.move(169, 481)
        self.textbox_m3.resize(55, 35)
        self.textbox_m3.setFont(QFont('San Francisco', 14))
        self.textbox_m3.setStyleSheet(text_box_style)
        self.textbox_m3.setAlignment(Qt.AlignCenter)   

        self.bt00 = QPushButton("Очистить поля", self)
        self.bt00.move(1110, 280)
        self.bt00.setFont(QFont('San Francisco', 16))
        self.bt00.setFixedSize(400, 50)
        self.bt00.setObjectName("pushButton")
        self.bt00.setStyleSheet(button_style)
        self.bt00.clicked.connect(self.Button00)
        
        self.bt0 = QPushButton("Вставить случайные значения", self)
        self.bt0.move(1110, 340)
        self.bt0.setFont(QFont('San Francisco', 16))
        self.bt0.setFixedSize(400, 50)
        self.bt0.setObjectName("pushButton")
        self.bt0.setStyleSheet(button_style)
        self.bt0.clicked.connect(self.Button0) 

        self.bt1 = QPushButton("Рассчитать", self)
        self.bt1.move(1110, 400)
        self.bt1.setFont(QFont('San Francisco', 16))
        self.bt1.setFixedSize(400, 50)
        self.bt1.setObjectName("pushButton")
        self.bt1.setStyleSheet(button_style)
        self.bt1.clicked.connect(self.Button1)   

        self.bt2 = QPushButton("Исследовать", self)
        self.bt2.move(1110, 460)
        self.bt2.setFont(QFont('San Francisco', 16))
        self.bt2.setFixedSize(400, 50)
        self.bt2.setObjectName("pushButton")
        self.bt2.setStyleSheet(button_style)
        self.bt2.clicked.connect(self.Button2)

        self.textboxes = [self.textbox_b1, self.textbox_b2, self.textbox_b3, self.textbox_b4, self.textbox_b5, self.textbox_b6,
                          self.textbox_m1, self.textbox_m2, self.textbox_m3, self.textbox_m4, self.textbox_m5, self.textbox_m6,
                          self.textbox_m7, self.textbox_m8, self.textbox_m9, self.textbox_m10, self.textbox_m11, self.textbox_m12,
                          self.textbox_s1, self.textbox_s2, self.textbox_s3, self.textbox_s4, self.textbox_s5, self.textbox_s6,
                          self.result]

        self.show()
    
    def show_info_messagebox_critical(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Ошибка ввода данных")
        msg.setText("Некорректно введены значения")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def Button00(self):

        for textbox in self.textboxes:
            textbox.clear()

    def Button0(self):

        for index in range(18):
            if not self.textboxes[index].text():
                self.textboxes[index].setText(str(random.uniform(0.1, 1))[:4])

    def Button1(self):
        try:
            self.b1 = float(self.textbox_b1.text())
            self.b2 = float(self.textbox_b2.text())
            self.b3 = float(self.textbox_b3.text())
            self.b4 = float(self.textbox_b4.text())
            self.b5 = float(self.textbox_b5.text())
            self.b6 = float(self.textbox_b6.text())

            self.m1 = float(self.textbox_m1.text())
            self.m2 = float(self.textbox_m2.text())
            self.m3 = float(self.textbox_m3.text())
            self.m4 = float(self.textbox_m4.text())
            self.m5 = float(self.textbox_m5.text())
            self.m6 = float(self.textbox_m6.text())
            self.m7 = float(self.textbox_m7.text())
            self.m8 = float(self.textbox_m8.text())
            self.m9 = float(self.textbox_m9.text())
            self.m10 = float(self.textbox_m10.text())
            self.m11 = float(self.textbox_m11.text())
            self.m12 = float(self.textbox_m12.text())

            self.calculations = Calculations()
            self.calculations.logic(self.b1, self.b2, self.b3, self.b4, self.b5,
                                    self.b6, self.m1, self.m2, self.m3, self.m4,
                                    self.m5, self.m6, self.m7, self.m8, self.m9,
                                    self.m10, self.m11, self.m12)

            self.textbox_s1.setText(str(self.calculations.s1)[:5])
            self.textbox_s2.setText(str(self.calculations.s2)[:5])
            self.textbox_s3.setText(str(self.calculations.s3)[:5])
            self.textbox_s4.setText(str(self.calculations.s4)[:5])
            self.textbox_s5.setText(str(self.calculations.s5)[:5])
            self.textbox_s6.setText(str(self.calculations.s6)[:5])

            self.result.setText(str(self.calculations.ef)[:7])

            with open('data.txt', 'w') as file:
                file.writelines(f'{self.b1} {self.b2} {self.b3} {self.b4} {self.b5} {self.b6} {self.m1} {self.m2} {self.m3} {self.m4} {self.m5} {self.m6} {self.m7} {self.m8} {self.m9} {self.m10} {self.m11} {self.m12}')
        
                # print(f'{self.b1} {self.b2} {self.b3} {self.b4} {self.b5} {self.b6} {self.m1} {self.m2} {self.m3} {self.m4} {self.m5} {self.m6} {self.m7} {self.m8} {self.m9} {self.m10} {self.m11} {self.m12}')
        
        except Exception:
            self.show_info_messagebox_critical()

    def Button2(self):
        self.w = AnotherWindow()
        self.w.show()


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setWindowTitle("Режим исследования")
        self.setFixedSize(1600, 850)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: rgb(8, 5, 26)')

        self.label11 = QLabel('<b style="color: white;">Параметр delta: </b>', self)
        self.label11.setGeometry(400, 30, 300, 50)
        self.label11.setFont(QFont('San Francisco', 16))
        self.label11.setAlignment(Qt.AlignCenter)

        self.textbox11 = QLineEdit(self)
        self.textbox11.move(700, 30)
        self.textbox11.resize(100, 50)
        self.textbox11.setFont(QFont('San Francisco', 14))
        self.textbox11.setStyleSheet(text_box_style)
        self.textbox11.setAlignment(Qt.AlignCenter)

        self.bt11 = QPushButton("Исследовать показатели эффективности", self)
        self.bt11.move(830, 30)
        self.bt11.setFont(QFont('San Francisco', 16))
        self.bt11.setFixedSize(400, 50)
        self.bt11.setObjectName("pushButton")
        self.bt11.setStyleSheet(button_style)
        self.bt11.clicked.connect(self.Button11)

        self.table = QTableWidget(self)  # Create a table
        self.table.setColumnCount(4)     #Set three columns
        self.table.setRowCount(18)        # and one row
 
        # Set the table headers
        self.table.setHorizontalHeaderLabels(["Название параметра", "Значние \n параметра", "Коэффициент", "Ранг"])

        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        strs = self.table.verticalHeader()
        strs.setSectionResizeMode(0, QHeaderView.Stretch)
 
        # Set the alignment to the headers
        for i in range(4):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
 
        # Do the resize of the columns by content
        self.table.resizeColumnsToContents()
        self.table.setGeometry(40, 100, 490, 720)
        self.table.setStyleSheet(table_style)

        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.plot(list(range(1, 19)), list(range(1, 19)))
        self.graphWidget.setGeometry(550, 100, 1000, 720)
        self.graphWidget.setBackground('w')
        # self.graphWidget.setTitle(f'Изменение показателя эффективности фунционирования сложной технической системы', color="b", size="10pt")
        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Показатель эффективности', **styles)
        self.graphWidget.setLabel('bottom', 'Параметр', **styles)
        self.graphWidget.showGrid(x=True, y=True, alpha=1)

    def show_info_messagebox_critical_mini(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Ошибка ввода данных")
        msg.setText("Некорректно введены значения")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def Button11(self):

        try:
            delta = float(self.textbox11.text())

            with open('data.txt', 'r') as file:
                data = file.read().split()

            data = [float(param) for param in data]

            # print(data)
            
            b1, b2, b3, b4, b5, b6, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12 = data
            data_for_table = [b1, m1, m2, b2, m3, m4, b3, m5, m6, b4, m7, m8, b5, m9, m10, b6, m11, m12]

            calculations = Calculations()
            calculations.exploration(b1, b2, b3, b4, b5, b6, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, delta)
            
            # print(calculations.EF_2)
            x_data = [int(el) for el in calculations.EF_2]
            rang = sorted(x_data, reverse=True)

            self.graphWidget.clear()
            self.graphWidget.plot(range(1, len(x_data)+1), x_data, pen=pg.mkPen(color=(255, 255, 255), width=15, style=Qt.DashLine),  symbol='o', symbolSize=30, symbolBrush=('b'))
            # self.graphWidget.setTitle(f'Изменение показателя эффективности фунционирования сложной технической системы при delta={delta}', color="b", size="10pt")

            params = ['Долговечность', 'Модифицируемость', 'Модернизируемость', 'Сохраняемость', 
                    'Обеспеченность', 'Возможность', 'Оперативность', 'Монотонность', 'Обратимость', 
                    'Успешность', 'Рискованность', 'Безотказность', 'Диагностируемость', 'Достижимость',
                    'Скоординированность', 'Результативность', 'Устойчивость структур', 'Устойчивость процессов']

            for i in range(len(x_data)):
                new_value = 1 if (data_for_table[i] + delta) > 1 else (data_for_table[i] + delta)

                self.table.setItem(i, 0, QTableWidgetItem(f"{params[i]}"))
                self.table.setItem(i, 1, QTableWidgetItem(f"{round(new_value, 3)}"))
                self.table.setItem(i, 2, QTableWidgetItem(f"{x_data[i]}"))
                self.table.setItem(i, 3, QTableWidgetItem(f"{rang.index(x_data[i])+1}"))

                if rang.index(x_data[i])+1 == 18:
                    for j in range(self.table.columnCount()):
                        self.table.item(i, j).setBackground(QBrush(QColor(242, 172, 65)))

                if rang.index(x_data[i])+1 == 1:
                    for j in range(self.table.columnCount()):
                        self.table.item(i, j).setBackground(QBrush(QColor(92, 242, 117)))
        
        except Exception as error:
            self.show_info_messagebox_critical_mini()
            print(error)

            
if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setWindowIcon(QIcon('14.jpg'))
    window = Window()
    sys.exit(App.exec())