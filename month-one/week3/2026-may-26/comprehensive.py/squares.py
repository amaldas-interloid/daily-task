        # normal method................................
        #  squares a number.........................



numbers = input("enter the numbers:").split()
numbers = [int(i) for i in numbers]
squares = []
for i in numbers:
    squares.append(i*i)
print(squares)