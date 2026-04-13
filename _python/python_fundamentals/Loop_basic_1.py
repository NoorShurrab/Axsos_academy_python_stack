# Task 1
for i in range(151):
    print(i)

# Task 2
for j in range(5, 1001):
    if j % 5 == 0:
        print(j)

# Task 3
for n in range(1, 101):
    if n % 10 == 0:
        print("Coding Dojo")
    elif n% 5 == 0:
        print("Coding")

# Task 4
sum  = 0
for k in range(1, 500001):
    if k % 2 != 0:
        sum += k
        print(sum)

# Task 5 
for m in range(2018, 0, -4):
    print(m)

#Task 6
lowNum = 4
highNum = 40
mult = 5
for p in range(lowNum, highNum + 1):
    if p % mult == 0:
        print(p)