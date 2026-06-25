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

black = [] # 黒の場所のリスト
white = [] # 白の場所のリスト
hantai = {}
black_okeru = []
white_okeru = []
batu = []

import random
import time


# 黒が置ける場所を探索する関数
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
    
    右左(1, black, black_okeru, 1, 3)  # 右
    右左(-1, black, black_okeru, 1, 3)  # 左
    上下(-8, black, black_okeru, 1, 3)  # 上
    上下(8, black, black_okeru, 1, 3)  # 下
    斜め(-7, black, black_okeru, 1, 3)  # 右上
    斜め(7, black, black_okeru, 1, 3)  # 左下
    斜め(-9, black, black_okeru, 1, 3)  # 左上
    斜め(9, black, black_okeru, 1, 3)  # 右下


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
    右左(1, white, white_okeru, 2, 3)  # 右
    右左(-1, white, white_okeru, 2, 3)  # 左
    上下(-8, white, white_okeru, 2, 3)  # 上
    上下(8, white, white_okeru, 2, 3)  # 下
    斜め(-7, white, white_okeru, 2, 3)  # 右上
    斜め(7, white, white_okeru, 2, 3)  # 左下
    斜め(-9, white, white_okeru, 2, 3)  # 左上
    斜め(9, white, white_okeru, 2, 3)  # 右下


def 右左(e, f, g, h, i):
    """
    e:向きの数
    f:黒ならblack、白ならwhiteのリスト
    g:黒ならblack_okeru、白ならwhite_okeruのリスト
    h:相手のコマ種類番号（黒なら1、白なら2）
    i:置ける場所を表すコマの番号（3）
    """
    for c in range(len(f)):  # 右左
        j = [] # kaesu用リスト
        b = e  # 一つ移動する
        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 一つ移動した先は白？
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 白を抜けるまで進む
                j.append(f[c] + b)
                b += e
                if e == 1 and (f[c]) % 8 >= (f[c] + b) % 8:
                    break
                if e == -1 and (f[c]) % 8 <= (f[c] + b) % 8:
                    break
            if e == 1 and (f[c]) % 8 >= (f[c] + b) % 8:
                break
            if e == -1 and (f[c]) % 8 <= (f[c] + b) % 8:
                break
            
            if board[(f[c]+b) // 8][(f[c]+b) % 8] == 0:
                try:  # 今いる場所にコマは置かれてない？
                    hantai[f[c]][e] ={"kaesu":j,"sitei":f[c] + b}
                except:
                    hantai[f[c]] = {e:{"kaesu":j,"sitei":f[c]+b}}
                board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                g.append(f[c] + b)

def 上下(e, f, g, h, i):
    """
    e:向きの数
    f:黒ならblack、白ならwhiteのリスト
    g:黒ならblack_okeru、白ならwhite_okeruのリスト
    h:相手のコマ種類番号（黒なら1、白なら2）
    i:置ける場所を表すコマの番号（3）
    """
    for c in range(len(f)):  # 上下
        j = [] # kaesu用リスト
        b = e  # 一つ移動する
        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 一つ移動した先は白？
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 白を抜けるまで進む
                j.append(f[c] + b)
                b += e
                if e == 8 and (f[c] + b) > 63:
                    break
                if e == -8 and (f[c] + b) < 0:
                    break
            if e == 8 and (f[c] + b) > 63:
                break
            if e == -8 and (f[c] + b) < 0:
                break
            
            if board[(f[c]+b) // 8][(f[c]+b) % 8] == 0:
                try:
                    hantai[f[c]][e] ={"kaesu":j,"sitei":f[c] + b}
                except:
                    hantai[f[c]] = {e:{"kaesu":j,"sitei":f[c]+b}}
                board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                g.append(f[c] + b)


def 斜め(e, f, g, h, i):
    """
    e:向きの数
    f:黒ならblack、白ならwhiteのリスト
    g:黒ならblack_okeru、白ならwhite_okeruのリスト
    h:相手のコマ種類番号（黒なら1、白なら2）
    i:置ける場所を表すコマの番号（3）
    """
    
    for c in range(len(f)):  # 上下
        j = [] # kaesu用リスト
        b = e  # 一つ移動する
        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 一つ移動した先は白？
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 白を抜けるまで進む
                j.append(f[c] + b)
                b += e
                if (e == -7 or e == 9) and (f[c]) % 8 >= (f[c] + b) % 8:
                    break
                if (e == 7 or e == -9) and (f[c]) % 8 <= (f[c] + b) % 8:
                    break
                if (e == 7 or e == 9) and (f[c] + b) > 63:
                    break
                if (e == -7 or e == -9) and (f[c] + b) < 0:
                    break
            if (e == -7 or e == 9) and (f[c]) % 8 >= (f[c] + b) % 8:
                break
            if (e == 7 or e == -9) and (f[c]) % 8 <= (f[c] + b) % 8:
                break
            if (e == 7 or e == 9) and (f[c] + b) > 63:
                break
            if (e == -7 or e == -9) and (f[c] + b) < 0:
                break
            
            if board[(f[c]+b) // 8][(f[c]+b) % 8] == 0:
                try:
                    hantai[f[c]][e] ={"kaesu":j,"sitei":f[c] + b}
                except:
                    hantai[f[c]] = {e:{"kaesu":j,"sitei":f[c]+b}}
                board[(f[c] + b) // 8][(f[c] + b) % 8] = i
                g.append(f[c] + b)


def reset():
    global black_okeru
    global white_okeru
    global hantai 
    global black
    global white
    black_okeru = []
    white_okeru = []
    hantai= {}
    black = []
    white = []
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 3:
                batu.append(left + 8 * a)  # 黒の位置を見つける
            left += 1
    for i in range(len(batu)):
        a = batu[i]
        board[a // 8][a % 8] = 0


def show_color():
    table = {2: "●", 1: "○", 3: "×", 0: "□"}
    print("  1 2 3 4 5 6 7 8")
    for i,a in enumerate(board):
        print(str(i+1)+" "+(" ".join(table[b] for b in a)))


def okerubasyo_kuro():
    w =input("置ける場所を指定してください")
    w1 = w[0]
    w2 = w[1]
    w =(int(w1)-1)*8+int(w2)-1
    if w in black_okeru:
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


def kaesu_kuro(w):
    for a,b in hantai.items():
        for c,d in b.items():
            if int(w) == d["sitei"]:
                board[d["sitei"]//8][d["sitei"]%8] =2
                for i in d["kaesu"]:
                 board[i // 8][i % 8] = 2
            


def kaesu_shiro(w):
    for a,b in hantai.items():
        for c,d in b.items():
            if int(w) == d["sitei"]:
                board[d["sitei"]//8][d["sitei"]%8] =1
                for i in d["kaesu"]:
                 board[i // 8][i % 8] = 1



while True:
    print()
    kuro_okeru()
    show_color() 
    okerubasyo_kuro()
    show_color()
    print()
    reset()
    time.sleep(1)
    shiro_okeru()
    okerubasyo_shiro()
    show_color()
    reset()
