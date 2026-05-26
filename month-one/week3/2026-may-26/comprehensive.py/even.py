# nums = [1,2,3,4,5,6,7,8,9,10]
# even = []
# for i in nums:
#     if i%2 == 0:
#         even.append(i) 
# print(even)


    #    comprehensive...............
    
    
    
    
# nums = [1,2,3,4,5,6,7,8,9,10]
# even=[i for i in nums if i%2 == 0]
# print(even)


                    #   user input...............................................
nums = input("enter the nums:").split()
converted_numbers = [int(i) for i in nums]
even = [i for i in converted_numbers if i%2 == 0]
print(even)
       