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
        val2 = vec2
        if type(vec2) is vec:
            val2 = vec2.value
        s = 0
        for a,b in zip(self.value, val2):
            s += a*b
        return s

    def Norm(self, vec2, innerProduct=None):
        if innerProduct == None: innerProduct = self.dotP
        s = innerProduct(vec2)
        return s ** 0.5
    
    def l1Norm(self):
        s = 0
        for i in self.value:
            s += abs(i)
        return s
    
    def l2Norm(self):
        return self.Norm(self.value) 
