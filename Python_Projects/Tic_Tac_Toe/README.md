# ❌⭕ Tic Tac Toe

A simple two-player Tic Tac Toe game built with Python, played in the terminal.

---

## 📋 Project Description

This is a turn-based game where two players take turns marking a 3×3 grid with `X` and `O`. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) wins the game.

---

## 🧩 How the Game Works

### 🔹 Step 1: Player Setup

- The program randomly assigns `X` or `O` to each player at the start.

### 🔹 Step 2: Game Board

- The board is displayed with numbers 1–9 indicating the available cells.
- Players input a number to choose the cell where they want to place their mark.

### 🔹 Step 3: Turns

- Players take turns to input their move.
- The game displays the board after each move.

### 🔹 Step 4: Win or Draw

- If a player aligns 3 marks in a row, column, or diagonal → they win! 🎉
- If all cells are filled without a winner → it's a draw.

---

## ▶️ How to Run

```bash
python tic_tac_toe.py
```

Make sure you're using Python 3.x — no external libraries required.

---

## 🧪 Example Output

```
1	2	3	
4	5	6	
7	8	9	

🎮 Player 1's turn (X)
➤ Enter a number (1-9) for an empty cell: 5

1	2	3	
4	X	6	
7	8	9	
...
🎉 Congratulations! Player 1 (X) wins! 🏆
```

---

## 🛠️ Built With

- Python 3
- Only standard library (`random` module)

---

## 📄 License

This project is open-source and free to use.
