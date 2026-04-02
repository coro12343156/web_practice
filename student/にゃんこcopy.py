board = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,2,1,0,0,0],
         [0,0,0,1,2,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

import random

black = []
white = []
black_okeru = []
white_okeru = []
w = 100


def kuro_okeru():
  for a in range(8):
   left = 0
   for i in board[a]:
     if i == 2:
      black.append(left+8*a) #黒の位置を見つける
     left += 1
  for a in range(8):
   left = 0
   for i in board[a]:
     if i == 1:
      white.append(left+8*a) #白の位置を見つける
     left += 1
  rightandleft(1,black,black_okeru,1,3) #右
  rightandleft(-1,black,black_okeru,1,3) #左
  upanddown(-8,black,black_okeru,1,3) #上
  upanddown(8,black,black_okeru,1,3) #下
  naname(-7,black,black_okeru,1,3) #右上
  naname(7,black,black_okeru,1,3)  #左下
  naname(-9,black,black_okeru,1,3) #左上
  naname(9,black,black_okeru,1,3)  #右下


def shiro_okeru():
  for a in range(8):
   left = 0
   for i in board[a]:
     if i == 1:
      white.append(left+8*a) #白の位置を見つける
     left += 1
  for a in range(8):
   left = 0
   for i in board[a]:
     if i == 2:
      black.append(left+8*a) #黒の位置を見つける
     left += 1
  rightandleft(1,white,white_okeru,2,4) #右
  rightandleft(-1,white,white_okeru,2,4) #左
  upanddown(-8,white,white_okeru,2,4) #上
  upanddown(8,white,white_okeru,2,4) #下
  naname(-7,white,white_okeru,2,4) #右上
  naname(7,white,white_okeru,2,4)  #左下
  naname(-9,white,white_okeru,2,4) #左上
  naname(9,white,white_okeru,2,4)  #右下

  

 
def rightandleft(e,f,g,h,i):
 for c in range(len(f)):  #右左
  b = e # 一つ移動する
  if board[(f[c]+b)//8][(f[c]+b)%8] == h: # 一つ移動した先は白？
    while board[(f[c]+b)//8][(f[c]+b)%8] == h: # 白を抜けるまで進む
      b += e
    if board[(f[c]+b)//8][(f[c]+b)%8] == 0: # 今いる場所にコマは置かれてない？
      if e == 1 and (f[c])%8 < (f[c]+b)%8: # 右の条件
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append([c]+b)
      elif e == -1 and (f[c])%8 > (f[c]+b)%8: # 左の条件
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append(f[c]+b)


def upanddown(e,f,g,h,i):
 for c in range(len(f)): #上下
   b = e
   if board[(f[c]+b)//8][(f[c]+b)%8] == h:
    while board[(f[c]+b)//8][(f[c]+b)%8] == h:
      b += e 
    if board[(f[c]+b)//8][(f[c]+b)%8] == 0:
      if e == -8 and (f[c]+b) >= 0:
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append(f[c]+b)
      elif e == 8 and (f[c]+b) <= 63:
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append(f[c]+b)


def naname(e,f,g,h,i):
 for c in range(len(f)): #斜め
  b = e
  if board[(f[c]+b)//8][(f[c]+b)%8] == h:
    while board[(f[c]+b)//8][(f[c]+b)%8] == h:
      b += e
    if board[(f[c]+b)//8][(f[c]+b)%8] == 0:
      if e == -7 and (f[c])%8 < (f[c]+b)%8 and (f[c]+b) >= 0: #右上
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append(f[c]+b)
      elif e == 7 and (f[c])%8 > (f[c]+b)%8 and (f[c]+b) <= 63: #左下
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append(f[c]+b)
      elif e == -9 and (f[c])%8 > (f[c]+b)%8 and (f[c]+b) >= 0: #左上
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append(f[c]+b)
      elif e == 7 and (f[c])%8 < (f[c]+b)%8 and (f[c]+b) <= 63: #右下
        board[(f[c]+b)//8][(f[c]+b)%8] = i
        g.append(f[c]+b)

    
  
def show():
 for a in board:
  print(" ".join(str(b) for b in a))
  
def show_color():
  table = {
    2:"●",
    1:"○",
    3:"×",
    0:"□"
  }
  for a in board:
    print(" ".join(table[b] for b in a))

  
def okerubasyo():
  w = input(置ける場所を指定してください)
  if w in black_okeru:
    board[(w)//8][(w)%8] = 2

def bot():
  if len(white_okeru) >= 1:
   w = random.choice(white_okeru)
   board[(w)//8][(w)%8] = 1






    


print(black)
print(white)
for i in range(10):
 show_color()
 kuro_okeru()
 okerubasyo()
 shiro_okeru()
 bot()


