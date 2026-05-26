# def count(n):
#     count =1
#     count_numbers = []
#     while count<=n:
#         count_numbers.append(count)
#         count+=1
#     return count_numbers
        
# numbers = int(input("enter the numbers:"))
# for n in count(numbers):
#      print(n) 

                      #by generator................................................

def count_value(n):
    count = 1
    while count<=n:
        yield count
        count +=1
numbers = int(input("enter the numbers:"))
for i in count_value(numbers):
    print(i)
