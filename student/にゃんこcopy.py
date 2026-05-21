board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

import random

black = []
white = []
batu = []
black_okeru = []
white_okeru = []
hantai = {}
w = 100
j = []


def kuro_okeru():
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 2:
                black.append(left + 8 * a)  # 黒の位置を見つける
            left += 1
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 1:
                white.append(left + 8 * a)  # 白の位置を見つける
            left += 1
    rightandleft(1, black, black_okeru, 1, 3)  # 右
    rightandleft(-1, black, black_okeru, 1, 3)  # 左
    upanddown(-8, black, black_okeru, 1, 3)  # 上
    upanddown(8, black, black_okeru, 1, 3)  # 下
    naname(-7, black, black_okeru, 1, 3)  # 右上
    naname(7, black, black_okeru, 1, 3)  # 左下
    naname(-9, black, black_okeru, 1, 3)  # 左上
    naname(9, black, black_okeru, 1, 3)  # 右下


def shiro_okeru():
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 1:
                white.append(left + 8 * a)  # 白の位置を見つける
            left += 1
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 2:
                black.append(left + 8 * a)  # 黒の位置を見つける
            left += 1
    rightandleft(1, white, white_okeru, 2, 3)  # 右
    rightandleft(-1, white, white_okeru, 2, 3)  # 左
    upanddown(-8, white, white_okeru, 2, 3)  # 上
    upanddown(8, white, white_okeru, 2, 3)  # 下
    naname(-7, white, white_okeru, 2, 3)  # 右上
    naname(7, white, white_okeru, 2, 3)  # 左下
    naname(-9, white, white_okeru, 2, 3)  # 左上
    naname(9, white, white_okeru, 2, 3)  # 右下


def rightandleft(e, f, g, h, i):
    global j
    for c in range(len(f)):  # 右左
        b = e  # 一つ移動する
        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 一つ移動した先は白？
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 白を抜けるまで進む
                j.append(f[c] + b)
                b += e
            if (board[(f[c] + b) // 8][(f[c] + b) % 8] == 0):
              try:  # 今いる場所にコマは置かれてない？
                hantai[f[c]][e] ={"kaesu":j,"sitei":f[c] + b}
              except:
                  hantai[f[c]] = {e:{"kaesu":j,"sitei":f[c]+b}}
              j = []
              if e == 1 and (f[c]) % 8 < (f[c] + b) % 8:  # 右の条件
                  board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                  g.append(f[c] + b)
              elif e == -1 and (f[c]) % 8 > (f[c] + b) % 8:  # 左の条件
                  board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                  g.append(f[c] + b)


def upanddown(e, f, g, h, i):
    global j
    for c in range(len(f)):  # 上下
        b = e
        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
                j.append(f[c] + b)
                b += e
            if board[(f[c] + b) // 8][(f[c] + b) % 8] == 0:
                try:
                  hantai[f[c]][e] ={"kaesu":j,"sitei":f[c] + b}
                except:
                    hantai[f[c]] = {e:{"kaesu":j,"sitei":f[c]+b}}  
                j = []
                if e == -8 and (f[c] + b) >= 0:
                    board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                    g.append(f[c] + b)
                elif e == 8 and (f[c] + b) <= 63:
                    board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                    g.append(f[c] + b)


def naname(e, f, g, h, i):
    global j
    for c in range(len(f)):  # 斜め
        b = e
        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
                j.append(f[c] + b)
                b += e
            if board[(f[c] + b) // 8][(f[c] + b) % 8] == 0:
                try:
                  hantai[f[c]][e] ={"kaesu":j,"sitei":f[c] + b}
                except: #返す場所を辞書に保存
                    hantai[f[c]] = {e:{"kaesu":j,"sitei":f[c]+b}}
                j = []
                if e == -7 and (f[c]) % 8 < (f[c] + b) % 8 and (f[c] + b) >= 0:  # 右上
                    board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                    g.append(f[c] + b)
                elif (
                    e == 7 and (f[c]) % 8 > (f[c] + b) % 8 and (f[c] + b) <= 63
                ):  # 左下
                    board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                    g.append(f[c] + b)
                elif (
                    e == -9 and (f[c]) % 8 > (f[c] + b) % 8 and (f[c] + b) >= 0
                ):  # 左上
                    board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                    g.append(f[c] + b)
                elif (
                    e == 7 and (f[c]) % 8 < (f[c] + b) % 8 and (f[c] + b) <= 63
                ):  # 右下
                    board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                    g.append(f[c] + b)


def show():
    for a in board:
        print(" ".join(str(b) for b in a))


def show_color():
    table = {2: "●", 1: "○", 3: "×", 0: "□"}
    for a in board:
        print(" ".join(table[b] for b in a))


def okerubasyo_kuro():
    w = input("置ける場所を指定してください")
    if int(w) in black_okeru:
        kaesu_kuro(w)
        # board[int(w) // 8][int(w) % 8] = 2
    else:
        okerubasyo_kuro()  # 置ける場所以外を指定した場合、もう一回指定させる


def okerubasyo_shiro():
    if len(white_okeru) >= 1:
        w = random.choice(white_okeru)
        kaesu_shiro(w)
        # board[w // 8][w % 8] = 1
    else:
        okerubasyo_shiro()  # 置ける場所以外を指定した場合、もう一回指定させる


def reset():
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 3:
                batu.append(left + 8 * a)  # 黒の位置を見つける
            left += 1
    for i in range(len(batu)):
        a = batu[i]
        board[a // 8][a % 8] = 0


def kaesu_kuro(w):
    print(hantai)

def kaesu_shiro(w):
    pass



for i in range(10):
    kuro_okeru()
    show_color()
    okerubasyo_kuro()
    reset()

    shiro_okeru()
    okerubasyo_shiro()
    reset()
