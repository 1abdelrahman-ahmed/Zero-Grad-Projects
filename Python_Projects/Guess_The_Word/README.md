# 🎯 Word Guess Game

A simple Python project where the user tries to guess a hidden word letter by letter before running out of attempts.

---

## 📋 Project Description

### 🔹 First: Word Selection

The computer selects a random word from these categories:

- **Fruits** 🍎: apple, banana, orange, etc.
- **Animals** 🦁: lion, elephant, tiger, etc.
- **Colors** 🌈: red, blue, green, etc.
- **9 other categories** with common words

---

### 🔹 Second: Game Setup

- A random word is selected using Python's `random` module
- Number of allowed attempts: `2 × word length`
- Hidden word displayed as underscores (e.g., "_ _ _ _" for "lion")

---

### 🔹 Finally: Play the game!

- The user guesses letters one by one
- Game logic:
  - ✅ If the letter is correct:
    - Letter is revealed in its position(s)
    - `Correct guess ✅ Nice! "{letter}" is in the word!`
  - ❌ If the letter is wrong:
    - Attempt counter decreases
    - `Wrong guess ❌ Oops! "{letter}" is wrong.`
  - 🎉 If complete word is guessed:
    - `You win! 🎉 YAY! The word was "{word}"!`
  - 😢 If attempts run out:
    - `You lose 😢 Game over! The word was "{word}"`

---

## ▶️ How to Run

```bash
python guess_the_word.py
```

No installation needed — just run it using Python 3.x.

---

## 🧪 Example Output

```
🌟 Welcome to Word Guess! 🌟
Guess a letter (a-z): a
Correct guess ✅
Nice! "a" is in the word!
_ a _ _ 
Guess a letter (a-z): z
Wrong guess ❌
Oops! "z" is wrong.
_ a _ _
```

---

## 🛠️ Built With

- Python 3
- Standard Library only

---

## 📄 License

This project is open-source and free to use.