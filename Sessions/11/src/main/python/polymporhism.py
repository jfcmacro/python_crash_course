from person import Person

class Employee(Person):
    def eat(self): print('Employee - Eat')
    def drink(self): print('Employee - Drink')
    def sleep(self): print('Employee - Sleep')

class SalesPerson(Employee):
    def eat(self): print('SalesPerson - Eat')
    def drink(self): print('SalesPerson - Drink')

class Dog:
    def eat(self): print('Dog - Eat')
    def drink(self): print('Dog - Drink')
    def sleep(self): print('Dog - Sleep')
