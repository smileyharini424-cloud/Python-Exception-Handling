# Python Exception Handling

## Explanation

This program demonstrates how Python handles runtime errors using exception handling. It uses `try`, `except`, `else`, and `finally` blocks to safely perform division and handle invalid input.

## Problem Statement

Write a Python program that accepts two numbers from the user and performs division. Handle errors such as entering non-numeric values and division by zero without terminating the program unexpectedly.

## Features

* Accepts user input
* Performs division
* Handles invalid numeric input
* Handles division by zero
* Uses `try`, `except`, `else`, and `finally`

## How It Works

1. The program asks the user to enter two numbers.
2. The `try` block attempts to convert the input into numbers and perform division.
3. The `except` block handles errors.
4. The `else` block executes when no exception occurs.
5. The `finally` block executes whether an exception occurs or not.

## Technologies Used

* Python 3
* Exception Handling

## Program Flow

Start → Input Numbers → Try Operation → Check for Exception → Display Result/Error → Finally → End

## Sample Input

```text
Enter first number: 20
Enter second number: 5
```

## Sample Output

```text
Result: 4.0
Program execution completed.
```

## Key Learning

* `try` is used for code that may cause an exception.
* `except` handles exceptions.
* `else` executes when no exception occurs.
* `finally` always executes.
* Exception handling makes programs safer and more reliable.

## File Location

```text
Python-Exception-Handling/exception_handling.py
```

## Repository Structure

```text
Python-Exception-Handling/
│
├── exception_handling.py
└── README.md
```

## Author

V.Harini
