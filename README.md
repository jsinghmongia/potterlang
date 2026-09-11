# PotterLang

**PotterLang** is an interpreted, Harry Potter-themed programming language implemented in Python.

PotterLang uses magical incantations as programming constructs while retaining familiar programming concepts such as variables, expressions, conditionals, loops, functions, arrays, exception handling, lexical analysis, parsing, scoped environments, and tree-walk interpretation.

PotterLang source files use the `.wand` extension.

---

# Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Running PotterLang](#running-potterlang)
7. [Your First PotterLang Program](#your-first-potterlang-program)
8. [Language Syntax](#language-syntax)
9. [Variables](#variables)
10. [Data Types](#data-types)
11. [Operators](#operators)
12. [Output](#output)
13. [Conditionals](#conditionals)
14. [Loops](#loops)
15. [Functions](#functions)
16. [Return Values](#return-values)
17. [Recursion](#recursion)
18. [Exception Handling](#exception-handling)
19. [Arrays](#arrays)
20. [Array Access and Mutation](#array-access-and-mutation)
21. [Comments](#comments)
22. [Scope](#scope)
23. [Complete Programs](#complete-programs)
24. [Language Keyword Reference](#language-keyword-reference)
25. [Operator Reference](#operator-reference)
26. [File Extension](#file-extension)
27. [Interpreter Architecture](#interpreter-architecture)
28. [Example Programs](#example-programs)

---

# Introduction

PotterLang is designed as an educational and experimental programming language where traditional programming concepts are represented using terminology inspired by the Harry Potter universe.

Instead of writing:

```text
var score = 100
```

PotterLang uses:

```text
Accio score = 100
```

Instead of:

```text
print(score)
```

PotterLang uses:

```text
Lumos score
```

Instead of:

```text
if (score >= 50)
```

PotterLang uses:

```text
Riddikulus (score >= 50)
```

The goal is not to replace conventional programming languages, but to provide a fun language through which concepts such as lexical analysis, parsing, abstract syntax trees, environments, functions, recursion, and interpretation can be explored.

---

# Features

PotterLang currently provides the following language features:

* Variable declaration and assignment
* Integers
* Floating-point numbers
* Strings
* Booleans
* Arrays
* Arithmetic expressions
* Comparison expressions
* Logical expressions
* Conditional statements
* `while`-style loops
* User-defined functions
* Function parameters
* Return values
* Recursive functions
* Lexical scoping
* Function closures
* Exception handling
* Array indexing
* Array mutation
* Tree-walk interpretation
* `.wand` source files

---

# Architecture

PotterLang follows a traditional interpreter pipeline.

```text
PotterLang Source
       |
       v
     Lexer
       |
       v
     Tokens
       |
       v
     Parser
       |
       v
  Abstract Syntax Tree
       |
       v
   Environment
       |
       v
 Interpreter
       |
       v
    Output
```

The major components are:

### Lexer

The lexer reads raw PotterLang source code and converts it into a sequence of tokens.

### Parser

The parser consumes the token stream and constructs an Abstract Syntax Tree (AST).

### AST

The AST represents the structure of the PotterLang program.

### Environment

The environment stores variables, functions, scopes, and bindings required during execution.

### Interpreter

The interpreter walks through the AST and evaluates each node.

---

# Project Structure

A typical PotterLang project contains the following files:

```text
PotterLang/
│
├── tokens.py
├── lexer.py
├── ast_nodes.py
├── parser.py
├── environment.py
├── interpreter.py
├── potter.py
│
└── examples/
    ├── hello.wand
    ├── bubble_sort.wand
    └── binary_search.wand
```

## `tokens.py`

Contains token definitions and token representation used by the lexer and parser.

## `lexer.py`

Converts PotterLang source code into tokens.

## `ast_nodes.py`

Contains the AST node definitions representing expressions and statements.

## `parser.py`

Implements recursive-descent parsing and converts tokens into an AST.

## `environment.py`

Implements variable environments, scope handling, function bindings, and closures.

## `interpreter.py`

Walks the AST and evaluates the program.

## `potter.py`

Acts as the main command-line entry point for running `.wand` programs.

---

# Installation

## Requirements

PotterLang requires:

```text
Python 3.8+
```

Verify your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

Clone or download the PotterLang repository and open a terminal in the project directory.

No external runtime is required beyond Python unless the project specifies additional dependencies.

---

# Running PotterLang

A PotterLang program is stored in a file ending in `.wand`.

For example:

```text
hello.wand
```

Run it with:

```bash
python potter.py hello.wand
```

If the PotterLang CLI has been installed and registered globally:

```bash
potter hello.wand
```

---

# Your First PotterLang Program

Create a file named:

```text
hello.wand
```

Add:

```text
Lumos "Hello, Hogwarts!"
```

Run:

```bash
python potter.py hello.wand
```

The program produces:

```text
Hello, Hogwarts!
```

A slightly larger program:

```text
Accio wizard = "Harry"
Accio house = "Gryffindor"

Lumos "Wizard: " + wizard
Lumos "House: " + house
```

---

# Language Syntax

PotterLang uses a syntax inspired by conventional programming languages.

Statements are generally written one after another.

Example:

```text
Accio name = "Harry"
Accio age = 17

Lumos name
Lumos age
```

Blocks of statements are enclosed in curly braces:

```text
Riddikulus (age >= 17) {
    Lumos "Adult wizard"
}
```

Expressions can contain literals, variables, operators, function calls, and array access.

---

# Variables

Variables are declared using the `Accio` keyword.

## Declaration

```text
Accio score = 100
```

Another example:

```text
Accio wizard = "Harry"
```

Boolean values can be assigned directly:

```text
Accio is_alive = true
```

Variables can also contain expressions:

```text
Accio score = 50 + 25
```

Variables can be reassigned using `Accio`:

```text
Accio score = 100
Accio score = 150
```

---

# Data Types

PotterLang supports the following fundamental data types.

## Integer

Whole numbers:

```text
Accio age = 17
Accio score = 100
```

## Float

Decimal numbers:

```text
Accio temperature = 21.5
Accio price = 12.75
```

## String

Text values are enclosed in double quotation marks:

```text
Accio name = "Harry"
Accio spell = "Expelliarmus"
```

## Boolean

PotterLang provides two boolean values:

```text
true
false
```

Example:

```text
Accio wizard = true
Accio defeated = false
```

## Array

Arrays contain multiple values:

```text
Accio spells = ["Lumos", "Accio", "Expelliarmus"]
```

Arrays can contain values of the supported types.

---

# Operators

## Arithmetic Operators

PotterLang supports:

```text
+
-
*
/
%
```

Example:

```text
Accio a = 20
Accio b = 5

Lumos a + b
Lumos a - b
Lumos a * b
Lumos a / b
Lumos a % b
```

Expressions can be combined:

```text
Accio result = 10 + 5 * 2
```

Parentheses can be used to control evaluation order:

```text
Accio result = (10 + 5) * 2
```

---

# Comparison Operators

PotterLang supports:

```text
==
!=
<
>
<=
>=
```

Examples:

```text
Lumos 10 == 10
Lumos 10 != 5
Lumos 5 < 10
Lumos 10 > 5
Lumos 10 <= 10
Lumos 10 >= 5
```

Comparison expressions evaluate to a boolean value.

---

# Logical Operators

PotterLang supports:

```text
and
or
not
```

Examples:

```text
Accio age = 18
Accio has_permission = true

Riddikulus (age >= 18 and has_permission) {
    Lumos "Access granted."
}
```

Using `or`:

```text
Riddikulus (age >= 18 or has_permission) {
    Lumos "Access granted."
}
```

Using `not`:

```text
Riddikulus (not false) {
    Lumos "The spell is active."
}
```

---

# Output

The `Lumos` keyword prints an expression to standard output.

## Printing a string

```text
Lumos "Mischief Managed"
```

## Printing a variable

```text
Accio score = 100
Lumos score
```

## Printing an expression

```text
Accio a = 10
Accio b = 20

Lumos a + b
```

## Combining strings and values

```text
Accio wizard = "Harry"
Accio score = 100

Lumos wizard + " scored " + score + " points."
```

---

# Conditionals

PotterLang uses `Riddikulus` for conditional execution.

## If Statement

```text
Riddikulus (condition) {
    statements
}
```

Example:

```text
Accio score = 75

Riddikulus (score >= 50) {
    Lumos "Passed the O.W.L. exam!"
}
```

---

# If / Else

The `Finite` keyword represents the alternative branch.

```text
Riddikulus (condition) {
    statements
} Finite {
    statements
}
```

Example:

```text
Accio score = 40

Riddikulus (score >= 50) {
    Lumos "Passed the O.W.L. exam!"
} Finite {
    Lumos "Troll grade received."
}
```

---

# Loops

PotterLang uses `TimeTurner` for while-style loops.

Syntax:

```text
TimeTurner (condition) {
    statements
}
```

Example:

```text
Accio counter = 1

TimeTurner (counter <= 5) {
    Lumos counter
    Accio counter = counter + 1
}
```

Output:

```text
1
2
3
4
5
```

The condition is evaluated before every iteration.

---

# Functions

Functions are declared using the `Incantation` keyword.

Syntax:

```text
Incantation functionName(parameters) {
    statements
}
```

Example:

```text
Incantation addGalleons(a, b) {
    ExpectoPatronum a + b
}
```

The function can then be called:

```text
Accio total = addGalleons(10, 25)

Lumos total
```

Output:

```text
35
```

---

# Function Parameters

Functions may accept zero or more parameters.

## No parameters

```text
Incantation greet() {
    Lumos "Hello, wizard!"
}
```

Call:

```text
greet()
```

## One parameter

```text
Incantation greet(name) {
    Lumos "Hello, " + name
}
```

Call:

```text
greet("Harry")
```

## Multiple parameters

```text
Incantation multiply(a, b) {
    ExpectoPatronum a * b
}
```

Call:

```text
Accio result = multiply(5, 4)
Lumos result
```

---

# Return Values

Functions return values using:

```text
ExpectoPatronum
```

Example:

```text
Incantation square(number) {
    ExpectoPatronum number * number
}

Accio result = square(8)

Lumos result
```

Output:

```text
64
```

A function can return from within a conditional:

```text
Incantation checkScore(score) {
    Riddikulus (score >= 50) {
        ExpectoPatronum "Passed"
    } Finite {
        ExpectoPatronum "Failed"
    }
}
```

---

# Recursion

PotterLang supports recursive function calls.

A recursive function calls itself until a terminating condition is reached.

## Factorial

```text
Incantation factorial(n) {
    Riddikulus (n <= 1) {
        ExpectoPatronum 1
    } Finite {
        ExpectoPatronum n * factorial(n - 1)
    }
}

Lumos factorial(5)
```

Output:

```text
120
```

Recursive calls are evaluated using the runtime's function and environment stack.

---

# Exception Handling

PotterLang provides exception handling using two magical keywords:

```text
Protego
Crucio
```

`Protego` defines the protected section of code.

`Crucio` handles an exception raised inside that section.

Syntax:

```text
Protego {
    statements
} Crucio (errorVariable) {
    statements
}
```

Example:

```text
Protego {
    Accio result = 100 / 0
    Lumos result
} Crucio (curse) {
    Lumos "Defense triggered! Hex intercepted: " + curse
}
```

The exception information is made available through the variable specified by `Crucio`.

---

# Arrays

Arrays are created using square brackets.

Example:

```text
Accio spells = [
    "Expelliarmus",
    "Stupefy",
    "Alohomora"
]
```

Arrays can contain numbers:

```text
Accio numbers = [10, 20, 30, 40, 50]
```

Arrays can be passed to functions:

```text
Incantation first(arr) {
    ExpectoPatronum arr[0]
}

Accio spells = ["Lumos", "Accio", "Protego"]

Lumos first(spells)
```

---

# Array Access and Mutation

Array indexes begin at `0`.

Given:

```text
Accio spells = ["Expelliarmus", "Stupefy", "Alohomora"]
```

The first element is:

```text
spells[0]
```

The second element is:

```text
spells[1]
```

The third element is:

```text
spells[2]
```

Example:

```text
Lumos spells[0]
```

Output:

```text
Expelliarmus
```

Array elements can also be modified:

```text
Accio spells[1] = "AvadaKedavra"
```

Then:

```text
Lumos spells[1]
```

produces:

```text
AvadaKedavra
```

Array indexing can also use expressions:

```text
Accio index = 1
Lumos spells[index]
```

---

# Comments

Comments are intended to allow programmers to document their PotterLang source code.

If comment syntax is implemented in the current lexer, use the supported comment format consistently throughout `.wand` programs.

Example:

```text
// This is a comment
Accio score = 100
```

---

# Scope

PotterLang uses environments to manage variable bindings and lexical scope.

A function creates its own execution environment for its parameters and local variables.

For example:

```text
Accio x = 10

Incantation test() {
    Accio x = 20
    Lumos x
}

test()

Lumos x
```

The `x` inside the function belongs to the function's local scope, while the `x` outside belongs to the surrounding environment.

Functions can retain access to variables from their surrounding environment through closures.

---

# Complete Programs

## Hello Wizard

```text
Lumos "Hello, Hogwarts!"
```

---

## Student Information

```text
Accio name = "Harry"
Accio house = "Gryffindor"
Accio year = 7

Lumos "Name: " + name
Lumos "House: " + house
Lumos "Year: " + year
```

---

## O.W.L. Grade Checker

```text
Accio score = 72

Riddikulus (score >= 90) {
    Lumos "Outstanding"
} Finite {
    Riddikulus (score >= 50) {
        Lumos "Passed"
    } Finite {
        Lumos "Failed"
    }
}
```

---

## Counting Program

```text
Accio counter = 1

TimeTurner (counter <= 10) {
    Lumos counter
    Accio counter = counter + 1
}
```

---

# Bubble Sort

PotterLang can be used to implement common algorithms.

The following program implements Bubble Sort:

```text
Incantation bubbleSort(arr, n) {
    Accio i = 0

    TimeTurner (i < n - 1) {
        Accio j = 0

        TimeTurner (j < n - i - 1) {
            Riddikulus (arr[j] > arr[j + 1]) {
                Accio temp = arr[j]
                Accio arr[j] = arr[j + 1]
                Accio arr[j + 1] = temp
            }

            Accio j = j + 1
        }

        Accio i = i + 1
    }

    ExpectoPatronum arr
}

Accio numbers = [64, 34, 25, 12, 22, 11, 90]

Accio sorted = bubbleSort(numbers, 7)

Lumos sorted
```

The algorithm repeatedly compares adjacent elements and swaps them when they are in the wrong order.

---

# Binary Search

Binary Search can also be expressed using PotterLang functions, loops, arrays, conditionals, and return values.

```text
Incantation binarySearch(arr, target, low, high) {
    TimeTurner (low <= high) {
        Accio mid = (low + high) / 2

        Riddikulus (arr[mid] == target) {
            ExpectoPatronum mid
        }

        Riddikulus (arr[mid] < target) {
            Accio low = mid + 1
        } Finite {
            Accio high = mid - 1
        }
    }

    ExpectoPatronum -1
}

Accio inventory = [10, 20, 30, 40, 50, 60, 70]

Accio targetIndex = binarySearch(
    inventory,
    40,
    0,
    6
)

Lumos "Target found at index: " + targetIndex
```

---

# Function Example

A complete function-based program:

```text
Incantation addGalleons(a, b) {
    ExpectoPatronum a + b
}

Incantation multiplyGalleons(a, b) {
    ExpectoPatronum a * b
}

Accio gold = addGalleons(10, 25)
Accio total = multiplyGalleons(gold, 2)

Lumos "Gold: " + gold
Lumos "Total: " + total
```

---

# Exception Example

```text
Protego {
    Accio numerator = 100
    Accio denominator = 0

    Accio result = numerator / denominator

    Lumos result
} Crucio (curse) {
    Lumos "A magical error occurred: " + curse
}
```

---

# Language Keyword Reference

| Keyword           | Purpose                                  |
| ----------------- | ---------------------------------------- |
| `Accio`           | Variable declaration or assignment       |
| `Lumos`           | Print an expression                      |
| `Riddikulus`      | Conditional / if statement               |
| `Finite`          | Else branch                              |
| `TimeTurner`      | While-style loop                         |
| `Incantation`     | Function declaration                     |
| `ExpectoPatronum` | Return a value from a function           |
| `Protego`         | Begin protected exception-handling block |
| `Crucio`          | Catch an exception                       |
| `true`            | Boolean true                             |
| `false`           | Boolean false                            |
| `and`             | Logical AND                              |
| `or`              | Logical OR                               |
| `not`             | Logical NOT                              |

---

# Operator Reference

## Arithmetic

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `%`      | Modulo         |

## Comparison

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `<`      | Less than             |
| `>`      | Greater than          |
| `<=`     | Less than or equal    |
| `>=`     | Greater than or equal |

## Logical

| Operator | Meaning     |
| -------- | ----------- |
| `and`    | Logical AND |
| `or`     | Logical OR  |
| `not`    | Logical NOT |

---

# File Extension

PotterLang programs use:

```text
.wand
```

Example:

```text
hello.wand
```

```text
bubble_sort.wand
```

```text
factorial.wand
```

The `.wand` extension identifies source files intended for the PotterLang interpreter.

---

# Interpreter Architecture

PotterLang is implemented as a tree-walk interpreter.

The execution process can be summarized as:

```text
.wand Source File
       |
       v
     Lexer
       |
       v
     Tokens
       |
       v
     Parser
       |
       v
Abstract Syntax Tree
       |
       v
 Environment / Scope
       |
       v
   Interpreter
       |
       v
 Program Execution
```

## Lexical Analysis

The lexer reads the source code character by character and identifies meaningful units such as:

* Keywords
* Identifiers
* Numbers
* Strings
* Operators
* Parentheses
* Braces
* Brackets
* Separators

These units are represented as tokens.

## Parsing

The parser consumes the tokens and verifies that they follow the PotterLang grammar.

The parser then creates an Abstract Syntax Tree.

## Abstract Syntax Tree

The AST represents the logical structure of the program.

For example:

```text
Accio score = 100
```

is represented conceptually as a variable declaration containing:

```text
Variable: score
Value: 100
```

## Environment

The environment stores runtime values associated with variable names.

For example:

```text
Accio score = 100
```

creates a binding conceptually equivalent to:

```text
score -> 100
```

Nested environments allow local variables and function scopes to coexist with outer scopes.

## Interpreter

The interpreter walks through the AST and evaluates each node.

For example:

```text
Accio result = 10 + 20
```

causes the interpreter to:

1. Evaluate `10`.
2. Evaluate `20`.
3. Apply `+`.
4. Produce `30`.
5. Store `30` under `result`.

---

# Language Design Philosophy

PotterLang is designed around the idea that programming language concepts can be made approachable through a familiar fictional theme.

The magical terminology maps directly to conventional programming concepts:

```text
Accio             -> variable declaration / assignment

Lumos             -> output

Riddikulus        -> if

Finite            -> else

TimeTurner        -> while loop

Incantation       -> function

ExpectoPatronum   -> return

Protego           -> try

Crucio            -> catch
```

Despite the themed syntax, the underlying concepts remain conventional programming-language concepts.

---

# Complete Syntax Overview

The following examples provide a compact reference for PotterLang syntax.

## Variable

```text
Accio variable = value
```

## Assignment

```text
Accio variable = expression
```

## Output

```text
Lumos expression
```

## Conditional

```text
Riddikulus (condition) {
    statements
}
```

## Conditional with Else

```text
Riddikulus (condition) {
    statements
} Finite {
    statements
}
```

## Loop

```text
TimeTurner (condition) {
    statements
}
```

## Function

```text
Incantation name(parameters) {
    statements
}
```

## Return

```text
ExpectoPatronum expression
```

## Exception Handling

```text
Protego {
    statements
} Crucio (error) {
    statements
}
```

## Array

```text
Accio values = [value1, value2, value3]
```

## Array Access

```text
values[index]
```

## Array Mutation

```text
Accio values[index] = expression
```

## Function Call

```text
functionName(argument1, argument2)
```

---

# Example: Complete PotterLang Program

The following program combines variables, functions, conditionals, loops, arrays, and output:

```text
Incantation calculateScore(scores) {
    Accio total = 0
    Accio i = 0

    TimeTurner (i < 5) {
        Accio total = total + scores[i]
        Accio i = i + 1
    }

    ExpectoPatronum total
}

Accio scores = [80, 75, 90, 65, 85]

Accio total = calculateScore(scores)

Lumos "Total score: " + total

Riddikulus (total >= 350) {
    Lumos "Outstanding wizard!"
} Finite {
    Lumos "More studying required."
}
```

---

# Example: Recursive Factorial

```text
Incantation factorial(n) {
    Riddikulus (n <= 1) {
        ExpectoPatronum 1
    } Finite {
        ExpectoPatronum n * factorial(n - 1)
    }
}

Accio result = factorial(5)

Lumos "Factorial: " + result
```

---

# Example: Array Processing

```text
Accio spells = [
    "Lumos",
    "Accio",
    "Protego",
    "Expelliarmus"
]

Accio i = 0

TimeTurner (i < 4) {
    Lumos spells[i]
    Accio i = i + 1
}
```

---

# Example: Exception Handling

```text
Protego {
    Accio x = 10
    Accio y = 0

    Accio result = x / y

    Lumos result
} Crucio (curse) {
    Lumos "Spell failed: " + curse
}
```

---

# PotterLang at a Glance

A complete PotterLang program can look like this:

```text
Accio wizard = "Harry"
Accio score = 85

Incantation getResult(score) {
    Riddikulus (score >= 50) {
        ExpectoPatronum "Passed"
    } Finite {
        ExpectoPatronum "Failed"
    }
}

Accio result = getResult(score)

Lumos wizard + ": " + result

TimeTurner (score < 100) {
    Accio score = score + 5
}

Lumos "Final score: " + score
```

The language combines a themed vocabulary with conventional programming-language structures, making PotterLang both a functional interpreted language and an exploration of how interpreters work internally.

---

# Summary

PotterLang provides a complete interpreted programming environment built around a magical programming vocabulary.

The primary language constructs are:

```text
Accio             Variables
Lumos             Output
Riddikulus        Conditions
Finite            Else
TimeTurner        Loops
Incantation       Functions
ExpectoPatronum   Return values
Protego           Exception handling
Crucio            Exception catching
```

Programs are written in `.wand` files and executed by the PotterLang interpreter.

The project demonstrates the major stages of interpreter construction:

```text
Source Code
    ↓
Lexical Analysis
    ↓
Tokens
    ↓
Parsing
    ↓
Abstract Syntax Tree
    ↓
Environment / Scope
    ↓
Tree-Walk Interpretation
    ↓
Execution
```

PotterLang is intended for experimentation, education, and fun while demonstrating real programming-language implementation techniques.
