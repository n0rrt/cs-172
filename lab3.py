class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    def approximate(self):
        return self.num/self.den
    def simplify(self):
        x = self.gcd(self.num, self.den)
        self.num = self.num//x
        self.den = self.den//x
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    def __add__(self, other):
        return ((self.num * other.den) + (self.den * other.num)), (self.den * other.num)
    def __sub__(self, other):
        return (self.num, self.den) + (-1*other.num, other.den)
    def __mul__(self, other):
        return (self.num * other.num), (self.den * other.den)
    def __truediv__(self, other):
        return (self.num * other.den), (self.den * other.num)
    def __pow__(self, exp):
        if exp == 0:
            return 1
        elif exp < 0:   
            temp = self.num
            self.num = self.den
            self.den = temp
            return (self.__pow__( -1*exp))
        elif exp > 0:
            return (self.__pow__(exp-1))
if __name__ == "__main__":
    
    def H(n):
        
        total = Fraction(0,1)
        for i in range(1, n+1):
            total += Fraction(1, i)
    print(H(3))
