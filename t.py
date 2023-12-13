from PySide6 import QtCore, QtWidgets
import sys


class qt_filter():
    def __init__(self):
        self.label = QtWidgets.QLabel()
        self.label.setAttribute(
            QtCore.Qt.WA_TransparentForMouseEvents)  # マウスイベント透過
        self.label.setWindowFlags(QtCore.Qt.FramelessWindowHint |  # 枠なしにする
                                  QtCore.Qt.WindowStaysOnTopHint)  # 常に最前面に表示
        self.label.setGeometry(0, 0, 1920, 1080)  # 全画面に
        self.label.setStyleSheet('background-color: #111111;')  # 背景色の定義
        self.label.setWindowOpacity(0.5)  # 透明度設定

        self.label.show()

    def update(self, n):
        """
        画面の暗さを変更する（nは0.0~1.0の値）
        """
        self.label.setWindowOpacity(n)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = qt_filter()

    main_window.update(0.8)

    sys.exit(app.exec())
