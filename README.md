# PotterLang

PotterLang is an interpreted, wizarding-themed programming language implemented in Python.

The language combines familiar programming concepts with magical terminology. Programs support variables, expressions, conditionals, loops, functions, recursion, arrays, input, exception handling, scoped environments, and a tree-walk interpreter.

PotterLang source files use the `.wand` file extension.

The current package version is **0.1.2**.

---

# Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Running PotterLang](#running-potterlang)
6. [REPL](#repl)
7. [Your First Program](#your-first-program)
8. [Source File Structure](#source-file-structure)
9. [Language Basics](#language-basics)
10. [Variables](#variables)
11. [Data Types](#data-types)
12. [Output](#output)
13. [Input](#input)
14. [Arithmetic Operators](#arithmetic-operators)
15. [Comparison Operators](#comparison-operators)
16. [Logical Operators](#logical-operators)
17. [Unary Operators](#unary-operators)
18. [Operator Precedence](#operator-precedence)
19. [Conditionals](#conditionals)
20. [Loops](#loops)
21. [Functions](#functions)
22. [Return Values](#return-values)
23. [Recursion](#recursion)
24. [Arrays](#arrays)
25. [Array Access](#array-access)
26. [Array Mutation](#array-mutation)
27. [Comments](#comments)
28. [Exception Handling](#exception-handling)
29. [Program Termination](#program-termination)
30. [Scope and Environments](#scope-and-environments)
31. [Identifiers](#identifiers)
32. [Strings](#strings)
33. [Complete Examples](#complete-examples)
34. [Keyword Reference](#keyword-reference)
35. [Operator Reference](#operator-reference)
36. [Interpreter Architecture](#interpreter-architecture)
37. [Project Structure](#project-structure)
38. [Current Language Limitations](#current-language-limitations)

---

# Introduction

PotterLang is an esoteric programming language inspired by the magical world of Harry Potter.

The language replaces conventional programming terminology with magical incantations while preserving familiar programming structures.

For example, variable declaration:

```text
Accio score = 100
```

Output:

```text
Lumos score
```

Conditional execution:

```text
Riddikulus (score >= 50) {
    Lumos "Passed"
}
```

Function declaration:

```text
Incantation add(a, b) {
    ExpectoPatronum a + b
}
```

The magical terminology is only the surface syntax. Internally, PotterLang uses the same fundamental concepts found in traditional interpreters:

```text
Source Code
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
Execution
```

---

# Features

PotterLang currently supports:

* Variable declaration
* Variable assignment
* Integer values
* Floating-point values
* String values
* Boolean values
* Arrays
* Arithmetic expressions
* String concatenation
* Comparison operators
* Logical operators
* Unary operators
* Conditional statements
* `while`-style loops
* User-defined functions
* Function parameters
* Function return values
* Recursive functions
* Function closures
* Lexical environments
* Array indexing
* Array mutation
* User input
* Exception handling
* Program termination
* Comments
* Interactive REPL
* `.wand` source files

---

# Requirements

PotterLang requires:

```text
Python 3.10 or newer
```

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

# Installation

PotterLang is packaged as a Python project.

From the repository root, install it with:

```bash
pip install .
```

For development, an editable installation can be used:

```bash
pip install -e .
```

After installation, the `potter` command becomes available.

Verify the installation:

```bash
potter
```

Running `potter` without a file starts the PotterLang REPL.

---

# Running PotterLang

PotterLang programs are stored in files ending with:

```text
.wand
```

For example:

```text
hello.wand
```

Run a PotterLang program with:

```bash
potter hello.wand
```

The interpreter reads the source file, tokenizes it, parses it into an Abstract Syntax Tree, and evaluates the resulting tree.

---

# REPL

PotterLang also provides an interactive Read-Eval-Print Loop.

Start the REPL with:

```bash
potter
```

The interpreter displays:

```text
PotterLang 1.0.0 Interactive REPL
```

You can then enter PotterLang statements interactively:

```text
>>> Accio score = 100
>>> Lumos score
100
```

The REPL maintains the same environment between entered expressions.

To exit the REPL, use:

```text
AvadaKedavra
```

or press:

```text
Ctrl+C
```

---

# Your First Program

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
potter hello.wand
```

Output:

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

Output:

```text
Wizard: Harry
House: Gryffindor
```

---

# Source File Structure

The interpreter is organized as a Python package:

```text
potterlang/
│
├── src/
│   └── potterlang/
│       ├── __init__.py
│       ├── ast_nodes.py
│       ├── environment.py
│       ├── interpreter.py
│       ├── lexer.py
│       ├── parser.py
│       ├── potter.py
│       └── tokens.py
│
├── compiler-web/
├── dist/
├── test.wand
├── test_algo.wand
├── pyproject.toml
└── README.md
```

## `lexer.py`

The lexer converts raw PotterLang source code into tokens.

It recognizes:

* Keywords
* Identifiers
* Numbers
* Strings
* Operators
* Parentheses
* Braces
* Array brackets
* Commas
* Comments

## `tokens.py`

Defines the token types used by the lexer and parser.

## `parser.py`

Consumes the token stream and builds the Abstract Syntax Tree.

PotterLang uses a recursive-descent parser.

## `ast_nodes.py`

Contains the AST node classes representing PotterLang programs.

## `environment.py`

Implements variable environments and parent-child scope relationships.

## `interpreter.py`

Walks the AST and evaluates the program.

## `potter.py`

Provides the command-line entry point, file execution, and REPL.

---

# Language Basics

PotterLang statements do not require semicolons.

Example:

```text
Accio name = "Harry"
Accio age = 17

Lumos name
Lumos age
```

Blocks are enclosed using curly braces:

```text
Riddikulus (age >= 17) {
    Lumos "Adult wizard"
}
```

Expressions may be used anywhere an expression is expected.

---

# Variables

Variables are introduced using:

```text
Accio
```

## Declaration

```text
Accio score = 100
```

```text
Accio wizard = "Harry"
```

```text
Accio alive = true
```

A variable can contain an expression:

```text
Accio score = 50 + 25
```

## Assignment

Existing variables can be reassigned using `=`:

```text
Accio score = 100

score = 150
```

The `Accio` keyword is used for declarations, while ordinary assignment can be used for an existing variable.

Inside a loop:

```text
Accio counter = 1

TimeTurner (counter <= 5) {
    Lumos counter
    counter = counter + 1
}
```

---

# Data Types

PotterLang currently supports four primitive value categories and arrays.

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

Numbers containing a decimal point are represented as floating-point values.

## String

Strings are enclosed in double quotation marks:

```text
Accio wizard = "Harry"
Accio spell = "Expelliarmus"
```

## Boolean

PotterLang has two boolean literals:

```text
true
false
```

Example:

```text
Accio alive = true
Accio defeated = false
```

## Array

Arrays are enclosed in square brackets:

```text
Accio spells = ["Lumos", "Accio", "Protego"]
```

Arrays can contain expressions:

```text
Accio a = 10
Accio b = 20

Accio numbers = [a, b, a + b]
```

---

# Output

The `Lumos` keyword prints the value of an expression.

## String

```text
Lumos "Mischief Managed"
```

## Variable

```text
Accio score = 100

Lumos score
```

## Expression

```text
Accio a = 10
Accio b = 20

Lumos a + b
```

## String Concatenation

When `+` is used and either operand is a string, PotterLang automatically converts the other operand to a string.

For example:

```text
Accio wizard = "Harry"
Accio score = 100

Lumos wizard + " scored " + score + " points."
```

Output:

```text
Harry scored 100 points.
```

---

# Input

PotterLang uses:

```text
Legilimens
```

to read user input.

Syntax:

```text
Legilimens(prompt)
```

Example:

```text
Accio name = Legilimens("Enter your name: ")

Lumos "User: " + name
```

The input system attempts to convert numeric input automatically.

For example:

```text
Accio age = Legilimens("Enter your age: ")
```

If the user enters:

```text
17
```

the resulting value is an integer.

If the user enters:

```text
17.5
```

the resulting value is a floating-point number.

Other input remains a string.

`Legilimens()` may also be used without a prompt:

```text
Accio value = Legilimens()
```

---

# Arithmetic Operators

PotterLang supports the following arithmetic operators:

```text
+
-
*
/
%
```

## Addition

```text
Lumos 10 + 5
```

Result:

```text
15
```

## Subtraction

```text
Lumos 10 - 5
```

Result:

```text
5
```

## Multiplication

```text
Lumos 10 * 5
```

Result:

```text
50
```

## Division

```text
Lumos 10 / 5
```

Result:

```text
2.0
```

## Modulo

```text
Lumos 10 % 3
```

Result:

```text
1
```

## Parentheses

Parentheses can be used to explicitly control evaluation order:

```text
Lumos (10 + 5) * 2
```

Result:

```text
30
```

---

# Comparison Operators

PotterLang supports:

```text
==
!=
>
<
>=
<=
```

## Equal

```text
Lumos 10 == 10
```

## Not Equal

```text
Lumos 10 != 5
```

## Greater Than

```text
Lumos 10 > 5
```

## Less Than

```text
Lumos 5 < 10
```

## Greater Than or Equal

```text
Lumos 10 >= 10
```

## Less Than or Equal

```text
Lumos 5 <= 10
```

Comparison expressions evaluate to boolean values.

---

# Logical Operators

PotterLang uses symbolic logical operators.

## AND

```text
&&
```

Example:

```text
Accio age = 20
Accio permission = true

Riddikulus (age >= 18 && permission) {
    Lumos "Access granted."
}
```

Both conditions must be true.

## OR

```text
||
```

Example:

```text
Riddikulus (age >= 18 || permission) {
    Lumos "Access granted."
}
```

At least one condition must be true.

## NOT

```text
!
```

Example:

```text
Accio locked = false

Riddikulus (!locked) {
    Lumos "The door is open."
}
```

The `!` operator reverses the boolean value.

---

# Unary Operators

PotterLang supports unary:

```text
!
-
```

## Logical NOT

```text
!true
```

produces:

```text
false
```

## Numeric Negation

```text
-10
```

produces:

```text
-10
```

Variables can also be negated:

```text
Accio score = 100

Lumos -score
```

---

# Operator Precedence

Expressions are parsed in the following general order, from lower precedence to higher precedence:

```text
Logical OR       ||
Logical AND      &&
Comparison       == != > < >= <=
Addition         + -
Multiplication  * / %
Unary            ! -
Postfix          [] ()
Primary          literals, identifiers, arrays, parentheses
```

Therefore:

```text
10 + 5 * 2
```

is interpreted as:

```text
10 + (5 * 2)
```

while:

```text
(10 + 5) * 2
```

is interpreted as:

```text
(10 + 5) * 2
```

---

# Conditionals

PotterLang uses `Riddikulus` for conditional execution.

Syntax:

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

Syntax:

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
    Lumos "Passed!"
} Finite {
    Lumos "Failed!"
}
```

---

# Nested Conditionals

Conditionals can be placed inside other conditionals.

```text
Accio score = 85

Riddikulus (score >= 50) {
    Riddikulus (score >= 80) {
        Lumos "Outstanding!"
    } Finite {
        Lumos "Passed!"
    }
} Finite {
    Lumos "Failed!"
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
    counter = counter + 1
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

The loop condition is evaluated before each iteration.

---

# Functions

Functions are declared using:

```text
Incantation
```

Syntax:

```text
Incantation functionName(parameters) {
    statements
}
```

Example:

```text
Incantation add(a, b) {
    ExpectoPatronum a + b
}
```

Functions are called using their name followed by parentheses:

```text
Accio result = add(10, 25)

Lumos result
```

Output:

```text
35
```

---

# Functions Without Parameters

A function can have no parameters:

```text
Incantation greet() {
    Lumos "Hello, wizard!"
}

greet()
```

---

# Functions With Parameters

A function may accept one or more parameters:

```text
Incantation greet(name) {
    Lumos "Hello, " + name
}

greet("Harry")
```

Multiple parameters are separated by commas:

```text
Incantation multiply(a, b) {
    ExpectoPatronum a * b
}

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

A return statement immediately exits the current function.

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

---

# Arrays

Arrays are represented using square brackets.

Example:

```text
Accio spells = [
    "Expelliarmus",
    "Stupefy",
    "Alohomora"
]
```

Arrays may contain numbers:

```text
Accio numbers = [10, 20, 30, 40, 50]
```

Arrays may contain expressions:

```text
Accio a = 10
Accio b = 20

Accio values = [a, b, a + b]
```

An empty array is valid:

```text
Accio empty = []
```

---

# Array Access

Array indexes begin at `0`.

Given:

```text
Accio spells = ["Lumos", "Accio", "Protego"]
```

The first element is:

```text
spells[0]
```

The second element:

```text
spells[1]
```

The third element:

```text
spells[2]
```

Example:

```text
Lumos spells[0]
```

Output:

```text
Lumos
```

---

# Dynamic Array Indexing

Array indexes may be expressions.

```text
Accio spells = ["Lumos", "Accio", "Protego"]
Accio index = 1

Lumos spells[index]
```

Output:

```text
Accio
```

---

# Array Mutation

Array elements can be modified using assignment.

```text
Accio spells = ["Lumos", "Accio", "Protego"]

spells[1] = "Expelliarmus"

Lumos spells[1]
```

Output:

```text
Expelliarmus
```

Array mutation can also use expressions:

```text
Accio index = 1

spells[index] = "Stupefy"
```

---

# Comments

Single-line comments begin with:

```text
//
```

Example:

```text
// This is a PotterLang comment

Accio score = 100

// Display the score
Lumos score
```

Everything from `//` to the end of the line is ignored by the lexer.

---

# Exception Handling

PotterLang provides exception handling through:

```text
Protego
Crucio
```

`Protego` starts the protected block.

`Crucio` catches an exception.

Syntax:

```text
Protego {
    statements
} Crucio (error) {
    statements
}
```

Example:

```text
Protego {
    Accio result = 100 / 0
    Lumos result
} Crucio (curse) {
    Lumos "Defense triggered: " + curse
}
```

The variable inside `Crucio(...)` receives the exception message as a string.

---

# Array Exceptions

Exception handling can also be used to catch invalid array access.

```text
Accio spells = ["Lumos", "Accio", "Protego"]

Protego {
    Lumos spells[99]
} Crucio (err) {
    Lumos "Caught exception: " + err
}
```

---

# Program Termination

`AvadaKedavra` immediately terminates the interpreter.

Example:

```text
Lumos "The spell begins."

AvadaKedavra

Lumos "This will never execute."
```

`AvadaKedavra` terminates the entire running interpreter process.

It can also be used in the REPL to exit the interactive session.

---

# Scope and Environments

PotterLang uses chained environments to manage variable lookup and assignment.

Each block can create a child environment.

For example:

```text
Accio x = 10

Riddikulus (true) {
    Accio y = 20
    Lumos x
    Lumos y
}
```

The block can access variables from its parent environment.

Functions capture the environment in which they are defined, allowing functions to access surrounding variables.

Example:

```text
Accio message = "Hello"

Incantation greet() {
    Lumos message
}

greet()
```

Output:

```text
Hello
```

Variable assignment searches the current environment and its parents for an existing binding.

---

# Identifiers

Identifiers are used for variable names, function names, and parameters.

An identifier may contain:

* Letters
* Digits
* Underscores

An identifier cannot begin with a digit.

Examples of valid identifiers:

```text
score
wizard
student_name
level1
calculate_score
```

Examples of invalid identifiers:

```text
1score
2wizard
```

Language keywords such as `Accio`, `Lumos`, and `Riddikulus` are reserved and should not be used as identifiers.

---

# Strings

Strings use double quotation marks:

```text
"Hello"
```

Example:

```text
Accio spell = "Expelliarmus"

Lumos spell
```

String concatenation uses `+`:

```text
Accio name = "Harry"
Accio house = "Gryffindor"

Lumos name + " belongs to " + house
```

When a string participates in a `+` operation, non-string operands are converted to strings automatically.

Example:

```text
Accio score = 100

Lumos "Score: " + score
```

Output:

```text
Score: 100
```

---

# Complete Examples

## Basic Program

```text
Accio wizard = "Harry"
Accio house = "Gryffindor"
Accio year = 7

Lumos "Wizard: " + wizard
Lumos "House: " + house
Lumos "Year: " + year
```

---

## Grade Checker

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

## Counter

```text
Accio counter = 1

TimeTurner (counter <= 10) {
    Lumos counter
    counter = counter + 1
}
```

---

## Function

```text
Incantation addGalleons(a, b) {
    ExpectoPatronum a + b
}

Accio total = addGalleons(10, 25)

Lumos "Total: " + total
```

---

## Recursive Factorial

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

## Input

```text
Accio user_name = Legilimens("Enter your name: ")
Accio age = Legilimens("Enter your age: ")

Lumos "Name: " + user_name
Lumos "Age: " + age
```

---

## Arrays

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
    i = i + 1
}
```

---

## Array Mutation

```text
Accio spells = [
    "Lumos",
    "Accio",
    "Protego"
]

spells[1] = "Expelliarmus"

Lumos spells[1]
```

---

## Exception Handling

```text
Accio spells = [
    "Lumos",
    "Accio",
    "Protego"
]

Protego {
    Lumos spells[99]
} Crucio (err) {
    Lumos "Caught exception: " + err
}
```

---

# Algorithm Example

PotterLang can express conventional algorithms using variables, loops, arrays, conditionals, functions, and recursion.

For example, a simple recursive calculation:

```text
Incantation calculate_mana(level, bonus) {
    Riddikulus (level <= 1) {
        ExpectoPatronum bonus
    } Finite {
        ExpectoPatronum level * 10 + calculate_mana(level - 1, bonus)
    }
}

Accio mana = calculate_mana(3, 15)

Lumos "Mana: " + mana
```

Output:

```text
Mana: 75
```

---

# Keyword Reference

| Keyword           | Purpose                         |
| ----------------- | ------------------------------- |
| `Accio`           | Declare a variable              |
| `Lumos`           | Print an expression             |
| `Riddikulus`      | Conditional statement           |
| `Finite`          | Else branch                     |
| `TimeTurner`      | While loop                      |
| `Incantation`     | Function declaration            |
| `ExpectoPatronum` | Return a value                  |
| `Legilimens`      | Read user input                 |
| `Protego`         | Begin exception-protected block |
| `Crucio`          | Catch an exception              |
| `AvadaKedavra`    | Immediately terminate execution |
| `true`            | Boolean true                    |
| `false`           | Boolean false                   |

---

# Operator Reference

## Arithmetic Operators

| Operator | Meaning                         |
| -------- | ------------------------------- |
| `+`      | Addition / string concatenation |
| `-`      | Subtraction                     |
| `*`      | Multiplication                  |
| `/`      | Division                        |
| `%`      | Modulo                          |

## Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

## Logical Operators

| Operator | Meaning     |   |            |
| -------- | ----------- | - | ---------- |
| `&&`     | Logical AND |   |            |
| `        |             | ` | Logical OR |
| `!`      | Logical NOT |   |            |

---

# Syntax Reference

## Variable Declaration

```text
Accio name = expression
```

## Variable Assignment

```text
name = expression
```

## Output

```text
Lumos expression
```

## Input

```text
Legilimens()
```

or:

```text
Legilimens(prompt)
```

## Conditional

```text
Riddikulus (condition) {
    statements
}
```

## Conditional With Else

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

## Function Declaration

```text
Incantation name(parameters) {
    statements
}
```

## Function Return

```text
ExpectoPatronum expression
```

## Function Call

```text
name(arguments)
```

## Array

```text
[value1, value2, value3]
```

## Array Access

```text
array[index]
```

## Array Assignment

```text
array[index] = expression
```

## Exception Handling

```text
Protego {
    statements
} Crucio (error) {
    statements
}
```

## Program Termination

```text
AvadaKedavra
```

## Comment

```text
// comment
```

---

# Interpreter Architecture

PotterLang is implemented as a tree-walk interpreter.

The execution pipeline is:

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
    Execution
```

## 1. Source Code

A `.wand` file contains PotterLang source code.

Example:

```text
Accio score = 100
Lumos score
```

## 2. Lexical Analysis

The lexer reads the source code and produces tokens.

For example:

```text
Accio score = 100
```

is broken into conceptual tokens:

```text
ACCIO
IDENTIFIER(score)
ASSIGN
NUMBER(100)
```

## 3. Parsing

The parser consumes these tokens and constructs an Abstract Syntax Tree.

The parser uses recursive-descent parsing.

## 4. Abstract Syntax Tree

The AST represents the structure of the program.

PotterLang defines AST nodes for constructs including:

* Program
* Variable declaration
* Variable assignment
* Array assignment
* Print
* Input
* Conditional
* Loop
* Block
* Function declaration
* Function call
* Return
* Array literal
* Array access
* Exception handling
* Binary expressions
* Unary expressions
* Literals
* Variables
* Program termination

## 5. Environment

The environment stores runtime variable bindings.

Environments can reference parent environments:

```text
Current Environment
        |
        v
Parent Environment
        |
        v
Global Environment
```

This allows nested scopes and functions to access values from surrounding environments.

## 6. Interpretation

The interpreter walks the AST and evaluates each node.

For example:

```text
Accio result = 10 + 20
```

is evaluated by:

```text
10
+
20
=
30
```

The resulting value is then stored in the current environment.

---

# Project Structure

The main interpreter implementation is located under:

```text
src/potterlang/
```

The source files are:

```text
src/potterlang/
├── __init__.py
├── ast_nodes.py
├── environment.py
├── interpreter.py
├── lexer.py
├── parser.py
├── potter.py
└── tokens.py
```

### `ast_nodes.py`

Defines the Abstract Syntax Tree node classes.

### `environment.py`

Implements variable environments and parent-scope lookup.

### `interpreter.py`

Contains the tree-walk interpreter and runtime behavior.

### `lexer.py`

Converts source code into tokens.

### `parser.py`

Converts tokens into an AST.

### `potter.py`

Provides:

* Source-file execution
* REPL functionality
* CLI entry point

### `tokens.py`

Defines the token types and token representation.

---

# Current Language Limitations

PotterLang is an experimental and educational programming language.

The current implementation intentionally provides a relatively small runtime.

The following should not be assumed to exist unless explicitly implemented in the interpreter:

* Standard-library functions
* `len()`
* `floor()`
* File I/O
* Networking
* Classes
* Objects
* Modules
* Imports
* Exception types
* User-defined exception classes
* For loops
* Switch statements
* Dictionaries / maps
* Built-in collection methods

For example, the following should not currently be considered standard PotterLang syntax:

```text
len(array)
```

or:

```text
floor(number)
```

unless those functions are added to the runtime.

---

# Language Design Philosophy

PotterLang intentionally maps traditional programming concepts to magical terminology.

The language vocabulary is:

```text
Accio
    Variable declaration

Lumos
    Output

Legilimens
    Input

Riddikulus
    If / conditional

Finite
    Else

TimeTurner
    While loop

Incantation
    Function

ExpectoPatronum
    Return

Protego
    Try / protected execution

Crucio
    Catch / exception handling

AvadaKedavra
    Terminate execution
```

The goal is to make the language recognizable as a programming language while giving every major construct a consistent magical identity.

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
    score = score + 5
}

Lumos "Final score: " + score
```

The program demonstrates:

* Variables
* Strings
* Numbers
* Functions
* Parameters
* Return values
* Conditionals
* Loops
* String concatenation
* Output

---

# Summary

PotterLang is a small interpreted programming language built around a wizarding-themed syntax.

Its core language consists of:

```text
Accio             Variable declaration
Lumos             Output
Legilimens        Input
Riddikulus        Conditional
Finite            Else
TimeTurner        Loop
Incantation       Function
ExpectoPatronum   Return
Protego           Exception handling
Crucio            Exception catching
AvadaKedavra      Program termination
```

Programs are stored as `.wand` files and executed by the PotterLang interpreter.

The implementation demonstrates the fundamental stages of interpreter construction:

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

PotterLang is designed as an experimental programming language and as a practical demonstration of how a language can be tokenized, parsed, represented as an AST, evaluated through environments, and executed by a tree-walk interpreter.

---
