# Session 06

**Agenda**

  * Class Definition
  

-------------------------------------------------------------------------------

## Class Definition

```python
class nameOfClass(SuperClass):
    # init
    # attributes
    # methods
```

-------------------------------------------------------------------------------

## Class Definition - Intrinsic Attributes

### Classes have the following intrisic attributs

  * `__name__` the name of the class
  * `__module__` the module (or library) from which it is loaded
  * `__bases__` a collection of its base clases
  * `__dict__` a dictionary containing all the attributes (including methods)
  * `__doc__` the documentation string

### For objects

  * `__class__` the name of the class of the object
  * `__dict__` a dictionary containing all the objects attributes

-------------------------------------------------------------------------------

## Class Definition - Special Functions

  * `__str__`
  * `__repr__`

-------------------------------------------------------------------------------

## Class Definition - Class Side Data

```python
class Something:
    """An example of class to hold a class attribute"""
    instance_count = 0
    def ___init___(self,value):
        instance_count += 1
        self.value = value
        self.id = instance_count
```

-------------------------------------------------------------------------------

## Class Definition - Class Side Methods

```python
class Something:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def decrement_instance_count():
        Something.instance_count -= 1
```

-------------------------------------------------------------------------------

## Class Definition - Inheritance

```python
class SomethingElse(Something):
    def __init__(self,value):
        super().__init(value)
```

-------------------------------------------------------------------------------

## Class Definition - The Class Object and Inheritance

-------------------------------------------------------------------------------

## Class Definition - Property

```
<property_name> = property(fget = None, fset = None, fdel = None, doc=None)
```

-------------------------------------------------------------------------------

## Class Definition - Property (Decorators)

* `@property`
* `@property.setter`
* `@property.deleter`

-------------------------------------------------------------------------------

