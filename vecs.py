import math

def dotPCalc(v1,v2):
    s = 0
    for a,b in zip(v1.value, v2.value):
        s += a*b
    return s

class InnerProduct:
    def __init__(self, calc):
        self.calc = calc

    def func(self, vec1, vec2):
        if not type(vec1) is vec: vec1 = vec(vec1)
        if not type(vec2) is vec: vec2 = vec(vec2)
        if not len(vec1.value) == len(vec2.value): raise ValueError("vectors must have the same length")
        return self.calc(vec1, vec2)

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
        dp = InnerProduct(dotPCalc)
        return dp.calc(self, vec2)
        
    def Norm(self, innerProductCalc=None):
        if innerProductCalc == None: return math.sqrt(self.dotP(self.value))
        innerProduct = InnerProduct(innerProductCalc)
        return math.sqrt(innerProduct.calc(vec(self.value), vec(self.value)))
    
    def l1Norm(self):
        s = 0
        for i in self.value:
            s += abs(i)
        return s
    
    def l2Norm(self):
        return self.Norm()

    def Angle(self, vec2, innerProductCalc=None, deg=True):
        if innerProductCalc == None: numerator=self.dotP(vec2)
        else: numerator= InnerProduct(innerProductCalc).func(vec(self.value), vec2)
        vec1Norm = self.Norm(innerProductCalc=innerProductCalc)
        vec2Norm = vec2.Norm(innerProductCalc=innerProductCalc)
        denumerator=vec1Norm*vec2Norm
        cos_val = numerator/denumerator
        if deg: return math.degrees(math.acos(cos_val))
        return cos_val
