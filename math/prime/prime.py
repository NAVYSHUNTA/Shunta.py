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
Sentence(0.06, "[Prime number determination program]").sentence()

def Number():
    try:
        data = int(input("[Please enter any natural number of 2 or more]:"))
    except ValueError:
        print("ERROR")
        exit()
    if data <= 1:
        print("ERROR")
        exit()
    elif data == 2 or data == 3:
        count = 1
    elif data >= 4:
        for i in range(2, int(math.sqrt(data) + 1)):
            if data == 2 or data == 3:
                count = 1
                break
            elif data % i == 0:
                count = 0
                break
            else:
                count = 1
    if count == 0:
        Sentence(0.06, str(data) + " is not prime number.").sentence()
    else:
        Sentence(0.06, str(data) + " is prime number!").sentence()
    word = input("[1:{again} or 2:{end} Please enter 1 or 2]:")
    if word == "1":
        Number()
    elif word == "2":
        Sentence(0.06, "[End........]").sentence()
    else:
        print("ERROR")

Number()
