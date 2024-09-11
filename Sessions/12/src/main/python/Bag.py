class Bag:
    def __init__(self):
        self.data = ['a','b','c']

    def __getitem__(self, pos):
        return self.data[pos]

    def __str__(self):
        return 'Bag(' + str(self.data) + ')'

    def __getattribute__(self,name):
        print('Buscando attributo')
        return object.__getattribute__(self, name)
    
    def __getattr__(self,name):
        print('__getattr__')
        return 'default'


def get_length(self):
    return len(self.data)
