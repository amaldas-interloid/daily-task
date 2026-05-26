    #square root of the number....................................................
    
    
def square(n):
    square_root = 1
    while square_root<=n:
        SQ =square_root*square_root
        yield SQ
        square_root+=1
        
value = square(10)
print(next(value))
for i in value:
    print(i)