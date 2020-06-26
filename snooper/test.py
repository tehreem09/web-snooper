# import os
#
# print(os.path.isfile('new.txt'))


x = []

y=[1,2,3,4,5,6,7,7]
for z in y:
    x.append(z)
# print(x)
sides = [i for i in range(4)]
print(sides)
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
print("...")
for i in mygenerator:
    print("...")
    print(i)

