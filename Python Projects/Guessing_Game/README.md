# 🎮 Guessing Game

A simple Python project where the user tries to guess a hidden number based on the selected difficulty level.

---

## 📋 Project Description

### 🔹 First: Set the game level

The user selects one of the three difficulty levels:

- **(1) Easy**
  - Range: [1 - 10]
  - Number of trials: 3

- **(2) Intermediate**
  - Range: [1 - 100]
  - Number of trials: 7

- **(3) Hard**
  - Range: [1 - 1000]
  - Number of trials: 15

---

### 🔹 Second: Configure game settings

- A random number is generated within the selected range using Python's `random` module.
- Set the number of allowed trials based on the selected difficulty level.

---

### 🔹 Finally: Play the game!

- The user tries to guess the number.
- Game logic:
  - ✅ If the guess is correct:
    - `🎉 Congratulations! You got it in {trials} trial(s)`
  - ❌ If the guess is wrong:
    - If trials left: guide the user (try a higher/lower number)
    - If no trials left:
      - `😔 You've run out of trials. You Lose!`

---

## ▶️ How to Run

```bash
python project_(1)_guessing_game.py
```

No installation needed — just run it using Python 3.x.

---

## 🧪 Example Output

```
🎯 Guess the hidden number: 50
❌ Nope, try a higher number!
🎯 Guess the hidden number: 75
❌ Nope, try a lower number!
🎯 Guess the hidden number: 60
🎉 Congratulations! You got it in 3 trials!
```

---

## 🛠️ Built With

- Python 3
- Standard Library only

---

## 📄 License

This project is open-source and free to use.