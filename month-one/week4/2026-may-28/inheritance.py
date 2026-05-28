# class animal():
#     def sound(self):
#         print("braking")
# class dog(animal):
#     pass
# d=dog()
# d.sound()

        
        
        
# class animal():
#      def sound(self):
#          print("noise")
          
# class dog(animal):
#      def bark(self):
#          print("braking")
# d=dog()
# d.sound()
# d.bark()
        
        
        #   single level inheritance.......................
   
# class Father:
#     def bike(self):
#         print("Father has a bike")

# class Son(Father):
#     def laptop(self):
#         print("Son has a laptop")

# s = Son()

# s.bike()
# s.laptop()


          #multi level inheritance............................................
    
       
# class Grandfather:
#     def land(self):
#         print("Grandfather has land")

# class Father(Grandfather):
#     def bike(self):
#         print("Father has a bike")

# class Son(Father):
#     def laptop(self):
#         print("Son has a laptop")

# s = Son()

# s.land()
# s.bike()
# s.laptop()
  
  
  
  
                     # multiple inheritance............................
                     
                     
# class grandfather():
#     def job(self):
#         print("farmer")
# class father():
#     pass
# class son(grandfather,father):
#     pass
# result = son()
# result.job()


                    # hierarchical inheritance.....................................



# class Animal:
#     def eat(self):
#         print("Animal eats food")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")

# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()
    
    
    
    
                      #hybrid inheritance...............................
                      
                      
# class Grandparent:
#     def house(self):
#         print("Grandparent has a house")

# class Father(Grandparent):
#     def bike(self):
#         print("Father has a bike")

# class Mother:
#     def cooking(self):
#         print("Mother cooks well")

# class Son(Father, Mother):
#     def laptop(self):
#         print("Son has a laptop")

# s = Son()

# s.house()
# s.bike()
# s.cooking()
# s.laptop()


                         # super()    calls the parent method..........................
# class Father:
#     def __init__(self):
#         print("Father constructor")

# class Son(Father):
#     def __init__(self):
#         super().__init__()
#         print("Son constructor")

# s = Son()