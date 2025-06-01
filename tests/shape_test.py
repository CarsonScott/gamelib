from gamelib import *

shape=Rectangle([0,0], [100,100])
shape.rotate(1)
print(shape.contains([25,25]))
print(shape.points)
print(shape.polygon)