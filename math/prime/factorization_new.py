n = int(input())
box = []

# 素数判定
def check(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        is_check = True
        for i in range(2, int(n ** 0.5) + 1):
            if num % i == 0 and num != i:
                is_check = False
        if is_check:
            return True
        else:
            return False

# 素数である約数をboxに格納する。
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if check(i):
            box.append(i)
        if check(n // i):
            box.append(n // i)
box.sort()
cnt = 0

print(str(n) + "を素因数分解すると次のようになります。")
while n != 1:
    if n % box[cnt] == 0:
        if n // box[cnt] != 1:
            print(box[cnt], end = " x ")
        else:
            print(box[cnt])
        n = n // box[cnt]
    else:
        cnt += 1
