# turtleライブラリの使い方です。
# <注意>このプログラムを実行する場合は、プログラム名をturtle.py以外の名前に変更してください。そうしないとエラーになります。
from turtle import *
import time

class Draw:
    count = 0                # このクラスが何回呼び出されたかカウントします。
    def __init__(self):
        reset()              # キャンパスを白にリセットします。
        shape("turtle")      # 亀を呼び出します。
        speed(0)             # 亀の速度を設定します。最高速度を設定するには引数に0を格納します。
        if Draw.count != 0:  # 初回時は実行しません。
            time.sleep(0.5)  # 0.5秒間待機します。
        Draw.count += 1

    # 関数polygonは、正(vertex)角形を描く関数です。
    def polygon(self, vertex = 4, sidelength = 100):  # vertexは頂点の個数で、sidelengthは辺の長さです。
        self.sidelength = sidelength
        self.vertex = vertex
        for _ in range(self.vertex):
            forward(self.sidelength)
            right(360 / self.vertex)

    # 関数starは、スターを描く関数です。
    def star(self, sidelength = 100):
        self.sidelength = sidelength
        for _ in range(5):
            forward(self.sidelength)
            right(180 - 36)

    # 関数starSpiralは、スターを螺旋状に描く関数です。
    def starSpiral(self):
        Draw.size = 5
        for _ in range(100):
            self.star(Draw.size)
            Draw.size += 5
            right(5)

Draw().polygon()        # 辺の長さが100の正方形を描画します。
Draw().polygon(3)       # 辺の長さが100の正三角形を描画します。
Draw().polygon(6, 150)  # 辺の長さが150の正六角形を描画します。

Draw().star()           # 辺の長さが100のスターを描画します。
Draw().star(200)        # 辺の長さが200のスターを描画します。

Draw().starSpiral()     # スターを螺旋状に描画します。
mainloop()              # 自動でウィンドウを閉じないようにします。自動で閉じたい場合は、この行を削除してください。
