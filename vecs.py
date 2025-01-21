import math

class vec:
    def __init__(self, value=[]):
        if value == []: self.value = [];return 
        if not all(isinstance(item, (int, float)) for item in value):
            raise TypeError("all elements must be ints, floats or bools!")
        self.value = value

    def __add__(self, vec2):
        if not len(self.value) == len(vec2.value): raise ValueError("vectors must have the same length")
        value = [a+b for a, b in zip(self.value, vec2.value)]
        return vec(value)

    def __sub__(self, vec2):
        if not len(self.value) == len(vec2.value): raise ValueError("vectors must have the same length")
        value = [a-b for a,b in zip(self.value, vec2.value)]
        return vec(value)

    def scale(self, scalar):
        for idx, i in enumerate(self.value):
            self.value[idx] = scalar*i
    
    def dotP(self, vec2):
        if not type(vec2) is vec:
            vec2 = vec(vec2)
        if not len(self.value) == len(vec2.value): raise ValueError("vectors must have the same length")
        s = 0
        for a,b in zip(self.value, vec2.value):
            s += a*b
        return s

    def Norm(self, innerProduct=None):
        if innerProduct == None: innerProduct = self.dotP
        s = innerProduct(self.value)
        return s ** 0.5
    
    def l1Norm(self):
        s = 0
        for i in self.value:
            s += abs(i)
        return s
    
    def l2Norm(self):
        return self.Norm()

    def Angle(self, vec2, innerProduct=None, deg=True):
        if innerProduct == None: numerator=self.dotP(vec2)
        else: numerator=innerProduct(vec2)
        vec1Norm = self.Norm(innerProduct=innerProduct)
        vec2Norm = vec2.Norm(innerProduct=innerProduct)
        denumerator=vec1Norm*vec2Norm
        cos_val = numerator/denumerator
        if deg: return math.degrees(math.acos(cos_val))
        return cos_val
