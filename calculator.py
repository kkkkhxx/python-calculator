class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b<0 and a<0:
            b *= (-1)
            a *= (-1)
            for i in range(b):
                result = self.add(result, a)
            return result
        elif b<a:
            for i in range(a):
                result = self.add(result, b)
            return result
        else:
            for i in range(b):
                result = self.add(result, a)
            return result

    def divide(self, a, b):
        result = 1
        if a==0:
            return 0
        else:
            while a > b:
                a = self.subtract(a, b)
                result += 1
            return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))