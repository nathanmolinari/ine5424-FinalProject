import Geohash
from Coordinate_Object import Coordinate_Object

class Sensor(Coordinate_Object):

    id = 0;
    range = 0;

    def __init__(self, x, y):
        Coordinate_Object.__init__(self, x, y)
        self.id = Geohash.encode(x, y);
        self.range = 8;

    def decode_id(self):
        return Geohash.decode(self.id)

    def __hash__(self):
        return hash((self.x, self.y, self.range))

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
     return "("+ str(self.x) + ", " + str(self.y) + ")"
