from Logger import Logger

class Cursor(object):
    # Set up the descriptors at the class level
    x = Logger('x')
    y = Logger('y')
    def __init__(self, x0, y0):
        # Initialise the attributes
        # Note use of __dict__ to avoid using self.x notation
        # which would invoke the descriptor behaviour
        self.__dict__['x'] = x0
        self.__dict__['y'] = y0
    def move_by(self, dx, dy):
        print('move_by', dx, ',', dy)
        self.x = self.x + dx
        self.y = self.y + dy
    def __str__(self):
        return 'Point[' + str(self.__dict__['x']) + ', ' + str(self.__dict__['y']) + ']'
