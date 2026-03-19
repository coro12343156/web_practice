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
  rightandleft(-1)
  rightandleft(1)
  upanddown(-1)
  upanddown(1)
  naname(-7) #右上
  naname(7)  #左下
  naname(-9) #左上
  naname(9)  #右下

 
def rightandleft(e):
 for c in range(len(black)):  #右左
  b = 0
  while board[(black[c]+b)//8][(black[c]+b)%8] == 1 :
   b += e
  if (black[c]+b)%8 <= 7 and (black[c]-b)%8 >= 0:
     b -= e
  else:
     break
  if board[(black[c]+b)//8][(black[c]+b)%8] == 0:
    board[(black[c]+b)//8][(black[c]+b)%8] = 3

def upanddown(e):
 for c in range(len(black)): #上下
   b = 0
   while board[(black[c]+b)//8][(black[c]+b)%8] == 1:
    b += e 
    if black[c]-b<= -1 and black[c]+b >= 64:
     b -= e
    else:
     break
   if board[(black[c]+b)//8][(black[c]+b)%8] == 0:
    board[(black[c]+b)//8][(black[c]+b)%8] = 3
  
def naname(e):
 for c in range(len(black)): #斜め
  b = 0
  while board[(black[c]+b)//8][(black[c]+b)%8] == 1:
   b += e
  if black[c]-b>-1 and black[c]+b< 64 and (black[c]+b)%8 <= 7 and (black[c]-b)%8 >= 0:
    b -= e
  else:
   break
  if board[(black[c]+b)//8][(black[c]+b)%8] == 0:
     board[(black[c]+b)//8][(black[c]+b)%8] = 3


    
  
   
    
     
      
     
    


okeru()
print(black)
print(white)
print(board)
   
    
   


   
   
    

for c in range(len(black)): #上側置けるか
   b = 0
   while board[(black[c]+b)//8][(black[c]+b)%8] == 0:
    if black[c]-b>7:
     b -= 8
    else:
     break
   if board[(black[c]+b)//8][(black[c]+b)%8] == 0:
    board[(black[c]+b)//8][(black[c]+b)%8] = 3
for c in range(len(black)):   #下側置けるか
   b = 0
   while board[(black[c]+b)//8][(black[c]+b)%8] == 1:
    if black[c]+b< 56:
     b += 8
    else:
     break
    if board[(black[c]+b)//8][(black[c]+b)%8] == 0:
     board[(black[c]+b)//8][(black[c]+b)%8] = 3


    