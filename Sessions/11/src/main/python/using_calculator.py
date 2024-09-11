from Calculator import Calculator
from distance import Distance

calc = Calculator()

print('calc.add(3, 4):', calc.add(3, 4))
print('calc.add(3, 4.5):', calc.add(3, 4.5))
print('calc.add(4.5, 6.2):', calc.add(4.5, 6.2))
print('calc.add(2.3, 7):', calc.add(2.3, 7))
print('calc.add(-1, 4):', calc.add(-1, 4))

d1 = Distance(5)
d2 = Distance(10)
print(f'calc.add({str(d1)},{str(d2)}):{str(calc.add(d1,d2))}')
print(f'calc.substract({str(d1)},{str(d2)}):{str(calc.add(d1,d2))}')

