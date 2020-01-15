class Vector:

    def __init__(self, val):
        if not isinstance(val, list) or len([f for f in val if isinstance(f, float)]) != len(val):
            print("Vector __init__ error : list of float expected")
            raise Exception
        self.values = val
        self.size = len(val)
        print("Vector __init__ succeed")

    @classmethod
    def fromsize(cls, size):
        if not isinstance(size, int):
            print("Vector fromsize error : int expected")
            raise Exception
        values = [float(i) for i in range(0, size)]
        return cls(values)

    @classmethod
    def fromrange(cls, ra):
        if not isinstance(ra, tuple) or len(ra) != 2 or len([i for i in ra if isinstance(i, int)]) != len(ra):
            print("Vector fromrange error : tuple of 2 int expected")
            raise Exception
        values = [float(i) for i in range(ra[0], ra[1])]
        return cls(values)

    def __str__(self):
        txt = ""
        txt += "size = {}\n".format(self.size)
        txt += "values = {}\n".format(self.values)
        return txt
    
    def __repr__(self):
        txt = ""
        txt += "size = {}\n".format(self.size)
        txt += "values = {}\n".format(self.values)
        return txt

    def __add__(self, other):
        if isinstance(other, Vector):
            if (other.size != self.size):
                print("Vector operator dimension error\n")
                raise Exception
            return Vector([self.values[i] + other.values[i] for i in range(self.size)])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector([self.values[i] + float(other) for i in range(self.size)])

    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            tmp = Vector([-x for x in other.values])
        elif isinstance(other, int) or isinstance(other, float):
            tmp = other * -1
        return self.__add__(tmp)
        
    def __rsub__(self, other):
        tmp = Vector([float(other)])
        return tmp.__sub__(self)
   
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector([x * float(other) for x in self.values])
        if isinstance(other, Vector) and self.size == other.size:
            return Vector([self.values[i] * other.values[i] for i in range(self.size)])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            if (other.size != 1):
                print("Vector __div__ error : only scalars\n")
                raise Exception
            return Vector([self.values[i] / other.values[0] for i in range(self.size)])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector([self.values[i] / float(other) for i in range(self.size)])

    def __rtruediv__(self, other):
        if (self.size != 1):
            print("Vector __div__ error : only scalars\n")
            raise Exception
        tmpv = Vector([float(other)])
        return tmpv.__truediv__(self)

