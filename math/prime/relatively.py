import math
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

Sentence(0.06, "[Starting now........]").sentence()
Sentence(0.06, "[This program is relatively prime determination \
program.]").sentence()

def Relatively():
    a = input("[No.1]Please enter any integer:")
    b = input("[No.2]Please enter any integer:")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("ERROR")
        exit()
    data = math.gcd(a, b)
    if data == 1:
        Sentence(0.06, str(a) + " and " + str(b) + " are \
relatively prime!").sentence()
    else:
        Sentence(0.06, str(a) + " and " + str(b) + " aren't \
relatively prime.").sentence()
    word = input("[1:{again} or 2:{end} Please enter 1 or 2]:")
    if word == "1":
        Relatively()
    elif word == "2":
        Sentence(0.06, "End........").sentence()
    else:
        print("ERROR")

Relatively()
