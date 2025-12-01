# ClydeBank Coffee Shop Simulator 4000

A Python-based business simulation game that demonstrates core programming concepts through interactive gameplay. Players manage a coffee shop by making daily business decisions including pricing, inventory management, and advertising spend.

## Project Overview

This project showcases Python fundamentals through a practical, real-world application. The simulator implements a complete game loop with user interaction, data management, error handling, and dynamic calculations based on player choices and randomized conditions.

## Technical Skills Demonstrated

**Core Python Concepts:**
- Data structures (lists, dictionaries, strings, numbers)
- Control flow (loops, conditionals, boolean logic)
- Functions and code organization
- Error handling with try/except blocks
- Module imports and random number generation
- User input validation and type conversion
- String formatting and console output

**Programming Practices:**
- Clean, readable code with meaningful variable names
- Input validation and error handling
- Iterative development tracked through Git commits
- Structured problem-solving and algorithmic thinking

## How to Run

### Prerequisites

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Game

```bash
python main.py
```

The game will prompt you for your name and coffee shop name, then begin the daily simulation loop where you make business decisions.

### Running Tests

Execute the test suite:

```bash
python -m unittest coffee_shop_simulator_tests.py
```

Or with verbose output:

```bash
python -m unittest coffee_shop_simulator_tests.py -v
```

Tests are run automatically on push and pull requests via GitHub Actions (see `.github/workflows/ci.yml`).

## Project Structure

- `main.py` - Project entry point; starts the coffee shop simulator
- `coffee_shop_simulator.py` - Core simulator and game logic using NumPy for temperature distribution
- `coffee_shop_simulator_tests.py` - Unit tests covering game logic, sales calculations, and edge cases
- `README.md` - Project documentation
- `LICENSE` - Copyright and licensing information
- `requirements.txt` - Project dependencies (NumPy 2.0)
- `.github/workflows/ci.yml` - GitHub Actions workflow for continuous integration

## Learning Journey

This project was developed following _Python QuickStart Guide: The Simplified Beginner's Guide to Python Programming using Hands-on Projects and Real-World Applications_ by Robert Oliver. Each commit in the repository corresponds to a specific chapter, providing a traceable progression of Python knowledge acquisition.

### Curriculum Coverage

**Part 1 - Getting Started with Python**
- Chapter 1: Getting to Know Python
- Chapter 2: Understanding Python Data Structures
- Chapter 3: Controlling Program Flow
- Chapter 4: Handling Errors

**Part 2 - Functions and Classes**
- Chapter 5: Creating Reusable Tasks with Functions
- Chapter 6: Classes
- Chapter 7: Inheritance and Design Patterns
- Chapter 8: Saving Time with DataClasses
- Chapter 9: Reusing Code with Modules and Packages

**Part 3 - Python in Action**
- Chapter 10: Advanced Strings
- Chapter 11: Math in Python
- Chapter 12: Input and Output
- Chapter 13: The Internet
- Chapter 14: Debugging Python Code

**Part 4 - Advanced Python**
- Chapter 15: Developing Websites
- Chapter 16: Interfacing with Sqlite
- Chapter 17: Test-Driven Development
- Chapter 18: Managing Your Code with Git
- Chapter 19: The Junk Drawer
- Chapter 20: Optimizing Python
- Chapter 21: What's Next?
