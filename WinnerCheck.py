import colorama
from BoardGeneration import XY, lineXY, guide, board
from colorama import init, Fore, Back, Style

def WinnerCheck() :
  global win
  win = 0
  
  #CHECKING ROWS
  for key in board :
    p1Check = ['X'] * (lineXY - 1)
    p2Check = ['O'] * (lineXY - 1)
    if board[key] == p1Check :
      win = 1
    if board[key] == p2Check : 
      win = 2

  #CHECKING COlLUMS

  for i in range(1,lineXY) :
    p1Chance = 0
    p2Chance = 0
    for key in board : 
      if board[key][i-1] == "X" :
        p1Chance = p1Chance + 1
        if p1Chance == lineXY - 1 :
          win = 1
      if board[key][i-1] == "O" :
        p2Chance = p2Chance + 1
        if p2Chance == lineXY - 1 :
          win = 2
  
  

  #Checking FIRST DIAGONAL (LeftTop to RightBottom (NEGATIVE GRADIENT)) \
  p1Chance = 0
  p2Chance = 0
  for i in range(1,lineXY) :
    if board["line{0}".format(i)][i-1] == "X" :
      p1Chance = p1Chance + 1
    if board["line{0}".format(i)][i-1] == "O" :
      p2Chance = p2Chance + 1 
  if p1Chance == lineXY - 1 :
    win = 1
  if p2Chance == lineXY - 1 :
    win = 2
    
  #Checking SECOND DIAGONAL (RightTop to LeftBottom (POSITIVE GRADIENT)) \
  p1Chance = 0
  p2Chance = 0
  for i in range(1,lineXY) :
    if board["line{0}".format(i)][lineXY-i-1] == "X" :
      p1Chance = p1Chance + 1
    if board["line{0}".format(i)][lineXY-i-1] == "O" :
      p2Chance = p2Chance + 1 
  if p1Chance == lineXY - 1 :
    win = 1
  if p2Chance == lineXY - 1 :
    win = 2


    
        

def Victory() :
  # If a victory is detected, it will run this
  global win
  print(Fore.CYAN + "\nGAME FINISHED!")
  for i in range(1,lineXY) :
    for i2 in range(1,lineXY) : 
      print(end=Style.RESET_ALL + "")
      print(end=board["line{0}".format(i)][i2-1])
      print(end=" ")
    print(" ")
  
  print(end=Style.RESET_ALL + "\nThe winner is ")
  

  #Checks if player 1 won or player 2
  if win == 1 :
    print(Fore.RED + Style.BRIGHT + "Player 1")
  if win == 2 :
    print(Fore.BLUE + Style.BRIGHT + "Player 2")
