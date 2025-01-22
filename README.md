[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: Apache-2-License](https://img.shields.io/badge/Licence-Apache--2--Licence-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-yellow.svg)](https://www.linux.org/)
[![Quadratic Equation Test](https://github.com/CSC510-Group13/HW01/actions/workflows/test.yml/badge.svg)](https://github.com/CSC510-Group13/HW01/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/CSC510-Group13/HW01/badge.svg?branch=main)](https://coveralls.io/github/CSC510-Group13/HW01?branch=main)


# HW 1 - Solving Quadratic Equation

## Overview
This Homework uses a Python program to solve quadratic equation of the form:

$$ ax^2 + bx + c = 0 $$

where `a`, `b`, and `c` are real numbers, and `a` is not equal to 0. The program will calculate the roots of the quadratic equation using the quadratic formula:

$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

The program addresses all potential cases:  
- Two unique real roots  
- A single real root (repeated root)  
- No real roots (resulting in complex roots)

## Objectives

1. Add a function in `myfile.py` to compute the roots of a quadratic equation.  
2. Account for special cases, such as:  
   - When coefficient `a` equals zero (resulting in a linear equation, which this version does not handle).  
   - A negative discriminant ($b^2 - 4ac$), which leads to complex roots.  
3. Create a separate test file to write test cases that verify the functionality of the solver.
   
## File Structure

- `myfile.py`: The myfile.py file contains the implementation of the quadratic equation solver.
- `test_myfile.py`: This is a separate test file containing test cases for validating the solver function using `pytest`.

## Getting Started

### Prerequisites

- Python 3.13
- `pytest` for running the test cases

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CSC510-Group13/HW01.git
   cd HW01
2. Install Dependencies: Install pytest for running test cases.

### Usage
To use the Quadratic Equation Solver, run the main program with the following command:
python3.13 myfile.py

Then, do the following to solve the quadratic equation

Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
The roots are: (2.0, 1.0)

To Check for Test Cases for the program, run pytest

### Contributing
We welcome contributions to the Quadratic Equation Solver! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request. Or you can also open an issue to share and discuss your suggestions.
