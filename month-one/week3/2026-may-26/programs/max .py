def max_num(*numbers):
    if len(numbers)==0:
        return None
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number
print(max_num(10,20,4,5,3,8,9,2,3))