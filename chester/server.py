import sys
from socket import socket, AF_INET, SOCK_DGRAM

from PyQt4 import QtGui, QtCore


def forward_clicked(*args):
    print 'top am called'


def right_clicked(*args):
    print 'right am called'


def left_clicked(*args):
    print 'left am called'


def connect():
    pass


def window():
    connect()
    app = QtGui.QApplication(sys.argv)
    widget_manager = QtGui.QWidget()
    widget_manager.setGeometry(200, 200, 200, 200)

    forward = QtGui.QPushButton(widget_manager)
    forward.setText("Forward")
    forward.move(60, 10)
    forward.clicked.connect(forward_clicked)

    left = QtGui.QPushButton(widget_manager)
    left.setText("Left")
    left.move(10, 70)
    left.clicked.connect(left_clicked)

    right = QtGui.QPushButton(widget_manager)
    right.setText("Right")
    right.move(100, 70)
    right.clicked.connect(right_clicked)

    widget_manager.setWindowTitle('PyQt')
    widget_manager.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
