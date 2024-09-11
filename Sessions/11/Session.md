# Session - Protocols, Polymporhism, and Descriptos

**Agenda**

-------------------------------------------------------------------------------

## Implicit Contracts

* Calculator example

-------------------------------------------------------------------------------

## Duck Typing

> If it walks like a duck, swims like a duck and quacks like a duck then it’s a Duck!

-------------------------------------------------------------------------------

## Protocols

> How do you know what is required?

** Protocol **

> A Protocol is an informal description of the programmer interface provided
> by something in Python (for example a class but it could also be a module
> or a set of stand-alone functions).

-------------------------------------------------------------------------------

## An Protocol Example

> There is a protocol for defining Sequences, such as a container that can
> be accessed an item at a time.
> This protocol requires that any type that will be held in the container must
> provide the `__len__()` and `__getitem__()` methods.

-------------------------------------------------------------------------------

## The Context Manager Protocol

* It is associated with the `with as` statement.
* This statement is typically used with classes which will 
  need to allocate, and release so called *resources*.
* These resources could be files, or database connections etc.
* The 'with as' statement ensures that any set up steps are 
  performed before an object is available for use and that
  any shut down behaviour is invoked when it is finished with.

-------------------------------------------------------------------------------

## The Context Manager Protocol

**Syntax**

```python
with <managed_object> as <localname>:
    # Code to use managed object via <localname>
```

**Example**

```python
with ContextManagedClass() as cmc:
    print('In with block', cmc)
    print('Existing')
```

-------------------------------------------------------------------------------

## Then Context Manager Protocol

* `__enter__()`
* `__exit__()`

-------------------------------------------------------------------------------

## Polymorphism

> It is essentially the ability to request that the same operation be
> performed by a wide range of different types of things.

```python
def night_out(p):
    p.eat()
    p.drink()
    p.sleep()
```

-------------------------------------------------------------------------------

## The Descriptor Protocol

* Descriptors can be used to create what are known as *managed attributes*.
* A managed attribute is an object attributes that is managed (or protected)
  from direct access by external code via the descriptor.
* The descriptor protocol defines four methods
  * `__get__(self, instance, owner)`
  * `__set__(self, instance, value)`
  * `__delete__(self, instance)`
  * `__set_name__(self, owner, name)`


