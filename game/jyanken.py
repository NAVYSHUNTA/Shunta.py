import random
import time

class Sentence:
    def __init__(self, time_long, word):
        self.time_long = time_long
        self.word = word
        self.my_list = list(self.word)
    def sentence(self):
        for i in range(0, len(self.word) - 1):
            print(self.my_list[i], end = "", flush = True)
            time.sleep(self.time_long)
        print(self.my_list[-1])

def jyanken():
    my = input("['gu'か'cho'か'pa'のどれかを入力してください]:")
    cpu_list = ["gu", "cho", "pa"]
    cpu = random.choice(cpu_list)
    Sentence(0.07, "[  自分[{}]  vs  相手[{}]  ]"
    .format(my, cpu)).sentence()
    if my == cpu:
        Sentence(0.07, "[あいこです]").sentence()
        jyanken()
    elif my == "cho":
        if cpu == "gu":
            Sentence(0.07, "[君の負け！]").sentence()
        else:
            Sentence(0.07, "[君の勝ち！]").sentence()
    elif my == "pa":
        if cpu == "cho":
            Sentence(0.07, "[君の負け！]").sentence()
        else:
            Sentence(0.07, "[君の勝ち！]").sentence()
    elif my == "gu":
        if cpu == "pa":
            Sentence(0.07, "君の負け！").sentence()
        else:
            Sentence(0.07, "君の勝ち！").sentence()
    else:
        Sentence(0.05, 'エラー発生。ジャンケンゲーム'
                 'アプリを強制終了します').sentence()
        exit()

Sentence(0.07, "[ジャンケンゲームアプリ起動中......]").sentence()
Sentence(0.06, "[ジャンケンゲーム開始]").sentence()
jyanken()
