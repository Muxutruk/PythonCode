import math
def function(input = float):
    return math.log(input)

def closeslope(point):
    return (function(point+0.0000002)-function(point+0.0000001))*10000000


for i in range(1,10):
   print(f"{i}: {round(closeslope(i),5)}")