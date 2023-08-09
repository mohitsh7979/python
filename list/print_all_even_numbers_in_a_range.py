a = int(input("Starting Number :"))
b = int(input("Ending Number :"))

prime_number_list = []


for i in range(a,b):

    flag = 0
    for j in range(2,a):

        if int(a%j) == 0:

            flag = 1
    
    if flag ==0:
        prime_number_list.append(i)

print(prime_number_list)
