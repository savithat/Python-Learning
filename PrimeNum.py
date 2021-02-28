def Prime_num(x):
    count = 0
    if x > 1:
        for i in range(1, x+1):
            if(x%i == 0):
                count += 1
        if count == 2:
            print("number {} is prime".format(x))
        else:
            print("number {} is not prime".format(x))


Prime_num(11)



