# 1. Write a program to store seven fruits in a list entered by the user

'''

frt = []

f1 = input("enter the fruits name : ")
frt.append(f1)
f2 = input("enter the fruits name : ")
frt.append(f2)
f3 = input("enter the fruits name : ")
frt.append(f3)
f4 = input("enter the fruits name : ")
frt.append(f4)
f5 = input("enter the fruits name : ")
frt.append(f5)
f6 = input("enter the fruits name : ")
frt.append(f6)
f7 = input("enter the fruits name : ")
frt.append(f7)
apl
print(frt)


smal version

frt = []
for i in range(7):
    frt.append(input("Enter fruit " + str(i+1) + ": "))
print(frt)


'''

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

'''
std = []
for i in range(6):
    std.append(int(input("enter the student marks" + str(i+1) + ":")))
std.sort()
print(std)
'''

# 3. Check that a tuple type cannot be changed in python.

'''
cant change tuple because its unmutable
'''

# 4. Write a program to sum a list with 4 numbers.
'''
a = [4,8,6,3,2,1,70]
print(sum(a))


# other diff.

a = [4,8,6,3,2,1,70]
b = [x + 4 for x in a]
print(b)
'''


# 5. Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)

'''
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
'''