import random
import time

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

black = []  # 黒の場所のリスト
white = []  # 白の場所のリスト
hantai = {}
black_okeru = []
white_okeru = []
batu = []


# 黒が置ける場所を探索する関数
def kuro_okeru():
    global black, white
    black = []
    white = []
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 2:
                black.append(left + 8 * a)  # 黒の位置を見つける
            elif i == 1:
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
    global black, white
    black = []
    white = []
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 1:
                white.append(left + 8 * a)  # 白の位置を見つける
            elif i == 2:
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
    for c in range(len(f)):  # 右左
        b = e  # 一つ移動する
        j = []  # 各コマ・各方向ごとにリストを初期化
        
        # 盤面の範囲内チェック
        if not (0 <= f[c] + b <= 63):
            continue

        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 一つ移動した先は相手の石？
            flag = True
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:  # 相手の石を抜けるまで進む
                j.append(f[c] + b)
                # 端に到達した時のラップアラウンド（逆側の行へ回り込む現象）を防止
                if e == 1 and (f[c] + b) % 8 == 7:
                    flag = False
                    break
                if e == -1 and (f[c] + b) % 8 == 0:
                    flag = False
                    break
                b += e
                if not (0 <= f[c] + b <= 63):
                    flag = False
                    break
            
            if not flag:
                continue

            # 抜けた先が空（0）か、すでに「3」が置いてある場所なら
            if board[(f[c] + b) // 8][(f[c] + b) % 8] in (0, 3):
                target = f[c] + b
                if target not in hantai:
                    hantai[target] = []
                hantai[target].append({"kaesu": j})
                
                board[target // 8][target % 8] = i
                if target not in g:
                    g.append(target)


def 上下(e, f, g, h, i):
    for c in range(len(f)):  # 上下
        b = e  # 一つ移動する
        j = []  # 各コマ・各方向ごとにリストを初期化
        
        if not (0 <= f[c] + b <= 63):
            continue

        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
            flag = True
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
                j.append(f[c] + b)
                b += e
                if not (0 <= f[c] + b <= 63):
                    flag = False
                    break
            
            if not flag:
                continue

            if board[(f[c] + b) // 8][(f[c] + b) % 8] in (0, 3):
                target = f[c] + b
                if target not in hantai:
                    hantai[target] = []
                hantai[target].append({"kaesu": j})
                
                board[target // 8][target % 8] = i
                if target not in g:
                    g.append(target)


def 斜め(e, f, g, h, i):
    for c in range(len(f)):  # 斜め
        b = e  # 一つ移動する
        j = []  # 各コマ・各方向ごとにリストを初期化
        
        if not (0 <= f[c] + b <= 63):
            continue

        if board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
            flag = True
            while board[(f[c] + b) // 8][(f[c] + b) % 8] == h:
                j.append(f[c] + b)
                # 左右の端に到達した時のラップアラウンド防止
                current_col = (f[c] + b) % 8
                if (e in (-7, 9) and current_col == 7) or (e in (7, -9) and current_col == 0):
                    # 次に進むと盤面外（ラップアラウンド）になるため、ここでストップ
                    b += e
                    flag = False
                    break
                b += e
                if not (0 <= f[c] + b <= 63):
                    flag = False
                    break
            
            # 抜けた先がさらに正しく盤面内かチェック
            if not (0 <= f[c] + b <= 63):
                flag = False

            if not flag:
                # もし抜けた先が空（0）で、ラップアラウンドもしていない有効なマスならOK
                if 0 <= f[c] + b <= 63 and board[(f[c] + b) // 8][(f[c] + b) % 8] in (0, 3):
                    pass
                else:
                    continue

            if board[(f[c] + b) // 8][(f[c] + b) % 8] in (0, 3):
                target = f[c] + b
                if target not in hantai:
                    hantai[target] = []
                hantai[target].append({"kaesu": j})
                
                board[target // 8][target % 8] = i
                if target not in g:
                    g.append(target)


def reset():
    global black_okeru, white_okeru, hantai, batu
    black_okeru = []
    white_okeru = []
    hantai = {}
    batu = []
    for a in range(8):
        left = 0
        for i in board[a]:
            if i == 3:
                batu.append(left + 8 * a)
            left += 1
    for i in range(len(batu)):
        a = batu[i]
        board[a // 8][a % 8] = 0


def show_color():
    table = {2: "●", 1: "○", 3: "×", 0: "□"}
    print("  0 1 2 3 4 5 6 7")  # 列番号を表示して入力しやすく
    for idx, a in enumerate(board):
        print(f"{idx} " + " ".join(table[b] for b in a))


def okerubasyo_kuro():
    if len(black_okeru) == 0:
        print("黒はパスです。")
        return
    try:
        w = int(input("置ける場所を指定してください (0-63 または 行列計算値): "))
        if w in black_okeru:
            kaesu_kuro(w)
        else:
            print("そこには置けません。")
            okerubasyo_kuro()
    except ValueError:
        okerubasyo_kuro()


def okerubasyo_shiro():
    if len(white_okeru) >= 1:
        w = random.choice(white_okeru)
        print(f"白（AI）は {w} に置きました。")
        kaesu_shiro(w)
    else:
        print("白はパスです。")


def kaesu_kuro(w):
    if w in hantai:
        board[w // 8][w % 8] = 2
        for move in hantai[w]:
            for i in move["kaesu"]:
                board[i // 8][i % 8] = 2


def kaesu_shiro(w):
    if w in hantai:
        board[w // 8][w % 8] = 1
        for move in hantai[w]:
            for i in move["kaesu"]:
                board[i // 8][i % 8] = 1


# メインループ
for i in range(10):
    print(f"\n--- ターン {i+1} (黒の番) ---")
    kuro_okeru()
    show_color()
    okerubasyo_kuro()
    reset()
    time.sleep(0.5)

    print(f"\n--- ターン {i+1} (白の番) ---")
    shiro_okeru()
    okerubasyo_shiro()
    reset()
    time.sleep(0.5)