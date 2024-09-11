def logger(func):
    def inner():
        print('calling ', func.__name__)
        func()
        print('calling ', func.__name__)
    return inner
