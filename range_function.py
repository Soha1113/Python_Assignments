#range() practice
#basic range() (stop only)
for i in range(5):
    print(i)
    
#range(start, stop)
for i in range(1, 6):
    print(i)
    
#range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
    
#negative step (reverse range)
for i in range(10, 0, -1):
    print(i)
    
#using range() with while loop
i = 0
r = range(5)

while i < len(r):
    print(r[i])
    i += 1
    
#converting range() to list
numbers = list(range(1, 6))
print(numbers)

#using range() with index
names = ["AI", "ML", "DL"]

for i in range(len(names)):
    print(i, names[i])
    
#nested loop with range()
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        
#using range() for table
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
#checking membership in range()
r = range(1, 10)

print(5 in r)
print(15 in r)

#slicing a range()
r = range(0, 10)
print(list(r[2:7]))

#sum of numbers using range()
total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)

#mini practice program (all in.one)
r = range(2, 12, 2)

for i in r:
    print(i)
print(list(r))