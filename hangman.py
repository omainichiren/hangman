import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_____    ",
              "|        ",
              "|    |   ",
              "|    0   ",
              "|   /|\  ",
              "|   / \  ",
              "|        ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    while wrong < len(stages) - 1:
        msg = "1文字を予想して:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("貴方の勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("貴方の負け！正解は{}".format(word))

hlist = ["cat", "unkchan", "yaa", "397", "893"]
q = random.randint(0,4)
hangman(hlist[q])
