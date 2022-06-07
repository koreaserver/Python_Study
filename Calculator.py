class Calculator:
	def __init__(self, n1=0, n2=0):
		print("\n=== 객체 초기화 시작 ===")
		self.num1 = n1
		self.num2 = n2

	def addNum(self):
		print("\n=== 더하기 시작 ===")
		print('num1 + num2 =', self.num1 + self.num2)

	def subtractNum(self):
		print("\n=== 빼기 시작 ===")
		print('num1 - num2 =', self.num1 - self.num2)

	