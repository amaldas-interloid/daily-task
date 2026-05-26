# def name(n):
# 	count = 1
# 	while count <= n:
# 		yield count
# 		count += 1
# for i in name(5):
# 	print(i)

         # second .........................
def large_numbers(n):
	for i in range(n):
		yield i
gen = large_numbers(1000)
print(next(gen))
print(next(gen))
print(next(gen))




