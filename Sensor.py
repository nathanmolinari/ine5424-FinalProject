from Coordinate_Object import Coordinate_Object

class Sensor(Coordinate_Object):

    id = 0;
    range = 0;
    burden = 0;

    def __init__(self, x, y, range):
        Coordinate_Object.__init__(self, x, y)
        self.range = range;

    def __hash__(self):
        return hash((self.x, self.y, self.range))

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
     return "("+ str(self.x) + ", " + str(self.y) + ", " + str(self.range) + ")"
