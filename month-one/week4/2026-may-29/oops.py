# from  abc import ABC,abstractmethod
# class animal(ABC):
#      @abstractmethod
#      def sound(self):
#          pass
# class dog(animal):
#     def __init__(self,behaviour):
#         self.behaviour = behaviour
#     def sound(self):
#         return self.behaviour
# class cat(animal):
#     def sound(self):
#         print("meow")
# d1 = dog("braking")
# c1 = cat()
# c1.sound()
# print(d1.sound())


#Encapsulation................................................................

# class encapsulation():
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def result(self):
#         if self.__age > 21:
#             print("eligible")
#         else:
#             print("not eligible")
            
            
#             #get the private acess specifier................................
#     def get_age(self):
#         return self.__age
        
        
#         #set means modify the acess specifier......................
#     def set_age(self,age):
#         self.__age = age
      

# cl = encapsulation("amal",22)
# cl.result()
# print(cl.get_age())
# cl.set_age(23)
# print(cl.get_age())




#@class method............................ and @property............................................

# class student:
#     @property
#     def normal_method(self):
#         return "object_method"
#     @classmethod
#     def class_method(cls):
#         return "class_method"

# s1 = student()        
# print(s1.normal_method)
# print(student.class_method())



