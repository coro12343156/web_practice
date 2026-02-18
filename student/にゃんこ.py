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
      black.append(left+8*a)
     left += 1
  for a in range(8):
   left = 0
   for i in board[a]:
     if i == 1:
      white.append(left+8*a)
     left += 1
  for c in range(len(black)):  #right
   b = 0
   while board[(black(c)+b)//8][(black(c)+b)%8] == 1 :
    if (black(c)+b)%8 <7:
     b += 1
    else:
     break
   if board[(black(c)+b)//8][(black(c)+b)%8] == 0 :
    board[(black(c)+b)//8][(black(c)+b)%8] = 3
  for c in range(len(black)):  #left
   b = 0
   while board[(black(c)-b)//8][(black(c)-b)%8] == 1 :  
    if (black(c)-b)%8 >0:
     b += 1
    else:
     break
   if board[(black(c)-b)//8][(black(c)-b)%8] == 0 :
    board[(black(c)-b)//8][(black(c)-b)%8] = 3
   
   
    
     
      
     
    


okeru()
print(black)
print(white)
   
    
   


