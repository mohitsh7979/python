# class A:

#     name = "Mohit"
#     age = 20
#     address = "Jaipur"

#     def getoutput(self,name,age,address):

#         print(name,age,address)



# o1 = A()

# o1.getoutput("mohit",20,"Jaipur")


# class A:

#     # id = 1
#     # name = "mohit"
#     # age = 18
#     # address = "Jaipur"
    
#     def __init__(self,id,name,age,address):
        
#         self.id = id
#         self.name = name
#         self.age = age
#         self.address = address

#     def myinput(self):
#         self.id = input("Enter Your id : ")
#         self.name = input("Enter Your name : ")
#         self.age = input("Enter Your age : ")
#         self.address = input("Enter Your address : ")


        
#     def getoutput(self):

#         print(self.id,self.name,self.age,self.address)



# o1 = A(1,"mohit",18,"address")

# o1.myinput()

# o1.getoutput()



# Inheritance


# class A:

#     def __init__(self,id,name):
#         self.id = id
#         self.name = name

#     def getoutput(self):
#         print(self.id,self.name)


# class B(A):

#     def __init__(self,age,address,id,name):

#         super().__init__(id,name)


# x = B(1,"mohit",18,"jaipur")

# x.getoutput()



class A:

    def __init__(self,id,name,address):

        self.id = id 
        self.name = name
        self.address = address

    def getoutput(self):

        print(self.name,self.address,self.id)


class B(A):

  
    def myoutput():

        print("MY NAME IS MOHIT SHARMA")


        


o1 = A(1,"mohit","jaipur")

o1.getoutput()

o2 = B()

o2.getoutput()
o2.myoutput()



