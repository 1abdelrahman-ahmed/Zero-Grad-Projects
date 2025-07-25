def show_levels():
  print('''
╔══════════════════════════════════════════════════════╗
║                     ▪[GAME LEVELS]▪                  ║
╠══════════════════════════════════════════════════════╣
║ (1) Easy           ║ 📏 Range  : [1 - 10]           ║
║                    ║ 🎯 Trials : 3                  ║
╠══════════════════════════════════════════════════════╣
║ (2) Intermediate   ║ 📏 Range  : [1 - 100]          ║
║                    ║ 🎯 Trials : 7                  ║
╠══════════════════════════════════════════════════════╣
║ (3) Hard           ║ 📏 Range  : [1 - 1000]         ║
║                    ║ 🎯 Trials : 15                 ║
╚══════════════════════════════════════════════════════╝
''')

def game_level_choice():
  print('''
Enter the game level:
  ➤ (1) Easy
  ➤ (2) Intermediate
  ➤ (3) Hard
''')
  game_level = input()
  return game_level

def set_game_settings(game_level):
  level_details = {
      '1': [10, 3],
      '2': [100, 7],
      '3': [1000, 15],
  }
  limits = level_details[game_level][0]
  n_trials = level_details[game_level][1]
  return limits, n_trials

import random
def start_play(limits, n_trials):
  num = random.randint(1, limits)
  trials = 0
  while trials < n_trials:
    trials += 1
    x = int(input('🎯 Guess the hidden number: '))
    if x == num:
      print(f'🎉 Congratulations! You got it in {trials} trials! 🏆')
      return
    elif x < num:
      print('❌ Nope, try a higher number!')
    else:
      print('❌ Nope, try a lower number!')
  print(f'😔 Oh no! You\'ve run out of trials. The number was {num}.\n🔄 Try again to beat the game! 💪')

def play():
  show_levels()
  game_level = game_level_choice()
  limits, n_trials = set_game_settings(game_level)
  start_play(limits, n_trials)

if __name__ == "__main__":
  play()