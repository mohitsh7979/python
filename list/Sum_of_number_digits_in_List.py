a = [12, 67, 98, 34]

b = []

for i in a:
    
    total = 0

    while i>0:

        x = int(i%10)
        i = int(i/10)
        total = int(total + x)
    
    b.append(total)

print(b)
