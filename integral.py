def function(input):
    return input
def integral(a,b):
    sum = 0
    x = a
    while x < b:
        sum += function(x)*0.0000001
        x += 0.0000001
    return sum
print(integral(1,2))