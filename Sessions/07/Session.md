# Session 06

**Agenda**

- Functional Programming - High-Order Function Concepts
- Functional Programming - High-Order Function Example
- Functional Programming - Curried Functions
- Object-Oriented Programming
- Object-Oriented Programming - Object
- Object-Oriented Programming - Class
- Object-Oriented Programming - Abstraction
- Object-Oriented Programming - Encapsulation
- Object-Oriented Programming - Polymorphism
- Object-Oriented Programming - Association
- Object-Oriented Programming - Aggregation
- Object-Oriented Programming - Composition


-------------------------------------------------------------------------------

## Functional Programming - High-Order Function Concepts

* A function can be assigned to a variable.
* A function can be assigned to an argument of a function.
* A function value can be as a return value of a function.

-------------------------------------------------------------------------------

## Functional Programming - High-Order Function Example

```python
def apply(x, function):
    result = function(x)
    return result

def mult(y):
    return y * 100

apply(5, mult)
```

-------------------------------------------------------------------------------

## Functional Programming - Curried Functions

> Currying is a technique which allows new functions to be created from existing
> functions by *binding* one or more parameters to a specific value.

-------------------------------------------------------------------------------

## Functional Programming - Curried Functions

```python
def multiply(a,b):
   return a * b

multiply(3,2) # 6
multiply(10,2) # 8
```

-------------------------------------------------------------------------------

## Functional Programming - Curried Functions

```python
def curry_second(func, snd):
    return lambda y: func(y, num)

double = curry_second(multiply,2)
triple = curry_second(multiply,3)
```

-------------------------------------------------------------------------------

## Functional Programming - Curried Functions

> **Closure** A closure (or a lexical closure or function closure) is a function
> (or more stricly a reference to a function) together with a referencing environment.
> This referencing environment records the context within which the function was
> originally defined and if necessary, a reference to each of the non-local variables
> used by that function.

```python
more = 100

def increase(num):
    return num + more

print(increase(10)) # 110
more = 50
print(increase(10)) # 60
```

-------------------------------------------------------------------------------

## Functional Programming - Curried Functions

```python
def increment(num):
    return num + 1

def reset_function():
    global increment
    addition = 50
    increment = lambda num : num + addition

print(increment(5)) # 6
reset_function()
print(increment(5)) # 55
```

-------------------------------------------------------------------------------

## Object-Oriented Programming

* Object
* Class
* Abstraction
* Encapsulation
* Inheritance
* Polymorphism
* Association
* Aggregation
* Composition

-------------------------------------------------------------------------------

## Object-Oriented Programming - Interview Advice

> Common questions: **What is ...?**

> The correct answer are a combination of technical knowledge and real-world analogies or examples.

-------------------------------------------------------------------------------

## Object-Oriented Programming - Object

* An object is one the core concepts of OOP.
* An object is real-world entity.
* An object has state (fields) and behaviours  (methods).
* An object represent an instance of a class.
* An object takes up some space in memory.
* An object can communicate with other objects.

-------------------------------------------------------------------------------

## Object-Oriented Programming - Class

* A class is one the core concepts of OOP.
* A class is a template or a blueprint for creating objects.
* A class doesn't consume memory.
* A class can be instantiated multiple times.
* A class does one, and only one thing.

-------------------------------------------------------------------------------

## Object-Oriented Programming - Abstraction

* A class is one the core concepts of OOP.
* Abstraction is the concept of exposing to the user only those things that are revelant to them and hinding the remainder of the details.
* Abstraction allows the user to focus on what the application does instead of how it does it.
* Abstraction is achieved in some languages via abstract classes and interfac

-------------------------------------------------------------------------------

## Object-Oriented Programming - Encapsulation

  * Encapsulation is one the core concepts of OOP.
  * Encapsulation is a technique whereby the object state is hidden from the outer world and a set of public methods for accessing this state are exposed.
  * Encapsulation is achieved when each object keeps its state private, inside a class.
  * Encapsulation is known as the **data-hiding** mecanism.
  * Encapsulation has a number of important advantages associated with it, such as loosely coupled, reusable, secure and easy-to-test code.
  * In Java (for instance) , encapsulation is implemented via the access modifiers . `private`, `public`, `protected`.

-------------------------------------------------------------------------------

## Object-Oriented Programming - Inheritance ##

  * Inheritance is one the core concepts of OOP.
  * Inheritance allows an object to be based on another object.
  * Inheritance sustains code reusability by allowing an object to reuse the code of another object and add its own logic as well.
  * Inheritance is know as an **IS-A** relationship, also referenced as a parent-child relationship.
  * In Python, inheritance is achive via a list parameter in the class definition.
  * The inherited object is referenced as the superclass, and the object that inherites the superclass is reference as the superclass.
  * In Python, multiple inheritance is allowed.


-------------------------------------------------------------------------------

## Object-Oriented Programming - Polymorphism ##

  * Polimorphism is one the core concepts of OOP.
  * Polymorphism means *many forms* in Greek.
  * Polymorphism allows an object to behave differently in certain cases.
  * Polymorphism can be chaped via method overloading or via method overriding in the case of an IS-A relationship.

-------------------------------------------------------------------------------

## Object-Oriented Programming - Association ##

  * Association is one the core concepts of OOP.
  * Association defines the relation between two classes that are independent of another.
  * Association has no owner.
  * Association cab be one-to-one, one-to-many, many-to-one, and many-to-many.

-------------------------------------------------------------------------------

## Object-Oriented Programming - Aggregation ##

  * Aggregation is one the core concepts of OOP.
  * Aggregation is a special cases of unidirectional association.
  * Aggregation represente a **HAS-A** relationship.
  * Two aggregated objects have their own life cycle, but one of the objects is the owner of the HAS-A relationship.

-------------------------------------------------------------------------------

## Object-Oriented Programming - Composition ##

  * Composition is one the core concepts of OOP.
  * Composition is a more restrictive case of aggregation.
  * Composition represent a **HAS-A** relationship that contains an object that cannot exits on its own.
  * Composition sustains code reuse and the visibility control of objects.

-------------------------------------------------------------------------------

## Class Definition

```python
class nameOfClass(SuperClass):
    # init
    # attributes
    # methods
```
