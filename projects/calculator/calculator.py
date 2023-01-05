calculate = input("Введите число, пробел, операцию, пробел, и другое число, например, 2 + 2\n").split()

check_type = calculate[0].isdigit()
if check_type == False:
	print("Input Error")
	exit()
else:
	check_type = calculate[2].isdigit()
	if check_type == False:
	    print("Input Error")
	    exit()

class Math_ops:
	a = 0
	b = 0

	def __init__(self, a, b):
	    self.a = a
	    self.b = b
	    
	def multiply(self):
		return self.a * self.b
	def divide(self):
		return self.a / self.b
	def minus(self):
		return self.a - self.b
	def plus(self):
		return self.a + self.b

nums = Math_ops(int(calculate[0]), int(calculate[2]))

print("Result:")
if calculate[1] == '+':
    print(nums.plus())
elif calculate[1] == '-':
    print(nums.minus())
elif calculate[1] == '*':
    print(nums.multiply())
elif calculate[1] == '/':
    print(nums.divide())
