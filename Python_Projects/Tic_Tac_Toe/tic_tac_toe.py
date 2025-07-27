import random

def create_empty_board():
  board = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
  for row in board:
    for col in row:
      print(col, end='\t')
    print('\n')

def show_board(board):
  for col in board:
    for row in col:
      print(row, end='\t')
    print('\n')

def set_players():
  players = ['X', 'O']
  p1 = random.randint(0, 1)
  p2 = p1 - 1
  return players[p1], players[p2]

def take_input(board, player):
  while True:
    x = input('➤ Enter a number (1-9) for an empty cell: ')
    if (not x.isdigit()) or (int(x) < 1) or (int(x) > 9):
      print('❌ Invalid input! Please enter a number (1-9).')
      continue
    x = int(x)
    x -= 1
    row = x // 3
    col = x % 3
    if not board[row][col].isdigit():
      print('❌ This cell is already taken! Try again.')
      continue
    board[row][col] = player
    show_board(board)
    return

def check_full_board(board):
  for row in board:
    for col in row:
      if col.isdigit():
        return False
  return True

def check_win(board):
  for row in board:
    st = set()
    for col in row:
      st.add(col)
    if len(st) == 1:
      return True
  d1 = set()
  d2 = set()
  for col in range(0, 3):
    st = set()
    for row in range(0, 3):
      st.add(board[row][col])
      if row == col:
        d1.add(board[row][row])
        d2.add(board[2-row][row])
    if len(st) == 1:
      return True
  return len(d1) == 1 or len(d2) == 1

def play():
  player1, player2 = set_players()
  print(f'''
🎮 Welcome to Tic-Tac-Toe! 🎲
   ➤ Player 1: {player1}
   ➤ Player 2: {player2}
🔥 Get ready for the challenge! 💪
''')
  board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
  show_board(board)
  players = [player1, player2]
  for i in range(9):
    idx = i % 2
    player = players[idx]
    print(f'🎮 Player {idx+1}\'s turn ({player})')
    take_input(board, player)
    if check_win(board):
      print(f'🎉 Congratulations! Player {idx+1} ({player}) wins! 🏆')
      return
    if check_full_board(board):
      print('😔 It\'s a draw! No winner this time.')
      return

if __name__ == '__main__':
  play()