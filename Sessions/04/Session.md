# Session 04

---

## Agenda

* Python Functions
* Functional Programming

---

## Python Functions - What are Functions

> In Python, functions are a group of related statements that can be called together. They typically perform a specific task and may or may not take a set of parameters or return a value.

---

## Python Functions - How Functions Works

* Function definition (`def`)
* Function invocation (Calling a function)

```python
def function_name(): # Definition of a function
    pass

# Start of program
# ...
# ...
function_name() # Invocation of a function
```

---

## Python Functions - Type of Functions

* *build-in* functions: `print()`, `len()`, `input()`
* *user-defined* functions

---

### Python Functions - Defining Functions

```python
def function_name(parameter_list):
    """docstring"""
    # statement
    # statements(s)
```

---

## Python Functions - All functions return a value

```python
# Procedure
def void_function(value):
    print(value)
    
# Function
def no_void_function(value):
    return value + 1
```

---

## Python Functions - Python returns multiple values

```python
def swap(a,b):
    return b,a

x = 10
y = 20
x,y = swap(x,y) # x = 20, y = 10
tuple = swap(x,y) # (20,10) Tuple
```

---

## Python Functions - Function Parameters

> * A *parameter* is a variable defined in the function header that makes data available within the function itself.
> * An *argument* is the actual value or data passed into the function when it is called. The data will held within the parameters.

---

## Python Functions - Function Parameters - Multiple Parameter Function

```python
def multiple(one,two,three):
    return one + two * three
```

---

## Python Functions - Function Parameters - Default Parameter Values

```python
def multiple_default(one,two=2,three=3):
    return one + two * three
```

> Once one parameter has a default value all remaining parameters to the right of that parameter must also have a default values.

```python
# SyntaxError: non-default argument follows default argument
def error_multiple_default(one=1,two,three=3):
    return one + two * three
```

---

## Python Functions - Function Parameters - Arbitrary Arguments

```python
def media(*args):
    return sum(args) / len(args)

media(10,20,30) # 20.0
lst=[10,20,30,40]
media(lst) # Doesn't work TypeError
media(*lst) # Works 25.0
```

---

## Python Functions - Function Parameters - Positional and Keywords Arguments

```python
def multiple_default(one, two=2,three=3):
    return one + two * three

args = { "two:" 30, "one" : 20, "three" : 40 }

multiple_default(20, 30, 40) # 	1220
multiple_default(args) # TypeError: unsupported operand type(s) for +: 'dict' and 'int'
multiple_default(*args) # TypeError: can't multiply sequence by non-int of type 'str'
multiple_default(**args) # 1220
```

---

## Python Functions - Function Parameters - Positional and Keywords Arguments

```python
def keywords_args(**args):
    return args["one"] + args["two"] * args["three"] 

keywords_args(one=20,two=30,three=40) # 1220
args = { "two" : 30, "one" : 20, "three" : 40 }
keywords_args(**args) # 1220
```

> How do we define with default args?

```python
keywords_args(one=20) # KeyError: 'two'
```

---

## Python Functions - Function Parameters - Positional and Keywords Arguments - Solution

```python
def keywods_args(**args):
    def t(d,n,v):
        return d[n] if n in d else v 
    return t(args,'one',1) + t(args,'two',2) * t(args,'three',3)
```



---

## Functional Programming - Definition

Wikipedia defines the functional programming:

> … a programming paradigm, a style of building the structure and elements of computer
> programs that treats computation as the evaluation of mathematical functions and
> avoids state and mutable data.

---

## Functional Programming - Definition(2)

1. Functional Programming aims to avoid side effects.
2. Functional Programming avoids concepts such as state.
3. Functional Programming promotes immutable data.
4. Functional Programming promotes declarative programming.

---

## Functional Programming - Advantages

1. Less code.
2. Lack of (hidden) side effects (Referential Transparency)
3. Recursion is a natural control structure.
4. Good for prototyping solutions.
5. Modular Functionality.
6. The avoidance of state-based dehaviour.
7. Additional control structures.
8. Concurrency and immutable data.
9. Partial Evaluation.

---

## Functional Programming  - Disadvantages

1. Input-Output is harder in a purely functional language.
2. Interactive applications are harder to develop.
3. Continuously running programs.
4. Functional Programming Languages have tended to be less efficient on current hardware platforms.
5. No data oriented.
6. Programmers are less familiar with functional programming concepts.
7. Functional Programming Idioms are often less intuitive.
8. Ivory tower languages.

---

## Functional Programming - Referential Transparency

> An operation is said to be *Referential Transparent* if it can be replaced with its corresponding value, without changing the programs behaviour, for a given set of parameters.

```python
def increment(num):
    return num + 1

print(increment(5))
print(increment(5))
```

---

## Functional Programming - Referential Transparency (2)

```python
amount = 1
def increment(num):
    return num + amount
print(increment(5))
amount=2
print(increment(5))
```

