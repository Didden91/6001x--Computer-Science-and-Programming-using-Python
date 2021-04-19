class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    
    def __eq__(self, self2):
        return self.x == self2.x and self.y == self2.y
    
    def __repr__(self):
        return "Coordinate("+ str(self.x) + ',' + str(self.y)+")"
    
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

a = Coordinate(3,4)
b = Coordinate(3,3)
c = Coordinate(3,4)

print(a == c)

