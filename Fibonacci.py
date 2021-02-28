print("Enter the number for fibonacci series: ")
num = int (input())


def Fibonacci(num):
    n1 = 0
    n2 = 1
    print(n1, n2, end=" ",)
    for i in range(2, num):
        sum = n1 + n2
        print(sum, end=" ")
        n1 = n2
        n2 = sum

Fibonacci(num)