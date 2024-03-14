import time

class Sentence:
    def __init__(self, period, word):
        self.period = period
        self.word = word

    def print_sentence(self):
        for wi in self.word: 
            print(wi, end = "", flush = True)
            time.sleep(self.period)
        print()

Sentence(0.07, "Hello World!").print_sentence()
Sentence(0.05, "Have a nice day!").print_sentence()
