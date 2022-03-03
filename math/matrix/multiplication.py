import numpy as np

print("正方行列Aと正方行列Bの積ABを計算するプログラムです")
boxa = int(input("行列Aまたは行列Bの行数を入力:"))
boxA = []
boxB = []
boxC = []
boxX = []
boxY = []
print("行列Aの第一行から順に行列の成分を入力してください")
print("例：[2 -4]の場合は2 -4 と入力します")
for i in range(boxa):
    boxA.append(list(map(int, input().split())))
print("行列Bの第一行から順に行列の成分を入力してください")
for j in range(boxa):
    boxB.append(list(map(int, input().split())))
boxA = np.array(boxA)
boxB = np.array(boxB)
for a in range(boxa):
    num_a = boxA[a]
    for b in range(boxa):
        num_b = (boxB[:,b])
        for c in range(boxa):
            num_c = num_a[c] * num_b[c]
            boxX.append(num_c)
        boxY.append(sum(boxX))
        boxX = []
    boxC.append(boxY)
    boxY = []
print(np.array(boxC))
