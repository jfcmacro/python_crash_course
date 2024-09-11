class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def __getattr__(self, attribute):
        print('__get__attr__', attribute)
        return 'default'
        # return self.my_default

    def my_default(self):
        return 'default'
