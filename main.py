from variables import *
from BoardGeneration import *
import colorama
from colorama import init, Fore, Back, Style
init()

# Starting Hellos
print(Fore.CYAN + "Welcome to TicTacToe!")
print(Style.RESET_ALL + "\nSelect your board dimensions\n" + Style.DIM + "(i.e 1x1 2x2, 9x9) \n",  )

#Generation of board begins
BoardGen()
from BoardGeneration import XY

#Game begins
print("\n" + Fore.CYAN+ Style.BRIGHT + "GAME STARTED!")
for i in range(1,XY+1) :
  from UserInput import *
  DisplayBoard()
  UserInput()
  from WinnerCheck import *
  WinnerCheck()
  from WinnerCheck import win
  if win == 1 or win == 2 :
    Victory()
    break
from WinnerCheck import win
# DRAW
if win == 0 :
  # If no victory was detected and board is filled, its a draw
  print(Fore.CYAN + "\nGAME FINISHED!")
  for i in range(1,lineXY) :
    for i2 in range(1,lineXY) : 
      print(end=Style.RESET_ALL + "")
      print(end=board["line{0}".format(i)][i2-1])
      print(end=" ")
    print(" ")
  
  print(end=Style.RESET_ALL + "\nThis game is a ")
  print(Fore.BLUE + "DRAW")
    
  



