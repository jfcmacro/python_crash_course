class Logger(object):
    """ Logger class implementing the descriptor protocol"""
    def __init__(self, name):
        self.name = name
    def __get__(self, inst, owner):
        print('__get__:', inst, 'owner', owner, ', value', self.name, '=', str(inst.__dict__[self.name]))
        return inst.__dict__[self.name]
    def __set__(self, inst, value):
        print('__set__:', inst, '-', self.name, '=', value)
        inst.__dict__[self.name] = value
    def __delete__(self, instance):
        print('__delete__', instance)
    def __set_name__(self, owner, name):
        print('__set_name__', 'owner', owner, 'setting', name)
