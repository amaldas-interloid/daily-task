#print("hello world")



                       #create a global variable................................................................

# x = "das"
# def myname():
#     print("amal" + x)
# myname()


                       #create a variable inside a function ,same name as the outside the function...............................

# x = "amaldas"
# def myname():
#     x="suriya"
#     print("this is "+x)
# myname()
# myname()
# print("this is " + x )

                  # global variable can be acess inside by global keyword............................................

# x="amaldas"
# def myname():
#     global x
#     print("my name is "+ x)
# myname()

                     #functions
# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit-32) * 5 / 9
# print(fahrenheit_to_celsius(77))   
# print(fahrenheit_to_celsius(60))   
# print(fahrenheit_to_celsius(24))    
    
    
    
                #arguements and parameters..............................................................
# def myname(name1,name2):
#     return name1 + " " + name2
# print(myname("amal","das"))


                        #find the maximun number  using *args
def max_num(*numbers):
    if len(numbers)==0:
        return None
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number
print(max_num(10,20,4,5,3,8,9,2,3))