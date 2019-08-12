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

Sentence(0.07, "Hello World!").sentence()
Sentence(0.05, "Have a nice day!").sentence()
