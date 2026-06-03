# Python OOP Basics: Encapsulation and Private Attributes

This repository contains a Python script demonstrating the fundamental Object-Oriented Programming (OOP) concept of **Encapsulation**. It shows how to define public and private attributes within a class to protect internal data.

## Description

In Python, there is no strict `private` keyword like in Java or C++. Instead, Python relies on naming conventions. By prefixing an attribute with double underscores (e.g., `__color`), Python applies a mechanism called **Name Mangling**. 

This script defines a `food` class to illustrate this concept. It shows that while private variables can be easily accessed and utilized by methods *inside* the class, they are hidden from direct access *outside* the class.

## Code Overview

- `class food`: The main class representing a generic food item.
- `__init__(self, fruit, color)`: The constructor method. 
  - `self.fruit`: A **public** attribute that can be accessed from anywhere.
  - `self.__color`: A **private** attribute protected by name mangling.
- `show(self)`: An instance method that safely accesses both the public and private attributes to print their values.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### How to Run
1. Clone this repository or download the source code file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:
