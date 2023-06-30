"""#power
a = 4**2
print("a =",a)

#casting
a = int(3.5)
print("a =",a)

#min-max
a = min(3,5,6)
print("a =",a)

#user input
input = input("Enter an input: ")
print("Your input:",input)

#strings
#length
s = "ataberk"
print(len(s))
#substring
print("Substring 1:",s[2:])
print("Substring 2:",s[2:5])
print("Substring 3:",s[-5:]) #same with first one
#contains
print("Contains:",("ata" in s))

#list
list = []
list.append("house")
list.append("mouse")
list.append("blouse")
print(list)
print("Length:",len(list))
list.insert(1,"grouse")
print(list)
del(list[1])
print(list)
list2 = []
list2.append("house")
list2.append("mouse")
list2.append("blouse")
list.extend(list2)
print(list)
list3 = list + list2
print(list3)

#tuple
x = 2,3,4,5
y = x, "ataberk", "yes"
print(y)
#one element tuple
z = 2,
print(z)

#comparisons
x = 4
y = 5
print(x == y)
a = input()
b = "house"
print(a == b)
print(a is b)

#logical operators
print(not(4 < 5))
print(4 < 5 and 5 < 6)
print(4 < 5 or 5 > 6)

#conditions

if 4 > 5:
    print("1")
elif 3 < 4:
    print("3")
else:
    print("2")

#loops
x = 0
while x < 5:
    print(x,end = " ")
    x+=1
print()
for x in range(1,5,2):
    print(x, end = " ")
print()
list = [1,2,3,4]
for x in list:
    if x == 3:
        continue
    print(x, end=" ")

#methods
def sum(a,b,c = 0): #its users choice to use 2 or 3 parameters
    return a+b+c

print(sum("a","b","c"))
mystery = sum
print(mystery(1,2,3))
print(sum(1,2))
"""

#classes
class Dog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def getAge(self):
        return self._age
    def getName(self):
        return self._name
    def setAge(self,age):
        self._age = age
    def setName(self,name):
        self._name = name
    def __str__(self):
        return "Dog: \nName: "+self._name + "\nAge: "+ str(self._age)

d1 = Dog("Scooby",4)
print(d1)
d1.setAge(6)
d1.setName(d1.getName() + " Doo")
print(d1)