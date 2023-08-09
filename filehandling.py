
a = 10
w = open("mohit.txt","wi")

w.write(a)

w.close()

p = open("mohit.txt",'r')
l = p.read()
print(l)

p.close()

