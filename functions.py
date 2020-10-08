
def multiply(x,y=10):
	return x*y


def multiplyThese(*args):
	total = 1
	for item in args:
		total *= item
	return total


one = int(5)
two = int(10)
print (multiply(one,two))
print(multiply(one))
print( multiplyThese(1,2,3,4,5))
