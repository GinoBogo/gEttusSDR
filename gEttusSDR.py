"""
__version__ = "1.0"
__date__    = "February, 2021"
__author__  = "Gino Francesco Bogo"
"""
import os
import subprocess
import sys

from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QImage
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow

from ui.ui_MainWindow import Ui_MainWindow

_path = os.path.dirname(os.path.abspath(__file__))


def real_path(filename):
    return os.path.join(_path, filename)


class ShellThread(QThread):  # pylint:disable=too-few-public-methods
    on_exit = Signal(object)

    def __init__(self, task):
        QThread.__init__(self)
        self.m_task = task

    def run(self):
        proc = subprocess.Popen(self.m_task, shell=True)
        proc.wait()
        self.on_exit.emit(None)


def cfg_reader(lines):
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if len(line) > 0]
    items = {}
    title = ""
    for line in lines:
        if line.startswith("[") and line.endswith("]"):
            title = line.strip("[]")
        else:
            item = str.format("{}.{}", title, line).split("=")
            item = [x.strip() for x in item]
            if len(item) == 2:
                items[item[0]] = item[1]
    return items


def cfg_writer(cfg):
    items = [[K, V] for K, V in cfg.items()]
    lines = []
    title = ""
    first = True
    for item in items:
        K, V = item
        pos = K.rfind(".")
        if pos > 0:
            L = K[:pos]
            R = K[pos + 1:]
            if title != L:
                title = L
                if first:
                    first = False
                    lines.append(str.format("[{}]\n", title))
                else:
                    lines.append(str.format("\n[{}]\n", title))
            lines.append(str.format("{} = {}\n", R, V))
    return lines


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.m_icons = {}
        self.m_icons["01000"] = real_path("icons/tx0_rx1_ext0_agc0_sin0.svg")
        self.m_icons["01001"] = real_path("icons/tx0_rx1_ext0_agc0_sin1.svg")
        self.m_icons["01010"] = real_path("icons/tx0_rx1_ext0_agc1_sin0.svg")
        self.m_icons["01011"] = real_path("icons/tx0_rx1_ext0_agc1_sin1.svg")
        self.m_icons["01100"] = real_path("icons/tx0_rx1_ext1_agc0_sin0.svg")
        self.m_icons["01101"] = real_path("icons/tx0_rx1_ext1_agc0_sin1.svg")
        self.m_icons["01110"] = real_path("icons/tx0_rx1_ext1_agc1_sin0.svg")
        self.m_icons["01111"] = real_path("icons/tx0_rx1_ext1_agc1_sin1.svg")
        self.m_icons["10000"] = real_path("icons/tx1_rx0_ext0_agc0_sin0.svg")
        self.m_icons["10001"] = real_path("icons/tx1_rx0_ext0_agc0_sin1.svg")
        self.m_icons["10010"] = real_path("icons/tx1_rx0_ext0_agc1_sin0.svg")
        self.m_icons["10011"] = real_path("icons/tx1_rx0_ext0_agc1_sin1.svg")
        self.m_icons["10100"] = real_path("icons/tx1_rx0_ext1_agc0_sin0.svg")
        self.m_icons["10101"] = real_path("icons/tx1_rx0_ext1_agc0_sin1.svg")
        self.m_icons["10110"] = real_path("icons/tx1_rx0_ext1_agc1_sin0.svg")
        self.m_icons["10111"] = real_path("icons/tx1_rx0_ext1_agc1_sin1.svg")
        self.m_icons["11000"] = real_path("icons/tx1_rx1_ext0_agc0_sin0.svg")
        self.m_icons["11001"] = real_path("icons/tx1_rx1_ext0_agc0_sin1.svg")
        self.m_icons["11010"] = real_path("icons/tx1_rx1_ext0_agc1_sin0.svg")
        self.m_icons["11011"] = real_path("icons/tx1_rx1_ext0_agc1_sin1.svg")
        self.m_icons["11100"] = real_path("icons/tx1_rx1_ext1_agc0_sin0.svg")
        self.m_icons["11101"] = real_path("icons/tx1_rx1_ext1_agc0_sin1.svg")
        self.m_icons["11110"] = real_path("icons/tx1_rx1_ext1_agc1_sin0.svg")
        self.m_icons["11111"] = real_path("icons/tx1_rx1_ext1_agc1_sin1.svg")

        icon = QImage(real_path(self.m_icons["01000"]))
        self.m_ratio = icon.width() / icon.height()

        self.m_cfg = {}
        self.m_thread = ShellThread(real_path("gEttusSDR"))
        self.m_thread.on_exit.connect(self.on_exit)
        self.open_config(real_path("gEttusSDR.cfg"))
        self.slot_enable_tx_changed()
        self.slot_enable_rx_changed()

    def add_missing_cfg(self):  # pylint:disable=too-many-branches
        # [board.common]
        if not "board.common.serial_number" in self.m_cfg:
            self.m_cfg["board.common.serial_number"] = 'any'
        if not "board.common.fp_chunks_number" in self.m_cfg:
            self.m_cfg["board.common.fp_chunks_number"] = '200'
        if not "board.common.clock_source" in self.m_cfg:
            self.m_cfg["board.common.clock_source"] = 'internal'
        if not "board.common.enable_tx" in self.m_cfg:
            self.m_cfg["board.common.enable_tx"] = 'false'
        if not "board.common.enable_rx" in self.m_cfg:
            self.m_cfg["board.common.enable_rx"] = 'true'
        if not "board.common.folder_tx" in self.m_cfg:
            self.m_cfg["board.common.folder_tx"] = '.'
        if not "board.common.folder_rx" in self.m_cfg:
            self.m_cfg["board.common.folder_rx"] = '.'
        # [board.tx]
        if not "board.tx.sample_rate" in self.m_cfg:
            self.m_cfg["board.tx.sample_rate"] = '3.2e6'
        if not "board.tx.center_frequency" in self.m_cfg:
            self.m_cfg["board.tx.center_frequency"] = '400.0e6'
        if not "board.tx.bandwidth" in self.m_cfg:
            self.m_cfg["board.tx.bandwidth"] = '4.8e6'
        if not "board.tx.gain" in self.m_cfg:
            self.m_cfg["board.tx.gain"] = '30.0'
       # [board.rx]
        if not "board.rx.sample_rate" in self.m_cfg:
            self.m_cfg["board.rx.sample_rate"] = '3.2e6'
        if not "board.rx.center_frequency" in self.m_cfg:
            self.m_cfg["board.rx.center_frequency"] = '400.0e6'
        if not "board.rx.bandwidth" in self.m_cfg:
            self.m_cfg["board.rx.bandwidth"] = '4.8e6'
        if not "board.rx.gain" in self.m_cfg:
            self.m_cfg["board.rx.gain"] = '30.0'
        if not "board.rx.enable_agc" in self.m_cfg:
            self.m_cfg["board.rx.enable_agc"] = 'false'
        # [text]
        if not "test.enable_sin_generator" in self.m_cfg:
            self.m_cfg["test.enable_sin_generator"] = 'false'
        if not "test.sin_frequency" in self.m_cfg:
            self.m_cfg["test.sin_frequency"] = '1.0e6'
        if not "test.tx_frames_number" in self.m_cfg:
            self.m_cfg["test.tx_frames_number"] = '50'
        if not "test.rx_frames_number" in self.m_cfg:
            self.m_cfg["test.rx_frames_number"] = '40'

    def update_size(self):
        h = self.ui.groupBox_COM.height()
        w = h * self.m_ratio
        self.ui.widget.setMinimumSize(w, h)
        self.ui.widget.setMaximumSize(w, h)

    def showEvent(self, event):
        QMainWindow.showEvent(self, event)
        self.update_size()

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.update_size()

    def open_config(self, filename):
        if os.path.isfile(filename):
            stream = open(filename, "r", encoding="utf-8")
            lines = stream.readlines()
            stream.close()
            self.m_cfg = cfg_reader(lines)
        else:
            filename = '[default config values loaded]'
        self.add_missing_cfg()
        self.config_to_fields()
        self.ui.status_bar.showMessage(filename)

    def save_config(self, filename):
        stream = open(filename, "w", encoding="utf-8")
        self.fields_to_config()
        lines = cfg_writer(self.m_cfg)
        stream.writelines(lines)
        stream.close()
        self.ui.status_bar.showMessage(filename)

    def slot_button_open_clicked(self):
        dialog = QFileDialog(self)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setWindowTitle("Open CFG File")
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter(self.tr("Config Files (*.cfg)"))
        if dialog.exec_():
            filename = dialog.selectedFiles()[0]
            self.open_config(filename)

    def slot_button_save_clicked(self):
        dialog = QFileDialog(self)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setWindowTitle("Save CFG File")
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter(self.tr("Config Files (*.cfg)"))
        if dialog.exec_():
            filename, _ = os.path.splitext(dialog.selectedFiles()[0])
            filename += ".cfg"
            self.save_config(filename)

    def slot_button_run_clicked(self):
        filename = real_path("gEttusSDR.cfg")
        stream = open(filename, "w", encoding="utf-8")
        self.fields_to_config()
        lines = cfg_writer(self.m_cfg)
        stream.writelines(lines)
        stream.close()
        self.m_thread.start()
        self.ui.pushButton_Run.setText("Running")
        self.ui.pushButton_Run.setEnabled(False)

    def slot_button_folder_tx_clicked(self):
        dialog = QFileDialog(self)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setWindowTitle("Select TX Samples Folder")
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            value = dialog.selectedFiles()[0]
            self.m_cfg["board.common.folder_tx"] = value
            self.config_to_fields()

    def slot_button_folder_rx_clicked(self):
        dialog = QFileDialog(self)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.setWindowTitle("Select RX Samples Folder")
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            value = dialog.selectedFiles()[0]
            self.m_cfg["board.common.folder_rx"] = value
            self.config_to_fields()

    def update_diagram(self):
        def append_bit(value):
            if value:
                return "1"
            return "0"

        key = ""
        key += append_bit(self.ui.comboBox_enable_tx.currentText() == "true")
        key += append_bit(self.ui.comboBox_enable_rx.currentText() == "true")
        key += append_bit(self.ui.comboBox_clock_source.currentText() == "external")
        key += append_bit(self.ui.comboBox_rx_enable_AGC.currentText() == "true")
        key += append_bit(self.ui.comboBox_tx_enable_sin_generator.currentText() == "true")
        if key in self.m_icons:
            icon = self.m_icons[key]
            self.ui.widget.load(icon)

    def slot_clock_source_changed(self):
        self.update_diagram()

    def slot_enable_tx_changed(self):
        tx_enabled = self.ui.comboBox_enable_tx.currentText() == "true"
        rx_enabled = self.ui.comboBox_enable_rx.currentText() == "true"
        self.ui.groupBox_TX.setEnabled(tx_enabled)
        self.ui.lineEdit_folder_tx.setEnabled(tx_enabled)
        self.ui.pushButton_folder_tx.setEnabled(tx_enabled)
        if not tx_enabled and not rx_enabled:
            self.ui.groupBox_RX.setEnabled(True)
            self.ui.lineEdit_folder_rx.setEnabled(True)
            self.ui.pushButton_folder_rx.setEnabled(True)
            self.ui.comboBox_enable_rx.setCurrentText("true")
        self.update_diagram()

    def slot_enable_rx_changed(self):
        tx_enabled = self.ui.comboBox_enable_tx.currentText() == "true"
        rx_enabled = self.ui.comboBox_enable_rx.currentText() == "true"
        self.ui.groupBox_RX.setEnabled(rx_enabled)
        self.ui.lineEdit_folder_rx.setEnabled(rx_enabled)
        self.ui.pushButton_folder_rx.setEnabled(rx_enabled)
        if not rx_enabled and not tx_enabled:
            self.ui.groupBox_TX.setEnabled(True)
            self.ui.lineEdit_folder_tx.setEnabled(True)
            self.ui.pushButton_folder_tx.setEnabled(True)
            self.ui.comboBox_enable_tx.setCurrentText("true")
        self.update_diagram()

    def slot_rx_enable_agc_changed(self):
        self.update_diagram()

    def slot_tx_enable_sin_generator_changed(self):
        self.update_diagram()

    def config_to_fields(self):
        def to_mega(text):
            value = float(text) / 1.0e6
            return str(value)

        # [board.common]
        value = self.m_cfg["board.common.serial_number"]
        self.ui.lineEdit_serial_number.setText(value)
        value = self.m_cfg["board.common.fp_chunks_number"]
        self.ui.lineEdit_fp_chunks_number.setText(value)
        value = self.m_cfg["board.common.clock_source"]
        self.ui.comboBox_clock_source.setCurrentText(value)
        value = self.m_cfg["board.common.enable_tx"]
        self.ui.comboBox_enable_tx.setCurrentText(value)
        value = self.m_cfg["board.common.enable_rx"]
        self.ui.comboBox_enable_rx.setCurrentText(value)
        value = self.m_cfg["board.common.folder_tx"]
        self.ui.lineEdit_folder_tx.setText(value)
        value = "<p style='white-space:pre'><font color=black>" + value + "</p>"
        self.ui.lineEdit_folder_tx.setToolTip(value)
        value = self.m_cfg["board.common.folder_rx"]
        self.ui.lineEdit_folder_rx.setText(value)
        value = "<p style='white-space:pre'><font color=black>" + value + "</p>"
        self.ui.lineEdit_folder_rx.setToolTip(value)
        # [board.tx]
        value = self.m_cfg["board.tx.sample_rate"]
        self.ui.lineEdit_tx_sample_rate.setText(to_mega(value))
        value = self.m_cfg["board.tx.center_frequency"]
        self.ui.lineEdit_tx_center_frequency.setText(to_mega(value))
        value = self.m_cfg["board.tx.bandwidth"]
        self.ui.lineEdit_tx_bandwidth.setText(to_mega(value))
        value = self.m_cfg["board.tx.gain"]
        self.ui.lineEdit_tx_gain.setText(value)
       # [board.rx]
        value = self.m_cfg["board.rx.sample_rate"]
        self.ui.lineEdit_rx_sample_rate.setText(to_mega(value))
        value = self.m_cfg["board.rx.center_frequency"]
        self.ui.lineEdit_rx_center_frequency.setText(to_mega(value))
        value = self.m_cfg["board.rx.bandwidth"]
        self.ui.lineEdit_rx_bandwidth.setText(to_mega(value))
        value = self.m_cfg["board.rx.gain"]
        self.ui.lineEdit_rx_gain.setText(value)
        value = self.m_cfg["board.rx.enable_agc"]
        self.ui.comboBox_rx_enable_AGC.setCurrentText(value)
        # [test]
        value = self.m_cfg["test.enable_sin_generator"]
        self.ui.comboBox_tx_enable_sin_generator.setCurrentText(value)
        value = self.m_cfg["test.sin_frequency"]
        self.ui.lineEdit_tx_sin_frequency.setText(to_mega(value))
        value = self.m_cfg["test.tx_frames_number"]
        self.ui.lineEdit_tx_frames_number.setText(value)
        value = self.m_cfg["test.rx_frames_number"]
        self.ui.lineEdit_rx_frames_number.setText(value)

    def fields_to_config(self):
        def from_mega(text):
            value = float(text) * 1.0e6
            return str(value)

        # [board.common]
        value = self.ui.lineEdit_serial_number.text()
        self.m_cfg["board.common.serial_number"] = value
        value = self.ui.lineEdit_fp_chunks_number.text()
        self.m_cfg["board.common.fp_chunks_number"] = value
        value = self.ui.comboBox_clock_source.currentText()
        self.m_cfg["board.common.clock_source"] = value
        value = self.ui.comboBox_enable_tx.currentText()
        self.m_cfg["board.common.enable_tx"] = value
        value = self.ui.comboBox_enable_rx.currentText()
        self.m_cfg["board.common.enable_rx"] = value
        value = self.ui.lineEdit_folder_tx.text()
        self.m_cfg["board.common.folder_tx"] = value
        value = self.ui.lineEdit_folder_rx.text()
        self.m_cfg["board.common.folder_rx"] = value
        # [board.tx]
        value = self.ui.lineEdit_tx_sample_rate.text()
        self.m_cfg["board.tx.sample_rate"] = from_mega(value)
        value = self.ui.lineEdit_tx_center_frequency.text()
        self.m_cfg["board.tx.center_frequency"] = from_mega(value)
        value = self.ui.lineEdit_tx_bandwidth.text()
        self.m_cfg["board.tx.bandwidth"] = from_mega(value)
        value = self.ui.lineEdit_tx_gain.text()
        self.m_cfg["board.tx.gain"] = value
       # [board.rx]
        value = self.ui.lineEdit_rx_sample_rate.text()
        self.m_cfg["board.rx.sample_rate"] = from_mega(value)
        value = self.ui.lineEdit_rx_center_frequency.text()
        self.m_cfg["board.rx.center_frequency"] = from_mega(value)
        value = self.ui.lineEdit_rx_bandwidth.text()
        self.m_cfg["board.rx.bandwidth"] = from_mega(value)
        value = self.ui.lineEdit_rx_gain.text()
        self.m_cfg["board.rx.gain"] = value
        value = self.ui.comboBox_rx_enable_AGC.currentText()
        self.m_cfg["board.rx.enable_agc"] = value
        # [test]
        value = self.ui.comboBox_tx_enable_sin_generator.currentText()
        self.m_cfg["test.enable_sin_generator"] = value
        value = self.ui.lineEdit_tx_sin_frequency.text()
        self.m_cfg["test.sin_frequency"] = from_mega(value)
        value = self.ui.lineEdit_tx_frames_number.text()
        self.m_cfg["test.tx_frames_number"] = value
        value = self.ui.lineEdit_rx_frames_number.text()
        self.m_cfg["test.rx_frames_number"] = value

    def on_exit(self):
        self.ui.pushButton_Run.setText("Run")
        self.ui.pushButton_Run.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())
