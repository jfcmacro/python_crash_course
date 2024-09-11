from Cursor import Cursos

cursor = Cursor(15, 25)
print('-' * 25)

print('p1:', cursor)
cursor.x = 20
cursor.y = 35
print('p1 updated:', cursor)
print('p1.x:', cursor.x)
print('-' * 25)
cursor.move_by(1, 1)
print('-' * 25)
del cursor.x
