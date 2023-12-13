from PySide6 import QtCore, QtWidgets
import sys


class qt_filter():
    def __init__(self):
        self.label = QtWidgets.QLabel()
        self.label.setAttribute(
            QtCore.Qt.WA_TransparentForMouseEvents)
        self.label.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                                  QtCore.Qt.WindowStaysOnTopHint)
        self.label.setGeometry(0, 0, 1920, 1080)
        self.label.setStyleSheet('background-color: #111111;')
        self.label.setWindowOpacity(0.5)

        self.label.show()

    def update(self, n):
        self.label.setWindowOpacity(n)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = qt_filter()

    main_window.update(0.8)

    sys.exit(app.exec())
