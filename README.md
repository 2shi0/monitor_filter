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

# 注意
```
if __name__ == "__main__":
```
より以下のコードは動作検証用なので、使用するときは削除してください。

完全に同期処理で動いてるので、なんか問題が起こったら僕に相談してね