# a = 10
# b = 80
# c = 30
# d = 40

# if a>b:
#     if a>c:
#         if a>d:
#             print(a)
#         else:
#             print(d)
#     else:
#         if c>d:
#             print(c)
#         else:
#             print(d)
# else:
#     if b>c:
#         if b>d:
#             print(b)
#         else:
#             print(d)
#     else:
#         if c>d:
#             print(c)
#         else:
#             print(d)




# if :


# else if :


# else if:



# a = [10,20,30,40,50,"mohit",1.5,True]
# print(a)


# a = [10,20,30,40,"Mohit"],30,40,"Mohit"]

# even = [2,4,6,8,10,12]
# odd = [1,3,5,7,9,11,13,17,19,21,23,25]

# even = [2,4,6,8,10,12]
# odd = [1,3,5,7,9,11,13,17,19,21,23,25]
# a.append("Apple")
# a.pop()
# a.pop()
# print(a)

# for i in a:
#     print(i)


# a = [10,55,88,9,8,4,5,6]
# b = a.pop()
# c = a[0]
# a.append(c)
# a[0] = b
# print(a)

# a = [10,55,88,9,8,4,5,6]

# for i in range(len(a)):

#     if a[i]>=50:
#         a[i] = "Pass"
#     else:
#         a[i] = "fail"

# print(a)


name = ["mohit","rohit","ankit","aman"]

a = 1

while a!=0:
    
    a = int(input("1 for checking , 2 insert , 3 delete , 4 print list , 0 Exit  "))

    if a == 1:

        n = input("Enter Your name :")

        if n in name:
            print("Yes your name is exist in list")
        else:
            print("Your name is not exist in list")

    elif a==2:

        n = input("Enter Your name for inserting in list")
        name.append(n)

    elif a==3:

        n = input("Enter Your name for deleting :")
        name.remove(n)

    elif a==4:

        print(name)




