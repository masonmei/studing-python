# coding=utf-8

# import mylib
from mylib import Person

__author__ = 'mason'

# print something in the console.
print("hello mason")


# define vars
a = 10
b = 2.3

c = a + b
print(c)

# define flows
scope = 90
if (scope > 90):
    print ("OK")
else:
    print "你好"


# loop
count = 10
sum = 0
for i in range(0, count):
    sum += i
    print("Item {0}, total {1}".format(i, sum))

count = 10
while count > 0:
    count -= 1
    print(count)


# define function
def sayHello():
    print("Hello world")


sayHello()


def compare(a, b):
    if a > b:
        print a
    else:
        print b


compare(10, 4)

# person = mylib.Person("fucker")
# person.getName();

person = Person("fucker")
person.getName()
