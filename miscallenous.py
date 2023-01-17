def factorial(num = int):
    result = 1
    
    for x in range(1,num):
        result = result*(x)
    return result
def fibbonaci(num = int):
    if num < 1:
        return("Enter a positive number equal or more than 1")
    elif num in [1,2]:
        return("1")
    else:
        old = 1
        new = 1
        for _ in range(num-2):
            result = old + new
            old = new
            new = result
        return result
def factors(num):
    factorlist = []
    for i in range(1,num+1):
        if num % i == 0:
            factorlist.append(i)
    preetyfacotrs = ""
    for n in range(0,len(factorlist)-1):
        preetyfacotrs = preetyfacotrs + f"{factorlist[n]}, "
    return preetyfacotrs[0:-1] + " " + str(num)

for i in range(5):
    print(f"{i}! = {factorial(i)}")

for i in range(10):
    print(f"F({i}) = {fibbonaci(i)}")

for i in range(135,145):
    print(f"factors of {i}: {factors(i)}")

print(factorial(20))