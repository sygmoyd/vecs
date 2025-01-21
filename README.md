# vecs
a python implementation of real-valued vectors with a custom inner product

## Installation
1. clone this repository:
   ```bash
   git clone https://github.com/sygmoyd/vecs.git
## Useage
### create an vector
to create an n-dimensional vector
```python
vector = vec([1,2,...,n])
```
### print the entries of an vector
```python
print(vector.value)
```

### add/subtract vectors
both vectors must have the same length
```python
vector1 + vector2
vector1 - vector2
```
this returns an new vector

### scale an vector by scalar
```python
vector.scale(3)
```

### calculate the dotProduct
both vectors must have the same length
```python
vector1.dotP(vector2)

#this also works with an list
vector1.dotP([1,2,...,n])
```

### calculate l1 / l2 norm
```python
vector.l1Norm()
vector.l2Norm()
```

### create an inner product
to create the inner product you first must create an calculation blueprint, here is an example for the dotProduct
```python
def dotPCalc(v1,v2):
    s = 0
    for a,b in zip(v1.value, v2.value):
        s += a*b
    return s
```
with this you can create an inner product via the InnerProduct-Class
```python
dotP = InnerProduct(dotPCalc)
```
and use it with the func-method
```python
dotP.func(vector1, vector2)
```
both vectors must have the same length  
you can also use the func-method with lists
```python
dotP.func([1,2,3],[4,5,6])
```
in general this means
```python
InnerProduct(innerProductCalc).func(vector1, vector2)
```

### calculate the norm of an vector
to calculate the norm of an vector with respect to an specific inner product you can use the Norm-method,  
where you pass an inner product calculation blueprint
```python
vector.Norm(innerProductCalc)
```
if you dont pass an inner product, this method will be using the dotProduct

### calculate the angle between 2 vectors
to calculate the angle between two vectors with respect to an specific inner product you can use the Angle-method,  
where you pass an inner product calculation blueprint
```python
vector1.Angle(vector2, innerProductCalc=innerProductCalc, deg=True)
```
if you dont pass an inner product, this method will be using the dotProduct

### calculate the distance between 2 vectors
to calculate the distance between two vectors with respect to an specific inner product you can use the dist-method,  
where you pass an inner product calculation blueprint
```python
vector1.dist(vector2, innerProductCalc=innerProductCalc)
```
if you dont pass an inner product, this method will be using the dotProduct

## Example
```python
#create 3-dimensional vectors
v1 = vec([1,2,3])
v2 = vec([3,2,2])

#create inner product calculation blueprint for an weighted dotProduct
def weightedDotPCalc(v1,v2):
    s = 0
    for a,b in zip(v1.value, v2.value):
        s += a*b*5
    return s

#calculate the distance between v1 and v2 with respect to this weighted dotProduct
v1.dist(v2, innerProductCalc=weightedDotPCalc)

#calculate the l2Norm of the sum of v1 and v2
(v1+v2).l2Norm()
```



