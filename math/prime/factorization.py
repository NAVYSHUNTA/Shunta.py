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

Sentence(0.07, "[Starting now........]").sentence()
Sentence(0.07, "[Prime factorization program]").sentence()

def Prime():
    number_data = input("[Please enter any natural number of 2 or more]:")
    try:
        number = int(number_data)
        box = []
        i = 2
        count = int(math.sqrt(number))
    except ValueError:
        print("ERROR")
        exit()
    while True:
        if number == 1:
            print("ERROR")
            exit()
        elif number % i == 0:
            box.append(i)
            number /= i
            number = int(number)
            if number == 1:
                break
        elif count == i:
            box.append(number)
            break
        else:
            i += 1
    if len(box) == 1:
        Sentence(0.07, str(box[0]) + " is prime number!").sentence()
    else:
        box = list(map(str, box))
        data = "x".join(box)
        Sentence(0.07, number_data + " is " + data).sentence()
    word = input("[1:{again} or 2:{end} Please enter 1 or 2:]")
    if word == "1":
        Prime()
    elif word == "2":
        Sentence(0.07, "[End........]").sentence()
    else:
        print("ERROR")

Prime()
