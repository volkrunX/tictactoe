from variables import *
import colorama
from colorama import init, Fore, Back, Style

#Generating the board
def BoardGen() :
  global board
  global lineXY
  global guide
  global LineLength
  global XY

  #Getting users input and validating for the dimensions of the board
  dimensions = str.lower(input(Style.RESET_ALL + "Choice: "))
  if len(dimensions) != 3 :
    print(Fore.RED + Style.BRIGHT + "Invalid length, try again\n")
    BoardGen()  
  elif dimensions[0] != dimensions[2] :
    print(Fore.RED + Style.BRIGHT + "Your dimensions, must be equal (i.e 3x3), try again\n")
    BoardGen()  
  elif int(dimensions[0]) < 1 :
    print(Fore.RED + Style.BRIGHT + "Your dimensions, can not be less then 1x1, try again\n")
    BoardGen()
  elif dimensions[1] != "x" : 
    print(Fore.RED + Style.BRIGHT + "Format incorrect, try again\n")
    BoardGen()
  else :
    #If correct, two variables assigned for loops later
    lineXY = int(dimensions[0]) + 1
    # XY represents the number of possible turns
    XY = int(lineXY-1) * int(lineXY-1)
   
    # Generating each row, based on the users Y value, and X value
    for i in range(1,lineXY) :
      board["line{0}".format(i)] = ['-'] * (lineXY - 1) 
      
    # Generating the guide, 
    for i in range(1,lineXY) :
      LineGuide = []
      for i2 in range(1,lineXY) : 
        # Formulae to produce the guide
        LineGuide.append(str(i2+(lineXY-1) * (i-1)))
      guide["line{0}".format(i)] = LineGuide
      
    print("--------------------------------------------------------------------------------")

def DisplayBoard():
  global lines
  global lineXY
  global guide
  global board
  global LineLength

  # These two condtions are for formatting purposes only
  if lineXY % 2 != 0 :
    print(Style.RESET_ALL + "\nThis is your current board \t"+ (lineXY * "\t") + "THE GUIDE")
  else :
    print(Style.RESET_ALL + "\nThis is your current board \t" + (lineXY * "\t") + "THE GUIDE")

  # This prints each array for both the board and guide
  for i in range(1,lineXY) :
    for i2 in range(1,lineXY) : 
      print(end=board["line{0}".format(i)][i2-1])
      print(end=" ")
    print(end="\t\t\t\t\t\t\t")
    for i2 in range(1,lineXY) : 
      print(end="\t" + guide["line{0}".format(i)][i2-1])
      print(end=" ")
    print(end="\n")
    

