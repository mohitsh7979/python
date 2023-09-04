# def value(func,l):
    
#     result = 0

#     for i in l:

#         if func(i):

#             result = result + i
    

#     return result


# x = lambda a : a%2==0
# y = lambda a : a%2!=0
# z = lambda a : a%3==0

# l = [11,12,5,6,12,9,8]

# ans1 = value(x,l)
# ans2 = value(y,l)
# ans3 = value(z,l)
# print(type(ans1))


# def check_no(func,d1,d2):

#     if func(d1,d2)%2==0:
#         return 'yes'

# x = lambda a,b : a+b
# y = lambda a,b : a-b
# z = lambda a,b : a*b

# print(check_no(x,10,2))
# print(check_no(y,10,1))
# print(check_no(z,10,2))




# def check_no(func,l):
#     pass

# flag = 0
# x = lambda a : [i for i in range(2,a) flag = 1 if a%i==0 ]

# print(x(7))



# Map function


# a = [10,20,30,40,50]
# y = list(map(lambda x:x*2,a))
# print(y)


# z = list(filter(lambda x:x>30,a))
# print(z)


# for reduce use first of all import functools

from functools import reduce
y = [10,20,300,40,50]
# z = reduce(lambda a,b:a+b,y)
# print(z)

z = reduce(lambda x,y:x if x>y else y,y)
print(z)






