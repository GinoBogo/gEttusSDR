# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowIFuqIg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtSvg import QSvgWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QSize(800, 700))
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.pushButton_Open = QPushButton(self.central_widget)
        self.pushButton_Open.setObjectName(u"pushButton_Open")
        self.pushButton_Open.setMinimumSize(QSize(80, 32))
        self.pushButton_Open.setMaximumSize(QSize(80, 32))
        self.pushButton_Open.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_1.addWidget(self.pushButton_Open)

        self.pushButton_Save = QPushButton(self.central_widget)
        self.pushButton_Save.setObjectName(u"pushButton_Save")
        self.pushButton_Save.setMinimumSize(QSize(80, 32))
        self.pushButton_Save.setMaximumSize(QSize(80, 32))
        self.pushButton_Save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_1.addWidget(self.pushButton_Save)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer)

        self.pushButton_Run = QPushButton(self.central_widget)
        self.pushButton_Run.setObjectName(u"pushButton_Run")
        self.pushButton_Run.setMinimumSize(QSize(80, 32))
        self.pushButton_Run.setMaximumSize(QSize(80, 32))
        self.pushButton_Run.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_1.addWidget(self.pushButton_Run)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.line = QFrame(self.central_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_COM = QGroupBox(self.central_widget)
        self.groupBox_COM.setObjectName(u"groupBox_COM")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_COM.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_COM)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_clock_source = QLabel(self.groupBox_COM)
        self.label_clock_source.setObjectName(u"label_clock_source")
        self.label_clock_source.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_clock_source.setFont(font1)
        self.label_clock_source.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_clock_source, 2, 0, 1, 1)

        self.label_enable_tx = QLabel(self.groupBox_COM)
        self.label_enable_tx.setObjectName(u"label_enable_tx")
        self.label_enable_tx.setMinimumSize(QSize(0, 28))
        self.label_enable_tx.setFont(font1)
        self.label_enable_tx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_enable_tx, 3, 0, 1, 1)

        self.lineEdit_folder_tx = QLineEdit(self.groupBox_COM)
        self.lineEdit_folder_tx.setObjectName(u"lineEdit_folder_tx")
        self.lineEdit_folder_tx.setMinimumSize(QSize(0, 28))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.lineEdit_folder_tx.setFont(font2)
        self.lineEdit_folder_tx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_folder_tx, 5, 1, 1, 1)

        self.comboBox_enable_tx = QComboBox(self.groupBox_COM)
        self.comboBox_enable_tx.addItem("")
        self.comboBox_enable_tx.addItem("")
        self.comboBox_enable_tx.setObjectName(u"comboBox_enable_tx")
        self.comboBox_enable_tx.setMinimumSize(QSize(0, 28))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.comboBox_enable_tx.setPalette(palette)
        self.comboBox_enable_tx.setFont(font1)

        self.gridLayout.addWidget(self.comboBox_enable_tx, 3, 1, 1, 1)

        self.pushButton_folder_tx = QPushButton(self.groupBox_COM)
        self.pushButton_folder_tx.setObjectName(u"pushButton_folder_tx")
        self.pushButton_folder_tx.setMinimumSize(QSize(28, 28))
        self.pushButton_folder_tx.setMaximumSize(QSize(28, 28))
        self.pushButton_folder_tx.setFont(font2)
        self.pushButton_folder_tx.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_folder_tx, 5, 2, 1, 1)

        self.label_enable_rx = QLabel(self.groupBox_COM)
        self.label_enable_rx.setObjectName(u"label_enable_rx")
        self.label_enable_rx.setMinimumSize(QSize(0, 28))
        self.label_enable_rx.setFont(font1)
        self.label_enable_rx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_enable_rx, 4, 0, 1, 1)

        self.lineEdit_folder_rx = QLineEdit(self.groupBox_COM)
        self.lineEdit_folder_rx.setObjectName(u"lineEdit_folder_rx")
        self.lineEdit_folder_rx.setMinimumSize(QSize(0, 28))
        self.lineEdit_folder_rx.setFont(font2)
        self.lineEdit_folder_rx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit_folder_rx, 7, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.pushButton_folder_rx = QPushButton(self.groupBox_COM)
        self.pushButton_folder_rx.setObjectName(u"pushButton_folder_rx")
        self.pushButton_folder_rx.setMinimumSize(QSize(28, 28))
        self.pushButton_folder_rx.setMaximumSize(QSize(28, 28))
        self.pushButton_folder_rx.setFont(font2)
        self.pushButton_folder_rx.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_folder_rx, 7, 2, 1, 1)

        self.lineEdit_serial_number = QLineEdit(self.groupBox_COM)
        self.lineEdit_serial_number.setObjectName(u"lineEdit_serial_number")
        self.lineEdit_serial_number.setMinimumSize(QSize(0, 28))
        self.lineEdit_serial_number.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_serial_number, 0, 1, 1, 1)

        self.comboBox_enable_rx = QComboBox(self.groupBox_COM)
        self.comboBox_enable_rx.addItem("")
        self.comboBox_enable_rx.addItem("")
        self.comboBox_enable_rx.setObjectName(u"comboBox_enable_rx")
        self.comboBox_enable_rx.setMinimumSize(QSize(0, 28))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.comboBox_enable_rx.setPalette(palette1)
        self.comboBox_enable_rx.setFont(font1)

        self.gridLayout.addWidget(self.comboBox_enable_rx, 4, 1, 1, 1)

        self.lineEdit_fp_chunks_number = QLineEdit(self.groupBox_COM)
        self.lineEdit_fp_chunks_number.setObjectName(u"lineEdit_fp_chunks_number")
        self.lineEdit_fp_chunks_number.setMinimumSize(QSize(0, 28))
        self.lineEdit_fp_chunks_number.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_fp_chunks_number, 1, 1, 1, 1)

        self.label_folder_tx = QLabel(self.groupBox_COM)
        self.label_folder_tx.setObjectName(u"label_folder_tx")
        self.label_folder_tx.setMinimumSize(QSize(0, 28))
        self.label_folder_tx.setFont(font1)
        self.label_folder_tx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_folder_tx, 5, 0, 1, 1)

        self.label_folder_rx = QLabel(self.groupBox_COM)
        self.label_folder_rx.setObjectName(u"label_folder_rx")
        self.label_folder_rx.setMinimumSize(QSize(0, 28))
        self.label_folder_rx.setFont(font1)
        self.label_folder_rx.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_folder_rx, 7, 0, 1, 1)

        self.label_serial_number = QLabel(self.groupBox_COM)
        self.label_serial_number.setObjectName(u"label_serial_number")
        self.label_serial_number.setMinimumSize(QSize(0, 28))
        self.label_serial_number.setFont(font1)
        self.label_serial_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_serial_number, 0, 0, 1, 1)

        self.comboBox_clock_source = QComboBox(self.groupBox_COM)
        self.comboBox_clock_source.addItem("")
        self.comboBox_clock_source.addItem("")
        self.comboBox_clock_source.setObjectName(u"comboBox_clock_source")
        self.comboBox_clock_source.setMinimumSize(QSize(0, 28))
        self.comboBox_clock_source.setFont(font1)

        self.gridLayout.addWidget(self.comboBox_clock_source, 2, 1, 1, 1)

        self.label_fp_chunks_number = QLabel(self.groupBox_COM)
        self.label_fp_chunks_number.setObjectName(u"label_fp_chunks_number")
        self.label_fp_chunks_number.setMinimumSize(QSize(0, 28))
        self.label_fp_chunks_number.setFont(font1)
        self.label_fp_chunks_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_fp_chunks_number, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_COM)

        self.widget = QSvgWidget(self.central_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(200, 200))

        self.horizontalLayout_2.addWidget(self.widget)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_TX = QGroupBox(self.central_widget)
        self.groupBox_TX.setObjectName(u"groupBox_TX")
        palette2 = QPalette()
        brush2 = QBrush(QColor(170, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.groupBox_TX.setPalette(palette2)
        self.groupBox_TX.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_TX)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_TX = QGridLayout()
        self.gridLayout_TX.setSpacing(8)
        self.gridLayout_TX.setObjectName(u"gridLayout_TX")
        self.label_tx_sample_rate = QLabel(self.groupBox_TX)
        self.label_tx_sample_rate.setObjectName(u"label_tx_sample_rate")
        self.label_tx_sample_rate.setMinimumSize(QSize(160, 28))
        self.label_tx_sample_rate.setFont(font1)
        self.label_tx_sample_rate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_TX.addWidget(self.label_tx_sample_rate, 4, 0, 1, 1)

        self.label_tx_enable_sin_generator = QLabel(self.groupBox_TX)
        self.label_tx_enable_sin_generator.setObjectName(u"label_tx_enable_sin_generator")
        self.label_tx_enable_sin_generator.setMinimumSize(QSize(160, 28))
        self.label_tx_enable_sin_generator.setFont(font1)
        self.label_tx_enable_sin_generator.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_TX.addWidget(self.label_tx_enable_sin_generator, 11, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_TX)
        self.label_2.setObjectName(u"label_2")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_2.setPalette(palette3)
        self.label_2.setFont(font2)

        self.gridLayout_TX.addWidget(self.label_2, 6, 3, 1, 1)

        self.label_tx_bandwidth = QLabel(self.groupBox_TX)
        self.label_tx_bandwidth.setObjectName(u"label_tx_bandwidth")
        self.label_tx_bandwidth.setMinimumSize(QSize(160, 28))
        self.label_tx_bandwidth.setFont(font1)
        self.label_tx_bandwidth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_TX.addWidget(self.label_tx_bandwidth, 9, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_TX)
        self.label_9.setObjectName(u"label_9")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_9.setPalette(palette4)
        self.label_9.setFont(font2)

        self.gridLayout_TX.addWidget(self.label_9, 12, 3, 1, 1)

        self.label_tx_frames_number = QLabel(self.groupBox_TX)
        self.label_tx_frames_number.setObjectName(u"label_tx_frames_number")
        self.label_tx_frames_number.setMinimumSize(QSize(160, 28))
        self.label_tx_frames_number.setFont(font1)
        self.label_tx_frames_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_TX.addWidget(self.label_tx_frames_number, 14, 0, 1, 1)

        self.label_1 = QLabel(self.groupBox_TX)
        self.label_1.setObjectName(u"label_1")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_1.setPalette(palette5)
        self.label_1.setFont(font2)

        self.gridLayout_TX.addWidget(self.label_1, 4, 3, 1, 1)

        self.lineEdit_tx_frames_number = QLineEdit(self.groupBox_TX)
        self.lineEdit_tx_frames_number.setObjectName(u"lineEdit_tx_frames_number")
        self.lineEdit_tx_frames_number.setMinimumSize(QSize(0, 28))
        self.lineEdit_tx_frames_number.setFont(font1)
        self.lineEdit_tx_frames_number.setAlignment(Qt.AlignCenter)

        self.gridLayout_TX.addWidget(self.lineEdit_tx_frames_number, 14, 2, 1, 1)

        self.lineEdit_tx_bandwidth = QLineEdit(self.groupBox_TX)
        self.lineEdit_tx_bandwidth.setObjectName(u"lineEdit_tx_bandwidth")
        self.lineEdit_tx_bandwidth.setMinimumSize(QSize(0, 28))
        self.lineEdit_tx_bandwidth.setFont(font1)
        self.lineEdit_tx_bandwidth.setAlignment(Qt.AlignCenter)

        self.gridLayout_TX.addWidget(self.lineEdit_tx_bandwidth, 9, 2, 1, 1)

        self.comboBox_tx_enable_sin_generator = QComboBox(self.groupBox_TX)
        self.comboBox_tx_enable_sin_generator.addItem("")
        self.comboBox_tx_enable_sin_generator.addItem("")
        self.comboBox_tx_enable_sin_generator.setObjectName(u"comboBox_tx_enable_sin_generator")
        self.comboBox_tx_enable_sin_generator.setMinimumSize(QSize(0, 28))
        self.comboBox_tx_enable_sin_generator.setFont(font1)

        self.gridLayout_TX.addWidget(self.comboBox_tx_enable_sin_generator, 11, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_TX)
        self.label_3.setObjectName(u"label_3")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_3.setPalette(palette6)
        self.label_3.setFont(font2)

        self.gridLayout_TX.addWidget(self.label_3, 9, 3, 1, 1)

        self.label_tx_gain = QLabel(self.groupBox_TX)
        self.label_tx_gain.setObjectName(u"label_tx_gain")
        self.label_tx_gain.setMinimumSize(QSize(160, 28))
        self.label_tx_gain.setFont(font1)
        self.label_tx_gain.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_TX.addWidget(self.label_tx_gain, 10, 0, 1, 1)

        self.lineEdit_tx_gain = QLineEdit(self.groupBox_TX)
        self.lineEdit_tx_gain.setObjectName(u"lineEdit_tx_gain")
        self.lineEdit_tx_gain.setMinimumSize(QSize(0, 28))
        self.lineEdit_tx_gain.setFont(font1)
        self.lineEdit_tx_gain.setAlignment(Qt.AlignCenter)

        self.gridLayout_TX.addWidget(self.lineEdit_tx_gain, 10, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_TX)
        self.label_4.setObjectName(u"label_4")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_4.setPalette(palette7)
        self.label_4.setFont(font2)

        self.gridLayout_TX.addWidget(self.label_4, 10, 3, 1, 1)

        self.label_tx_center_frequency = QLabel(self.groupBox_TX)
        self.label_tx_center_frequency.setObjectName(u"label_tx_center_frequency")
        self.label_tx_center_frequency.setMinimumSize(QSize(160, 28))
        self.label_tx_center_frequency.setFont(font1)
        self.label_tx_center_frequency.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_TX.addWidget(self.label_tx_center_frequency, 6, 0, 1, 1)

        self.lineEdit_tx_sin_frequency = QLineEdit(self.groupBox_TX)
        self.lineEdit_tx_sin_frequency.setObjectName(u"lineEdit_tx_sin_frequency")
        self.lineEdit_tx_sin_frequency.setMinimumSize(QSize(0, 28))
        self.lineEdit_tx_sin_frequency.setFont(font1)
        self.lineEdit_tx_sin_frequency.setAlignment(Qt.AlignCenter)

        self.gridLayout_TX.addWidget(self.lineEdit_tx_sin_frequency, 12, 2, 1, 1)

        self.lineEdit_tx_center_frequency = QLineEdit(self.groupBox_TX)
        self.lineEdit_tx_center_frequency.setObjectName(u"lineEdit_tx_center_frequency")
        self.lineEdit_tx_center_frequency.setMinimumSize(QSize(0, 28))
        self.lineEdit_tx_center_frequency.setFont(font1)
        self.lineEdit_tx_center_frequency.setAlignment(Qt.AlignCenter)

        self.gridLayout_TX.addWidget(self.lineEdit_tx_center_frequency, 6, 2, 1, 1)

        self.lineEdit_tx_sample_rate = QLineEdit(self.groupBox_TX)
        self.lineEdit_tx_sample_rate.setObjectName(u"lineEdit_tx_sample_rate")
        self.lineEdit_tx_sample_rate.setMinimumSize(QSize(0, 28))
        self.lineEdit_tx_sample_rate.setFont(font1)
        self.lineEdit_tx_sample_rate.setAlignment(Qt.AlignCenter)

        self.gridLayout_TX.addWidget(self.lineEdit_tx_sample_rate, 4, 2, 1, 1)

        self.label_tx_sin_frequency = QLabel(self.groupBox_TX)
        self.label_tx_sin_frequency.setObjectName(u"label_tx_sin_frequency")
        self.label_tx_sin_frequency.setMinimumSize(QSize(160, 28))
        self.label_tx_sin_frequency.setFont(font1)
        self.label_tx_sin_frequency.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_TX.addWidget(self.label_tx_sin_frequency, 12, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_TX)


        self.horizontalLayout_3.addWidget(self.groupBox_TX)

        self.groupBox_RX = QGroupBox(self.central_widget)
        self.groupBox_RX.setObjectName(u"groupBox_RX")
        palette8 = QPalette()
        brush3 = QBrush(QColor(0, 85, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.groupBox_RX.setPalette(palette8)
        self.groupBox_RX.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_RX)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_RX = QGridLayout()
        self.gridLayout_RX.setSpacing(8)
        self.gridLayout_RX.setObjectName(u"gridLayout_RX")
        self.lineEdit_rx_sample_rate = QLineEdit(self.groupBox_RX)
        self.lineEdit_rx_sample_rate.setObjectName(u"lineEdit_rx_sample_rate")
        self.lineEdit_rx_sample_rate.setMinimumSize(QSize(0, 28))
        self.lineEdit_rx_sample_rate.setFont(font1)
        self.lineEdit_rx_sample_rate.setAlignment(Qt.AlignCenter)

        self.gridLayout_RX.addWidget(self.lineEdit_rx_sample_rate, 2, 2, 1, 1)

        self.label_rx_enable_AGC = QLabel(self.groupBox_RX)
        self.label_rx_enable_AGC.setObjectName(u"label_rx_enable_AGC")
        self.label_rx_enable_AGC.setMinimumSize(QSize(160, 28))
        self.label_rx_enable_AGC.setFont(font1)
        self.label_rx_enable_AGC.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_RX.addWidget(self.label_rx_enable_AGC, 9, 0, 1, 1)

        self.lineEdit_rx_bandwidth = QLineEdit(self.groupBox_RX)
        self.lineEdit_rx_bandwidth.setObjectName(u"lineEdit_rx_bandwidth")
        self.lineEdit_rx_bandwidth.setMinimumSize(QSize(0, 28))
        self.lineEdit_rx_bandwidth.setFont(font1)
        self.lineEdit_rx_bandwidth.setAlignment(Qt.AlignCenter)

        self.gridLayout_RX.addWidget(self.lineEdit_rx_bandwidth, 7, 2, 1, 1)

        self.label_rx_sample_rate = QLabel(self.groupBox_RX)
        self.label_rx_sample_rate.setObjectName(u"label_rx_sample_rate")
        self.label_rx_sample_rate.setMinimumSize(QSize(160, 28))
        self.label_rx_sample_rate.setFont(font1)
        self.label_rx_sample_rate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_RX.addWidget(self.label_rx_sample_rate, 2, 0, 1, 1)

        self.lineEdit_rx_center_frequency = QLineEdit(self.groupBox_RX)
        self.lineEdit_rx_center_frequency.setObjectName(u"lineEdit_rx_center_frequency")
        self.lineEdit_rx_center_frequency.setMinimumSize(QSize(0, 28))
        self.lineEdit_rx_center_frequency.setFont(font1)
        self.lineEdit_rx_center_frequency.setAlignment(Qt.AlignCenter)

        self.gridLayout_RX.addWidget(self.lineEdit_rx_center_frequency, 4, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_RX)
        self.label_8.setObjectName(u"label_8")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_8.setPalette(palette9)
        self.label_8.setFont(font2)

        self.gridLayout_RX.addWidget(self.label_8, 8, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_RX)
        self.label_6.setObjectName(u"label_6")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_6.setPalette(palette10)
        self.label_6.setFont(font2)

        self.gridLayout_RX.addWidget(self.label_6, 4, 3, 1, 1)

        self.label_rx_bandwidth = QLabel(self.groupBox_RX)
        self.label_rx_bandwidth.setObjectName(u"label_rx_bandwidth")
        self.label_rx_bandwidth.setMinimumSize(QSize(160, 28))
        self.label_rx_bandwidth.setFont(font1)
        self.label_rx_bandwidth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_RX.addWidget(self.label_rx_bandwidth, 7, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_RX)
        self.label_5.setObjectName(u"label_5")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_5.setPalette(palette11)
        self.label_5.setFont(font2)

        self.gridLayout_RX.addWidget(self.label_5, 2, 3, 1, 1)

        self.label_rx_frames_number = QLabel(self.groupBox_RX)
        self.label_rx_frames_number.setObjectName(u"label_rx_frames_number")
        self.label_rx_frames_number.setMinimumSize(QSize(160, 28))
        self.label_rx_frames_number.setFont(font1)
        self.label_rx_frames_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_RX.addWidget(self.label_rx_frames_number, 11, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_RX)
        self.label_7.setObjectName(u"label_7")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_7.setPalette(palette12)
        self.label_7.setFont(font2)

        self.gridLayout_RX.addWidget(self.label_7, 7, 3, 1, 1)

        self.label_rx_center_frequency = QLabel(self.groupBox_RX)
        self.label_rx_center_frequency.setObjectName(u"label_rx_center_frequency")
        self.label_rx_center_frequency.setMinimumSize(QSize(160, 28))
        self.label_rx_center_frequency.setFont(font1)
        self.label_rx_center_frequency.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_RX.addWidget(self.label_rx_center_frequency, 4, 0, 1, 1)

        self.label_rx_gain = QLabel(self.groupBox_RX)
        self.label_rx_gain.setObjectName(u"label_rx_gain")
        self.label_rx_gain.setMinimumSize(QSize(160, 28))
        self.label_rx_gain.setFont(font1)
        self.label_rx_gain.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_RX.addWidget(self.label_rx_gain, 8, 0, 1, 1)

        self.lineEdit_rx_gain = QLineEdit(self.groupBox_RX)
        self.lineEdit_rx_gain.setObjectName(u"lineEdit_rx_gain")
        self.lineEdit_rx_gain.setMinimumSize(QSize(0, 28))
        self.lineEdit_rx_gain.setFont(font1)
        self.lineEdit_rx_gain.setAlignment(Qt.AlignCenter)

        self.gridLayout_RX.addWidget(self.lineEdit_rx_gain, 8, 2, 1, 1)

        self.lineEdit_rx_frames_number = QLineEdit(self.groupBox_RX)
        self.lineEdit_rx_frames_number.setObjectName(u"lineEdit_rx_frames_number")
        self.lineEdit_rx_frames_number.setMinimumSize(QSize(0, 28))
        self.lineEdit_rx_frames_number.setFont(font1)
        self.lineEdit_rx_frames_number.setAlignment(Qt.AlignCenter)

        self.gridLayout_RX.addWidget(self.lineEdit_rx_frames_number, 11, 2, 1, 1)

        self.comboBox_rx_enable_AGC = QComboBox(self.groupBox_RX)
        self.comboBox_rx_enable_AGC.addItem("")
        self.comboBox_rx_enable_AGC.addItem("")
        self.comboBox_rx_enable_AGC.setObjectName(u"comboBox_rx_enable_AGC")
        self.comboBox_rx_enable_AGC.setMinimumSize(QSize(0, 28))
        self.comboBox_rx_enable_AGC.setFont(font1)

        self.gridLayout_RX.addWidget(self.comboBox_rx_enable_AGC, 9, 2, 1, 1)

        self.label_rx_spacer = QLabel(self.groupBox_RX)
        self.label_rx_spacer.setObjectName(u"label_rx_spacer")
        self.label_rx_spacer.setMinimumSize(QSize(160, 28))
        self.label_rx_spacer.setFont(font1)
        self.label_rx_spacer.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_RX.addWidget(self.label_rx_spacer, 10, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_RX)


        self.horizontalLayout_3.addWidget(self.groupBox_RX)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.central_widget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        QWidget.setTabOrder(self.pushButton_Open, self.pushButton_Save)
        QWidget.setTabOrder(self.pushButton_Save, self.pushButton_Run)
        QWidget.setTabOrder(self.pushButton_Run, self.lineEdit_serial_number)
        QWidget.setTabOrder(self.lineEdit_serial_number, self.comboBox_clock_source)
        QWidget.setTabOrder(self.comboBox_clock_source, self.comboBox_enable_tx)
        QWidget.setTabOrder(self.comboBox_enable_tx, self.comboBox_enable_rx)
        QWidget.setTabOrder(self.comboBox_enable_rx, self.lineEdit_folder_tx)
        QWidget.setTabOrder(self.lineEdit_folder_tx, self.pushButton_folder_tx)
        QWidget.setTabOrder(self.pushButton_folder_tx, self.lineEdit_folder_rx)
        QWidget.setTabOrder(self.lineEdit_folder_rx, self.pushButton_folder_rx)
        QWidget.setTabOrder(self.pushButton_folder_rx, self.lineEdit_tx_sample_rate)
        QWidget.setTabOrder(self.lineEdit_tx_sample_rate, self.lineEdit_tx_center_frequency)
        QWidget.setTabOrder(self.lineEdit_tx_center_frequency, self.lineEdit_tx_bandwidth)
        QWidget.setTabOrder(self.lineEdit_tx_bandwidth, self.lineEdit_tx_gain)
        QWidget.setTabOrder(self.lineEdit_tx_gain, self.comboBox_tx_enable_sin_generator)
        QWidget.setTabOrder(self.comboBox_tx_enable_sin_generator, self.lineEdit_tx_sin_frequency)
        QWidget.setTabOrder(self.lineEdit_tx_sin_frequency, self.lineEdit_tx_frames_number)
        QWidget.setTabOrder(self.lineEdit_tx_frames_number, self.lineEdit_rx_sample_rate)
        QWidget.setTabOrder(self.lineEdit_rx_sample_rate, self.lineEdit_rx_center_frequency)
        QWidget.setTabOrder(self.lineEdit_rx_center_frequency, self.lineEdit_rx_bandwidth)
        QWidget.setTabOrder(self.lineEdit_rx_bandwidth, self.lineEdit_rx_gain)
        QWidget.setTabOrder(self.lineEdit_rx_gain, self.comboBox_rx_enable_AGC)
        QWidget.setTabOrder(self.comboBox_rx_enable_AGC, self.lineEdit_rx_frames_number)

        self.retranslateUi(MainWindow)
        self.pushButton_Open.clicked.connect(MainWindow.slot_button_open_clicked)
        self.pushButton_Save.clicked.connect(MainWindow.slot_button_save_clicked)
        self.pushButton_Run.clicked.connect(MainWindow.slot_button_run_clicked)
        self.comboBox_enable_tx.currentIndexChanged.connect(MainWindow.slot_enable_tx_changed)
        self.comboBox_enable_rx.currentIndexChanged.connect(MainWindow.slot_enable_rx_changed)
        self.comboBox_clock_source.currentIndexChanged.connect(MainWindow.slot_clock_source_changed)
        self.comboBox_rx_enable_AGC.currentIndexChanged.connect(MainWindow.slot_rx_enable_agc_changed)
        self.comboBox_tx_enable_sin_generator.currentIndexChanged.connect(MainWindow.slot_tx_enable_sin_generator_changed)
        self.pushButton_folder_tx.clicked.connect(MainWindow.slot_button_folder_tx_clicked)
        self.pushButton_folder_rx.clicked.connect(MainWindow.slot_button_folder_rx_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GEttusSDR - CFG File Tool", None))
        self.pushButton_Open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_Run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.groupBox_COM.setTitle(QCoreApplication.translate("MainWindow", u"Common", None))
        self.label_clock_source.setText(QCoreApplication.translate("MainWindow", u"clock source", None))
        self.label_enable_tx.setText(QCoreApplication.translate("MainWindow", u"enable TX", None))
        self.lineEdit_folder_tx.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.comboBox_enable_tx.setItemText(0, QCoreApplication.translate("MainWindow", u"false", None))
        self.comboBox_enable_tx.setItemText(1, QCoreApplication.translate("MainWindow", u"true", None))

        self.pushButton_folder_tx.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_enable_rx.setText(QCoreApplication.translate("MainWindow", u"enable RX", None))
        self.lineEdit_folder_rx.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_folder_rx.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_serial_number.setText(QCoreApplication.translate("MainWindow", u"any", None))
        self.comboBox_enable_rx.setItemText(0, QCoreApplication.translate("MainWindow", u"false", None))
        self.comboBox_enable_rx.setItemText(1, QCoreApplication.translate("MainWindow", u"true", None))

        self.lineEdit_fp_chunks_number.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_folder_tx.setText(QCoreApplication.translate("MainWindow", u"TX folder", None))
        self.label_folder_rx.setText(QCoreApplication.translate("MainWindow", u"RX folder", None))
        self.label_serial_number.setText(QCoreApplication.translate("MainWindow", u"serial number", None))
        self.comboBox_clock_source.setItemText(0, QCoreApplication.translate("MainWindow", u"internal", None))
        self.comboBox_clock_source.setItemText(1, QCoreApplication.translate("MainWindow", u"external", None))

        self.label_fp_chunks_number.setText(QCoreApplication.translate("MainWindow", u"chunks number", None))
        self.groupBox_TX.setTitle(QCoreApplication.translate("MainWindow", u"Transmitter", None))
        self.label_tx_sample_rate.setText(QCoreApplication.translate("MainWindow", u"sample rate", None))
        self.label_tx_enable_sin_generator.setText(QCoreApplication.translate("MainWindow", u"enable sin generator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_tx_bandwidth.setText(QCoreApplication.translate("MainWindow", u"bandwidth", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_tx_frames_number.setText(QCoreApplication.translate("MainWindow", u"frames number", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Msps", None))
        self.lineEdit_tx_frames_number.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_tx_bandwidth.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.comboBox_tx_enable_sin_generator.setItemText(0, QCoreApplication.translate("MainWindow", u"false", None))
        self.comboBox_tx_enable_sin_generator.setItemText(1, QCoreApplication.translate("MainWindow", u"true", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_tx_gain.setText(QCoreApplication.translate("MainWindow", u"gain", None))
        self.lineEdit_tx_gain.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"dB", None))
        self.label_tx_center_frequency.setText(QCoreApplication.translate("MainWindow", u"center frequency", None))
        self.lineEdit_tx_sin_frequency.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_tx_center_frequency.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_tx_sample_rate.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_tx_sin_frequency.setText(QCoreApplication.translate("MainWindow", u"sin frequency", None))
        self.groupBox_RX.setTitle(QCoreApplication.translate("MainWindow", u"Receiver", None))
        self.lineEdit_rx_sample_rate.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_rx_enable_AGC.setText(QCoreApplication.translate("MainWindow", u"enable AGC", None))
        self.lineEdit_rx_bandwidth.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_rx_sample_rate.setText(QCoreApplication.translate("MainWindow", u"sample rate", None))
        self.lineEdit_rx_center_frequency.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"dB", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_rx_bandwidth.setText(QCoreApplication.translate("MainWindow", u"bandwidth", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Msps", None))
        self.label_rx_frames_number.setText(QCoreApplication.translate("MainWindow", u"frames number", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_rx_center_frequency.setText(QCoreApplication.translate("MainWindow", u"center frequency", None))
        self.label_rx_gain.setText(QCoreApplication.translate("MainWindow", u"gain", None))
        self.lineEdit_rx_gain.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_rx_frames_number.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.comboBox_rx_enable_AGC.setItemText(0, QCoreApplication.translate("MainWindow", u"false", None))
        self.comboBox_rx_enable_AGC.setItemText(1, QCoreApplication.translate("MainWindow", u"true", None))

        self.label_rx_spacer.setText("")
    # retranslateUi

