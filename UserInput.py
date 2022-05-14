import colorama
from BoardGeneration import XY, lineXY, guide, board
from colorama import init, Fore, Back, Style
player = 0
turn = 0
def UserInput() :
  global mark
  global guide
  global XY
  global board
  global lineXY
  global point
  global turn
  loop = 1
  while loop != 0 : 
    #  This decides if its player 1 or 2's turn
    if turn % 2 != 0 :
      pcolour = Fore.BLUE + Style.BRIGHT
      mark = "O"
      player = "2: "
    else :
      pcolour = Fore.RED + Style.BRIGHT
      mark = "X"
      player = "1: "
    print(end="\n" + pcolour + "Player " + player)

    # Getting input from the user
    point = input(Style.RESET_ALL + "Place your point: ")

    # Validating the input
    try: 
      int(point) > XY or int(point) < 1
      result = True
    except ValueError :
      result = False

    if result == False :
      print(Fore.RED + Style.BRIGHT + "Invalid input, try again")
      
    elif int(point) > XY or int(point) < 1 :
      print(Fore.RED + Style.BRIGHT + "Point not in range, try again")

      # It will then find where the point is located on the board
    else : 
      for key in guide :
        for num in guide[key] :
          if point == str(num) :
            index = (guide[key].index(num))

            # It checks here if the point is empty
            # If so, it will activate the next player
            if board[key][index] == '-' :
              board[key][index] = mark
              turn = turn + 1
              loop = 0

            # If not then repeat
            else :
              print(Fore.RED + Style.BRIGHT + "Point is taken, try a different spot")
  print("--------------------------------------------------------------------------------")

