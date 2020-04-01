def win_bad(matrix):
  win_row = []
  win_col = []
  win_backslash = []
  win_forwardslash = []
  general_i = 0
  win = False

  # Check Rows
  for i in range(len(matrix)):
    win_row.append(True)
    for j in range(len(matrix[0]) - 1):
      general_i += 1
      if matrix[i][j] != matrix[i][j + 1]:
        win_row[i] = False

  # Check Cols
  for j in range(len(matrix)):
    win_col.append(True)
    for i in range(len(matrix) - 1):
      general_i += 1
      if matrix[i][j] != matrix[i + 1][j]:
        win_col[j] = False

  # Diag
  win_backslash.append(True)
  win_forwardslash.append(True)
  for i in range(len(matrix) - 1):
    general_i += 1
    if matrix[i][i] != matrix[i + 1][i + 1]:
      win_backslash[0] = False
    general_i += 1
    if matrix[len(matrix) - i - 1][i] != matrix[len(matrix) - i - 2][i + 1]:
      win_forwardslash[0] = False

  wins = [win_row, win_col, win_backslash, win_forwardslash]
  for wn in wins:
    for result in wn:
      if result:
        win = True
  print(general_i)
  return win

# Check to see if the player has won
def win(matrix, looking):
  win_row = []
  win_col = []
  win_backslash = []
  win_forwardslash = []
  general_i = 0
  win = False

  # Check Rows
  for i in range(len(matrix)):
    win_row.append(True)
    for j in range(len(matrix[i])):
      general_i += 1
      if matrix[i][j] != looking:
        win_row[i] = False

  # Check Cols
  for j in range(len(matrix)):
    win_col.append(True)
    for i in range(len(matrix)):
      general_i += 1
      if matrix[i][j] != looking:
        win_col[j] = False

  # Diag
  win_backslash.append(True)
  win_forwardslash.append(True)
  for i in range(len(matrix)):
    general_i += 1
    if matrix[i][i] != looking:
      win_backslash[0] = False
    general_i += 1
    if matrix[len(matrix) - i - 1][i] != looking:
      win_forwardslash[0] = False

  wins = [win_row, win_col, win_backslash, win_forwardslash]
  # print(wins)
  for wn in wins:
    for result in wn:
      if result:
        win = True
  # print(general_i)
  return win


"""
# Losing games
lose_1 = [[1,3,0], [0,2,1], [2,0,1]] # random
lose_2 = [[1,7,1], [2,1,1], [4,2,6]] # wrong up down diag

# Winning Games
win_1 = [[1,1,1], [0,2,1], [2,0,1]] # same row
win_2 = [[1,7,1], [0,2,1], [2,2,2]] # same row
win_3 = [[1,7,1], [1,2,1], [1,2,2]] # same col
win_4 = [[1,7,1], [2,1,1], [5,2,1]] # down diag
win_5 = [[1,7,1], [2,1,1], [1,2,6]] # up diag
"""
# Test
"""
print(win(lose_1, 1))

print(win(lose_2, 1))

print(win(win_1, 1))
print(win(win_2, 2))
print(win(win_3, 1))
print(win(win_4, 1))
print(win(win_5, 1))
"""
# making the game
def board(n):
  bd = []
  for i in range(n):
    holder = []
    for j in range(n):
      holder.append(0)
    bd.append(holder)
  return bd

def ttt_print(board):
  for i in range(len(board)):
      print(board[i])

def history(new, lst):
  for item in lst:
    if new == item:
      return True


# print(board(3))
# playing the game
def game():
  size = input("Size of the Board: ")
  player_numbers_str = input("Number of Players? ")
  player_numbers = int(player_numbers_str)
  ttt_board = board(int(size))
  cur_player = 1
  ttt_print(ttt_board)
  past = []
  # Main Game loop, I suppose
  while True:
    print("Player {} it is your turn".format(cur_player))
    location_str = input("Row, Col location of turn: ")

    try:
      location = [int(s) for s in location_str.split(',')]
      if history(location, past):
          print("Already something there.\nTry again.")
          continue
      past.append(location)
      ttt_board[location[0]][location[1]] = cur_player
    except ValueError:
      print("NO STRINGS. Bro this is TickTackToe.\nTry Again")
      continue
    except IndexError:
      print("Gotta be in bounds.\nTry Again.")
      continue
    ttt_print(ttt_board)

    if win(ttt_board, cur_player):
      break

    cur_player += 1
    if cur_player > player_numbers:
      cur_player = 1
  print("game is done!")
  print(f"{cur_player} won the game")
  return

game()
