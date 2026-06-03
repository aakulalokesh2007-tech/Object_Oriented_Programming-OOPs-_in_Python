# Multiple Inheritance and MRO

This repository contains a Python script demonstrating **Multiple Inheritance** and how Python resolves the famous "Diamond Problem" using **Method Resolution Order (MRO)**.

## Description

The script sets up a diamond-shaped inheritance structure:
- A base class `demo`.
- Two intermediate classes `c` and `d`, which both inherit from `demo`.
- A final class `newdemo`, which inherits from *both* `c` and `d`.

All four classes have a method named `dis()`. This code demonstrates how Python's built-in `super()` function elegantly navigates this complex hierarchy without repeating method calls or skipping classes.

This script continues the experimental convention of using the positional argument `me` instead of `self`.

## Code Overview

- `class demo`: The base class at the top of the diamond.
- `class c(demo)` & `class d(demo)`: The middle tier of the diamond. Their `super().dis()` calls dynamically route based on the MRO of the calling object.
- `class newdemo(c, d)`: The bottom of the diamond. Inherits from multiple classes.
- `a = newdemo()`: Instantiates the bottom-level class to trigger the chain.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### How to Run
1. Clone this repository or download the source code file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:
