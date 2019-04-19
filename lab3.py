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
        return Fraction(((self.num * other.den) + (self.den * other.num)), (self.den * other.den))
    def __sub__(self, other):
        return Fraction(self.num, self.den) + Fraction(-1*other.num, other.den)
    def __mul__(self, other):
        return Fraction((self.num * other.num), (self.den * other.den))
    def __truediv__(self, other):
        return Fraction((self.num * other.den), (self.den * other.num))
    def __pow__(self, exp):
        if exp == 0:
            return Fraction(1,1)
        elif exp < 0:   
            temp = self.num
            self.num = self.den
            self.den = temp
            return self*(self.__pow__(-1*exp))
        elif exp > 0:
            return self*(self.__pow__(exp-1))
if __name__ == "__main__":
    #debugging
    frac1 = Fraction(2,3)
    frac2 = Fraction(3,4)
    print(frac1 + frac2)
    print(frac1 - frac2)
    print(frac1 * frac2)
    print(frac1 / frac2)
    print(frac1 ** 2)

    def H(n):
        total = Fraction(0,1)
        for i in range(1, n+1):
            total += Fraction(1, i)
        return total
    def T(n):
        total = Fraction(0,1)
        half = Fraction(1,2)
        for i in range(n+1):
            total += half ** i
        return total
    def Z(n):
        return (Fraction(2,1)-T(n))
    def R(n, b):
        total = Fraction(0,1)
        
        for ii in range(1, n+1):
            total += (Fraction(1, ii) ** b)
        return total
    riemannNums = [2,3,4,5,6,7,8]
    while True:
        try:
            userIn = int(input('Enter number of iterations (integer > 0):\n'))
        except TypeError:
            print('Bad Input')
            continue
        print('H({})={}'.format(userIn, H(userIn)))
        print('H({})~={:0.8f}'.format(userIn, H(userIn).approximate()))

        print('T({})={}'.format(userIn, T(userIn)))
        print('T({})~={:0.8f}'.format(userIn, T(userIn).approximate()))

        print('Z({})={}'.format(userIn, Z(userIn)))
        print('Z({})~={:0.8f}'.format(userIn, Z(userIn).approximate()))
        for i in riemannNums:
            print('R({},{})={}'.format(userIn, i, R(userIn, i)))
            print('R({},{})~={:0.8f}'.format(userIn, i, R(userIn, i).approximate()))
        break
        

