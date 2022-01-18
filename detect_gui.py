import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from gui_config import *


result_dir = './runs/detect/exp'
labels_dir = result_dir + '/labels'


def detect_label(filename: str):
    label_path = os.path.join(labels_dir, filename)
    with open(label_path, 'r') as f:
        det_labels = f.readlines()
        for det_label in det_labels:
            det_flag = det_label.split(' ')[0]
            if det_flag == '1':
                return 'head'
    return 'helmet'


class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.input_dir = None
        self.filename = None
        self.setupUi(self)
        self.toolButton.clicked.connect(self.view_files)
        self.detect_button.clicked.connect(self.detect)
        self.cancel_button.clicked.connect(self.cancel)

    def view_files(self):
        self.result_label.setText('')
        load_file = QFileDialog.getOpenFileName()[0]
        self.filename = load_file.split('/')[-1]
        input_dir = load_file.split('/')[:-1]
        self.input_dir = '/'.join(input_dir)
        self.png_label.setPixmap(QPixmap(load_file))

    def detect(self):
        # if os.path.exists(result_dir):
        #     os.system("rm -r {}".format(result_dir))
        # file_path = os.path.join(self.input_dir, self.filename)
        # os.system("bash make_detect.sh {}".format(file_path))
        # result_file = os.listdir(result_dir)
        # result_file.remove('labels')
        if self.filename is None:
            return
        result_png = os.path.join(result_dir, self.filename)
        self.png_label.setPixmap(QPixmap(result_png))
        label_filename = self.filename.split('.')[0] + '.txt'
        helmet_flag = detect_label(label_filename)
        if helmet_flag == 'head':
            self.result_label.setStyleSheet('color:red')
            self.result_label.setText('Warning: Person With No Helmet Detected!')
        else:
            self.result_label.setStyleSheet('color:green')
            self.result_label.setText('Helmet Detection Pass')

    def cancel(self):
        self.png_label.setPixmap(QPixmap(''))
        self.input_dir = None
        self.filename = None
        self.result_label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
