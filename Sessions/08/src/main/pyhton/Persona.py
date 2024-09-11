class Person:
    """
    This is super definition of a class in Python
    """
    instance_count = 0
    def __init__(self,name):
        self.id = Person.instance_count
        Person.increment_count()
        self.name = name ## self.__dict__["name"] = name

    @classmethod
    def increment_count(cls):
        cls.instance_count += 1

    def info(self):
        print(f"Class Name: {Person.__name__}")
        print(f"Class Module: {Person.__module__}")
        for base in Person.__bases__:
            print(f"Class base: {base}")
            
        for (key,value) in Person.__dict__.items():
            print(f"key: {key} value: {value} type: {type(value)}")

        print(f"Doc: {Person.__doc__}")

        print(f"Class: {self.__class__}")
        # self.__dict__["get_id"] = lambda _ : self.id
        self.__dict__["get_id"] = lambda: self.id

    def __str__(self): # Analog Java method toString()
        return f"id: {self.id} Name: {self.name}"

    # eval(repr(o)) == o
    def __repr__(self):
        return f"Person('{self.name}',{self.id})"

p1 = Person("Juan")
p2 = Person("Jesica")
p3 = Person("Arturo")
p4 = Person("Makemake")
p5 = Person("Ricard")
