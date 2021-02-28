
names = ("savi","sanju", "nidhi", "jags")
marks = (10, 20, 20, 40)
Empdata = ("savi", 10, 5.3, True)

for i in range(len(Empdata)):
    print(Empdata[i], end = " ")




L = len(Empdata)
print(L)
print("  ".join(Empdata[i] for i in range(L)))

#print(Empdata[3])
#print(Empdata[-1])


print(names[-3:-4:-1])

# #tuple is immutable, cann't add any element after u defined
# names[1] = "dad"



L=len(names)

for i in range(L):
    print(names[i], end=" ")
print()



"""
#print like this:   s, a, v, i next line s, a, n, j, u for all names

L = len(names)

for i in range(L):
    print(", ".join(names[i]))
"""





# #print like this:   savi, sanju, nidhi, jags
#
# L = len(names)
# print(", ".join(names[i] for i in range(L)))


