# 🧠 Python Quiz Game

A simple **command-line Quiz Game** built with Python using **Object-Oriented Programming (OOP)** principles.

The game presents a series of **True/False questions** to the player. The player answers each question, and the program checks whether the answer is correct while keeping track of the score.

This project demonstrates **Python classes, loops, object interaction, and modular programming**.

---

## Features

- Interactive command-line quiz
- True/False question system
- Real-time answer validation
- Score tracking system
- Displays correct answer when user is wrong
- Final score display at the end of the quiz
- Modular code structure using multiple Python files

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Command Line Interface (CLI)

---

## Project Structure

```bash
python-quiz-game/
│
├── main.py              # Runs the quiz game
├── quiz_brain.py        # Handles quiz logic and scoring
├── question_model.py    # Defines the Question class
├── data.py              # Contains quiz questions data
│
└── README.md
```

---

## Requirements

Before running the game, make sure you have **Python 3.x installed**.

Download Python from:

https://www.python.org/downloads/

To check if Python is installed:

#### Windows

```bash
python --version
```

#### Mac / Linux

```bash
python3 --version
```

---

## How to Run the Game

Follow these steps to run the quiz game on your computer.

### Clone the Repository

```bash
git clone https://github.com/adebayoadesugba/python-quiz-game.git
```

### Navigate into the Project Folder

```bash
cd python-quiz-game
```

### Run the Game

#### Windows

```bash
python main.py
```

#### Mac / Linux

```bash
python3 main.py
```

---

## How the Game Works

1. The program loads quiz questions from the **data file**.
2. Each question is converted into a **Question object**.
3. The **QuizBrain class** manages the quiz logic.
4. The player answers **True or False** questions.
5. The program checks if the answer is correct.
6. The score updates after each question.
7. At the end of the quiz, the **final score is displayed**.

Example:

```
Q.1: The sky is blue (True/False): True
You Got it Right 👍
Your Current Score Is: 1/1
```

---

## Key Concepts Demonstrated

This project demonstrates several important Python concepts:

- Classes and Objects
- Object-Oriented Programming (OOP)
- Lists and Loops
- User Input Handling
- Modular Programming
- File Organization in Python Projects

---

## Future Improvements

Possible upgrades for this project:

- Add multiple choice questions
- Add timer for questions
- Add graphical interface using Tkinter
- Store high scores
- Randomize question order
- Load questions from an API

---

## Author

**Adebayo Adesugba**

Full Stack Developer  
Python | JavaScript | React | Node.js | AI Development

---

### If you like this project, feel free to **star the repository** on GitHub.
