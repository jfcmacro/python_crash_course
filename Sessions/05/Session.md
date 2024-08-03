# Session 05

## Functional Programming - Anonymous Functions

1. We want to create a function and use it only once; giving it a name for this one can *pollute* the namespace of the program.
2. It also means that someone might call it when we don't expect them to.

```python
# lambda arguments: expression

double = lambda i : i * i
func0 = lambda: print('no args')
func1 = lambda x : x * x
func2 = lambda x, y: x * y
func3 = lambda one, two, three: one + two * tree

func0()
print(func1(4)) # 16
print(func2(2,4)) # 12
print(func3(1,2,3)) # 7
```

---

## Functional Programming - Functions as Objects

```python
def get_msg():
    return "Hi, Functional Programming"

message = get_msg()
print(message) # Hi, Functional Programming

message = get_msg
print(message) # <function get_msg at 0x7ff37e0a3a60>
```

---

## Functional Programming - High-Order Function Concepts

* A function can be assigned to a variable.
* A function can be assigned to an argument of a function.
* A function value can be as a return value of a function.

---

## Functional Programming - High-Order Function Example

```python
def apply(x, function):
    result = function(x)
    return result

def mult(y):
    return y * 100

apply(5, mult)
```



