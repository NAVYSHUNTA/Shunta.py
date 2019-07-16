import random

def hangman(word):
 print(str(len(word))+"文字です")
 wrong=0
 part=["",
       "_____    ",
       "|    |   ",
       "|    |   ",
       "|    0   ",
       "|   /|\  ",
       "|    |   ",
       "|   / \  ",
       "|        ",
       "|        ",
       "|________"]
 rletters=list(word)
 board=["_"]*len(word)
 win=False
 print("ハングマンへようこそ！")
 while wrong<len(part)-1:
  print("\n")
  char=input("1文字を予想してね:")
  if char in rletters:
   cind=rletters.index(char)
   board[cind]=char
   rletters[cind]="$sh$sh$"
  else:
   wrong+=1
  print("".join(board))
  e=wrong+1
  print("\n".join(part[:e]))
  if "_" not in board:
   print("あなたの勝ち！")
   print("".join(word))
   win=True
   break
 if not win:
  print("あなたの負け！正解は{}".format(word))

kingdom=["busy","easily","every","question","each","research","rate","country","world","japan","test","disorders","trigger","prescription","significant","diabetes","tendencies","ownership","dramatic","obesity","vacation","glassland","widespread","statistics","cancer","toward","equal","industry","benefit","actually","megadose","anemic","ingredients"]
a=random.choice(kingdom)
hangman(a)
