# a = [1, 2, 3, 4]

arr_num = []
num = int(input("enter the number of elements: "))

for i in range(0, num):
    ele = int(input())
    arr_num.append(ele)
print(arr_num)


# sum = 0
# for i in range(len(arr_num)):
#     sum += arr_num[i]

Tot = sum(arr_num)
print("sum of an array:", Tot)


Tot = sum((arr_num), 10)
print("sum of an array:", Tot)



# # num of ana array of elements
# a= [1,2,7]
# print("sum of an array elements:", sum(a))