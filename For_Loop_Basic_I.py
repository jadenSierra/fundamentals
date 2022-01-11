
#Basics

for x in range(0,101):
    print(x)

#Multiples of 5

for y in range(5,1001,5):
    print(y)


#Counting the Dojo Way

for z in range(1,101):
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)

#Whoa that Sucker's Huge

sum = 0

for s in range(0,500000):
    if s % 2 == 1:
        sum+=s
print(sum)

#countdown by 4
for p in range(2018,0,-4):
    print(p)

#flexible counter

lowNum = 2
highNum = 9
mult = 3

for m in range(lowNum,highNum + 1):
    if m % mult == 0:
        print(m)