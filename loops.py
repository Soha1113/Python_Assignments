#for loop
for i in range(1, 6):
    print(i)
    
#for loop with list
languages = ["Python", "AI", "ML"]

for lang in languages:
    print(lang)
    
#while loop
i = 1

while i <= 5:
    print(i)
    i += 1
    
#do-while loop (python style)
i = 1

while True:
    print(i)
    i += 1
    if i > 5:
        break
        
#loop with break
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
#loop with continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
#nested for Loop
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
        
#nested loop (pattern printing)
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()
    
#nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1
    
#loop with else
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")
    
#mini program combining all  
    for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()