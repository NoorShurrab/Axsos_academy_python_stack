def a():
    return 5
print(a())
# 1- T-Diagram
# no variables, no parameters | return 5

def a():
    return 5
print(a()+a())
# 2-  T-Diagram
# no variables, no parameters | return 10

def a():
    return 5
    return 10
print(a())
# 3- T-Diagram
# no variables, no parameters | return 5

def a():
    return 5
    print(10)
print(a())
# 4-  T-Diagram
# no variables, no parameters | return 5

def a():
    print(5)
x = a()
print(x)
# 5- T-Diagram
# no parameters | print 5 and none

def a(b,c):
    print(b+c)
    print(a(1,2) + a(2,3))
# 6- T-Diagram
# b=1 c=2 | 3 return none
# b=2 c=3 | 5 return none
# none + none = nothing to print

def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# 7- T-Diagram
# b=2 c=5 | 25

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# 8- T-Diagram
# b=100 | 100 and return 10

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3

print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# 9- T-Diagram
# b=2 c=3 | return 7
# b=5 c=3 | return 14
# return 7 + return 14 = 21

def a(b,c):
    return b+c
    return 10
print(a(3,5))
# 10- T-Diagram
# b=3 c=5 | return 8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# 11- T-Diagram
# b=500 | print 500
# a() | b=300
# b=500
# call a() | print 300
# b=500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# 12- T-Diagram
# b=500 | print 500
# a() b=300
# print 500
# call a() | print 300
# print 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# 13- T-Diagram
# b=500 | print 500
# a() b=300
# print 500
# call a() | print 300 | b=300
# print 300

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# 14- T-Diagram
# call a() | print 1, call b() print 3, print 2

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# 15- T-Diagram
# call a()
# print 1
# call b() | print 3  | return 5
# return 10