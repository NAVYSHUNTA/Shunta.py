def fibonacci(number):
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
        print("フィボナッチ数列の第" + take + "項は\n"\
              + str(box[int(take) - 1]) + "\nです。")
    else:
        print("[システムエラー発生。計算ソフトを強制終了します。]")
        exit()

print("[フィボナッチ数列計算ソフト起動中.....]")
take = input("第何項の値を出力しますか？\n"
             "自然数かつアラビア数字で入力してください。:")

fibonacci(int(take))
