class Calculator:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        total  = self.a + other.a
        return (f"Result of addition is {total}")
a = Calculator(2)
b = Calculator(2)
result  = a+b
print(result)
print("hello")