import time

def fibonacci(number, mode):
    if number <= 0:
        print("None")
    elif number <= 2:
        print("フィボナッチ数列の第" + str(number) + "項は\n"\
              + "1\nです")
    elif number >= 3:
        box = [1, 1]
        for i in range(0, number - 2):
            new_number = box[i] + box[i + 1]
            box.append(new_number)
        if mode == "a":
            print("フィボナッチ数列の第" + take + "項は\n"\
                  + str(box[int(take) - 1]) + "\nです。")
        else:
            count = 0
            for k in box:
                count += 1
                print(str(k) + "(第" + str(count) + "項)")
                time.sleep(0.01)
    else:
        for word3 in "[システムエラー発生。計算ソフトを強制終了します。":
            print(word3, end = "", flush = True)
            time.sleep(0.05)
        print("]")
        exit()

for word1 in "[フィボナッチ数列計算ソフト起動中.....":
    print(word1, end = "", flush = True)
    time.sleep(0.05)
print("]")
or_mode = input("モードを選択してください。\n"
                "[a]索引モード:指定した項の値を出力します。\n"
                "[b]表示モード:初項から指定した項まで出力します。\n"
                "[]の中の文字を入力してください:")
if or_mode == "a":
    take = input("第何項の値を出力しますか？\n"
                 "自然数かつアラビア数字で入力してください。:")
elif or_mode == "b":
    take = input("初項から第何項までの値を出力しますか？\n"
                 "自然数かつアラビア数字で入力してください。:")
else:
    for word2 in "[システムエラー発生。計算ソフトを強制終了します。":
        print(word2, end = "", flush = True)
        time.sleep(0.05)
    print("]")
    exit()
fibonacci(int(take), or_mode)
