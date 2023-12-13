from PySide6 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel()
label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # マウスイベント透過
label.setWindowFlags(QtCore.Qt.FramelessWindowHint |  # 枠なしにする
                     QtCore.Qt.WindowStaysOnTopHint)  # 常に最前面に表示
label.setGeometry(0, 0, 1920, 1080)  # 全画面に
label.setStyleSheet('background-color: #111111;')  # 背景色の定義
label.setWindowOpacity(0.5)  # 透明度設定

label.show()

sys.exit(app.exec())
