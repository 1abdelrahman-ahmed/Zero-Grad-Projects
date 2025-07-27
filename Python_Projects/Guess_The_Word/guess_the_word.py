import random
allowed_tries = 0

def choose_word():
  word_topics = {
    "fruits": ["apple", "banana", "orange", "grape", "mango", "peach", "kiwi", "strawberry"],
    "animals": ["lion", "elephant", "tiger", "giraffe", "zebra", "monkey", "kangaroo", "panda"],
    "colors": ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"],
    "countries": ["egypt", "canada", "brazil", "germany", "japan", "india", "france", "spain"],
    "sports": ["football", "basketball", "tennis", "cricket", "volleyball", "hockey", "swimming"],
    "programming": ["python", "java", "flutter", "variable", "loop", "function", "class", "debug"],
    "school subjects": ["math", "science", "history", "geography", "english", "chemistry", "physics", "art"],
    "jobs": ["doctor", "teacher", "engineer", "nurse", "pilot", "chef", "lawyer", "police"],
    "body parts": ["head", "shoulder", "knee", "eye", "nose", "ear", "mouth", "hand"],
    "weather": ["rain", "sunny", "cloudy", "windy", "storm", "snow", "fog", "thunder"]
  }
  topic = random.choice(list(word_topics.keys()))
  word = random.choice(word_topics[topic])
  global allowed_tries
  allowed_tries = 2 * len(word)
  return word

def display_word(word, guessed_letters):
  for letter in word:
    if letter in guessed_letters:
      print(letter, end='')
    else:
      print('_', end='')

def start_message():
  print('🌟 Welcome to Word Guess! 🌟')
  print(f'''How to play:
1.I pick a word (like "cat" 🐱 or "book" 📖).
2.You guess letters one by one.
3.You get {allowed_tries} tries!
  ''')

def guess_word():
  word = choose_word()
  guessed_letters = set()
  tries = 0
  start_message()
  while True:
    guess = input('Guess a letter (a-z): ')
    tries += 1
    if guess in word:
      print('Correct guess ✅')
      print(f'Nice! "{guess}" is in the word!')
      guessed_letters.add(guess)
    else:
      print('Wrong guess ❌')
      print(f'Oops! "{guess}" is wrong.')
    display_word(word, guessed_letters)
    if len(guessed_letters) == len(set(word)):
      print(f'You win! 🎉:')
      print(f'YAY! The word was "{word}"! You won with {allowed_tries - tries} tries left! 🏆')
      break
    elif tries == allowed_tries:
      print('You lose 😢:')
      print(f'Game over! The word was "{word}". Try again! ♻️')
      break

if __name__ == "__main__":
  guess_word()