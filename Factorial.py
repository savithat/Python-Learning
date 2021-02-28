def Factorial(x):
    y = 1
    if (x == 0  or x==1):
        y
    else:
        for i in range(1, x+1, 1):
            y*= i

    print("Factorial of a number {} is = {}".format(x, y))

Factorial(9)




