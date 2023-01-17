def PointAndSlope(point = tuple,slope = float):
    n = point[1] - slope*point[0]
    return f"Eq: y = {slope}x + ({n})"  
def TwoPoints(point1 = tuple, point2 = tuple):
    slope1 = (point2[1]-point1[1])/(point2[0]-point1[0])
    return PointAndSlope(point1, slope1)
def FindRoot(m = float,n = float):
    return f"Root:{-n/m}"
def Yintercept(m = float,n = float):
    return f"Y Intercept: {n}"

print(PointAndSlope((1,1), 2))
print(TwoPoints((6,5),(1,3)))
print(FindRoot(2,-3))