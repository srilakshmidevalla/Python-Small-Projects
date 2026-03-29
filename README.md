# Python Small Projects

A collection of beginner-friendly Python projects and exercises designed to practice and learn core Python concepts.

## 📁 Project Structure

### 📚 **exercises.py** - 10 Practice Exercises
A collection of 10 fundamental Python exercises with built-in solutions.

**Exercises included:**
1. **FizzBuzz** - Print numbers 1-30, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz"
2. **Reverse a String** - Reverse input string using slicing
3. **Count Vowels** - Count vowel occurrences in text
4. **Find Largest Number** - Find max value without using built-in max() function
5. **Palindrome Check** - Determine if a word reads the same forwards and backwards
6. **Calculate Factorial** - Compute n! without using math.factorial()
7. **Flatten Nested List** - Convert multi-level list to single-level list
8. **Word Frequency** - Count word occurrences and sort by frequency
9. **ATM Simulation** - Basic bank operations (deposit, withdraw, check balance)
10. **Caesar Cipher** - Encrypt/decrypt text using character shifting

**Run:** `python exercises.py`

---

### 🎮 **project_01_number_guessing.py** - Number Guessing Game
An interactive guessing game with multiple difficulty levels and helpful feedback.

**Features:**
- 3 difficulty levels:
  - Easy: 1-50 range, 10 guesses
  - Medium: 1-100 range, 7 guesses
  - Hard: 1-500 range, 5 guesses
- Smart feedback ("Way too low/high" or "A bit low/high")
- Performance rating system
- Play multiple rounds
- Error handling for invalid input

**Run:** `python project_01_number_guessing.py`

---

### 📝 **project_02_todo_list.py** - Command-Line To-Do List
A persistent task management application with JSON file storage.

**Features:**
- Add new tasks
- List all tasks with completion status
- Mark tasks as complete
- Delete tasks
- Clear all completed tasks
- Data persists between sessions (stored in todos.json)
- User-friendly menu interface

**Menu Commands:**
- `a` - Add a new task
- `l` - List all tasks
- `c` - Mark task as complete
- `d` - Delete a task
- `x` - Clear all completed tasks
- `q` - Quit

**Run:** `python project_02_todo_list.py`

---

### 🧮 **project_03_calculator.py** - Calculator with History
A command-line calculator with history tracking and special operations.

**Features:**
- Basic arithmetic operations: +, -, *, /
- Support for parentheses and complex expressions
- Operation history (last 10 calculations)
- Special operations:
  - Square root (sq)
  - Power/Exponentiation (pow)
  - Percentage calculations (pct)
- Safe expression evaluation
- Error handling (division by zero, invalid input)

**Menu Commands:**
- Type any math expression: `2+3`, `10*5`, `(4+2)/3`
- `h` - View calculation history
- `s` - Access special operations
- `q` - Quit

**Run:** `python project_03_calculator.py`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/srilakshmidevalla/Python-Small-Projects.git
   cd Python-Small-Projects
   ```

2. Run any project:
   ```bash
   python exercises.py
   python project_01_number_guessing.py
   python project_02_todo_list.py
   python project_03_calculator.py
   ```

---

## 📖 Learning Concepts

These projects cover essential Python fundamentals:

| Concept | Project |
|---------|---------|
| Loops & Conditionals | exercises.py, project_01 |
| Functions | All projects |
| Lists & Dictionaries | exercises.py, project_02, project_03 |
| File I/O | project_02 |
| String Manipulation | exercises.py, project_03 |
| Error Handling | All projects |
| User Input/Output | All projects |
| JSON Data Format | project_02 |
| Random Numbers | project_01 |

---

## 💡 Tips for Learning

- **Exercises**: Try solving each exercise *before* looking at the solution
- **Games**: Modify difficulty levels or add new features
- **To-Do List**: Experiment with adding categories or priority levels
- **Calculator**: Extend with more operations or save history to a file

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Feel free to fork this repository and add more projects or improvements!