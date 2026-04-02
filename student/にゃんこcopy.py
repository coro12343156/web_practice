board = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,2,1,0,0,0],
         [0,0,0,1,2,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

black = []
white = []


def okeru():
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
  rightandleft(1) #右
  rightandleft(-1) #左
  upanddown(-8) #上
  upanddown(8) #下
  naname(-7) #右上
  naname(7)  #左下
  naname(-9) #左上
  naname(9)  #右下

 
def rightandleft(e):
 for c in range(len(black)):  #右左
  b = e # 一つ移動する
  if board[(black[c]+b)//8][(black[c]+b)%8] == 1: # 一つ移動した先は白？
    while board[(black[c]+b)//8][(black[c]+b)%8] == 1: # 白を抜けるまで進む
      b += e
    if board[(black[c]+b)//8][(black[c]+b)%8] == 0: # 今いる場所にコマは置かれてない？
      if e == 1 and (black[c])%8 < (black[c]+b)%8: # 右の条件
        board[(black[c]+b)//8][(black[c]+b)%8] = 3
      elif e == -1 and (black[c])%8 > (black[c]+b)%8: # 左の条件
        board[(black[c]+b)//8][(black[c]+b)%8] = 3


def upanddown(e):
 for c in range(len(black)): #上下
   b = e
   if board[(black[c]+b)//8][(black[c]+b)%8] == 1:
    while board[(black[c]+b)//8][(black[c]+b)%8] == 1:
      b += e 
    if board[(black[c]+b)//8][(black[c]+b)%8] == 0:
      if e == -8 and (black[c]+b) >= 0:
        board[(black[c]+b)//8][(black[c]+b)%8] = 3
      elif e == 8 and (black[c]+b) <= 63:
        board[(black[c]+b)//8][(black[c]+b)%8] = 3


def naname(e):
 for c in range(len(black)): #斜め
  b = e
  if board[(black[c]+b)//8][(black[c]+b)%8] == 1:
    while board[(black[c]+b)//8][(black[c]+b)%8] == 1:
      b += e
    if board[(black[c]+b)//8][(black[c]+b)%8] == 0:
      if e == -7 and (black[c])%8 < (black[c]+b)%8 and (black[c]+b) >= 0: #右上
        board[(black[c]+b)//8][(black[c]+b)%8] = 3
      elif e == 7 and (black[c])%8 > (black[c]+b)%8 and (black[c]+b) <= 63: #左下
        board[(black[c]+b)//8][(black[c]+b)%8] = 3
      elif e == -9 and (black[c])%8 > (black[c]+b)%8 and (black[c]+b) >= 0: #左上
        board[(black[c]+b)//8][(black[c]+b)%8] = 3
      elif e == 7 and (black[c])%8 < (black[c]+b)%8 and (black[c]+b) <= 63: #右下
        board[(black[c]+b)//8][(black[c]+b)%8] = 3

    
  
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
    

okeru()
print(black)
print(white)
show_color()

