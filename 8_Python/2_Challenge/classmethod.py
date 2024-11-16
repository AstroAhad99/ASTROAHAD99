from classmethod_meth import Addition

class calculator:

    @classmethod
    def addition(cls, num1, num2):
        return Addition.add(num1, num2)
    

    @classmethod
    def subtraction(cls, num1, num2):
        return cls.addition(num1, -num2)
    

    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for num in range(0, num2):
            res = cls.addition(res, num1) # adding num1 to res num2 times
        return res
    

    @classmethod
    def divide(cls, num1, num2):
        res = num1
        cnt = 0
        while res>=num2:
            res = cls.addition(res, -num2)
            cnt = cls.addition(cnt, 1)
        return cnt
    
#mycal = calculator.addition(10, 5)
#mycal = calculator.subtraction(10, 5)
#mycal = calculator.multiply(10, 5)
mycal = calculator.divide(15, 5)

print(mycal)