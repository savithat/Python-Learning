# a = [1, 3, 8, 5]

print("Enter the number of elements:")
num = int(input())

li = []

for i in range(num):
    ele = int(input())
    li.append(ele)
print(li)

big = li[0]

for i in range(1,len(li)):
    if big < li[i]:
        big = li[i]
print("maximum num:", big)


small = li[0]

for i in range(1,len(li)):
    if small > li[i]:
        small = li[i]
print("minimum num:", small)



# print("Maximum num:",  min(li))
# print("Maximum num:",  max(li))