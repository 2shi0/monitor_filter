# monitor_filter
pythonで動作する、画面を薄暗くするフィルターです
# 使い方
```
app = QtWidgets.QApplication(sys.argv)
main_window = qt_filter()
```
でオブジェクトを作って、

```
main_window.update(0.8)
```
で明るさを更新します(0に近いほど明るくて、1に近いほど暗い)。

プログラムの最後で
```
sys.exit(app.exec())
```
で終了させたほうがいいと思います。