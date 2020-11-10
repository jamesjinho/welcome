import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QWidget, QLabel, QGridLayout, QVBoxLayout, QDesktopWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication, QDate, QTime, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.iconPath = 'D:\\OneDrive - JLab Technical Service\\# JLab\\07 IoT Concept\\_Pictures\\'
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon(self.iconPath + 'Exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # self.statusBar().showMessage('Ready')
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)+' '
                                     + self.time.toString(Qt.DefaultLocaleLongDate))

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        QToolTip.setFont(QFont('D2Coding', 10))
        self.setToolTip('This is a <b>QWidget</> widget')

        btn = QPushButton('Quit', self)
        btn.setFont(QFont('Tahoma', 11))
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.setStatusTip('You can exit application')
        btn.move(50, 400)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Cubloc CB210 Control')
        self.setWindowIcon(QIcon(self.iconPath + 'IoTicon.png'))
        # self.setGeometry(300, 300, 400, 200)    # 창의 x, y 위치 및 크기
        # self.move(300, 300)
        self.resize(800, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기정보 확인
        cp = QDesktopWidget().availableGeometry().center()  # 모니터 화면의 가운데 위치 확인
        qr.moveCenter(cp)   # 창의 직사각형 (Left top) 위치를 중앙으로 이동
        self.move(qr.topLeft()) # 창의 직사각형 (Left top) 위치를 Left top으로 이동하여 결과적으로 정 중아에 위치


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
