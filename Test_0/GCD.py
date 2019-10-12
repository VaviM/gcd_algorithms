
from timeit import default_timer as timer

class GCD_alg(object):
    start = 0
    def __init__(self, a, b):
        self.op1 = a
        self.op2 = b
        self.B = self.B_x(a, b)
        self.times = list()     
        self.gcd = 1
        self.ratio = 0.0
        self.Calculate(a, b)
        

    def Euclid_0(self, a, b):
        #start = timer()
        if a == b:
            end = timer()
            self.__time1 = end - start
            return a
        if a > b:
            a, b = b, a 
        return self.Euclid_0(a, b-a)

    def B_x(self, a, b):
        if a > b:
            self.ratio = b/a
            return len(str(a))#len(str(bin(a))[2:])
        else:
            self.ratio = a/b
            return len(str(b))#len(str(bin(b))[2:])

    def Calculate(self, a, b):
        global start 
        start = timer()
        self.gcd = self.Euclid_0(a, b)
        self.times.append(self.__time1)
        #self.Euclid_1(a, b)
        #self.times.append(self.__time2)
        #self.Binary_0(a, b)
        #self.times.append(self.__time3)
        #self.Binary_1(a, b)
        #self.times.append(self.__time4)
        #self.Binary_2(a, b)
        #self.times.append(self.__time5)

    def Euclid_1(self, a, b):
        start = timer()
        while a != b:
            if a > b:
                a,b = b,a
            b-=a
        end = timer()
        self.__time2 = end - start
        return a

    def Binary_0(self,a,b):
        start = timer()
        if a == 0:
            end = timer()
            self.__time3 = end - start
            return b
        elif b == 0:
            end = timer()
            self.__time3 = end - start
            return a
        elif a == b:
            end = timer()
            self.__time3 = end - start
            return a
        elif a == 1 and b == 1:
            end = timer()
            self.__time3 = end - start
            return 1
        elif a % 2 == 0 and b % 2 == 0:
            return 2 * self.Binary_0(a/2, b/2)
        elif a % 2 == 0 and b % 2 != 0:
            return self.Binary_0(a/2, b)
        elif a % 2 != 0 and b % 2 == 0:
            return self.Binary_0(a, b/2)
        elif a < b:
            return self.Binary_0((b - a)/2, a)
        else:
            return self.Binary_0((a - b)/2, b)


    def Binary_1(self,a,b):
        start = timer()
        nod = 1
        if a == 0:
            end = timer()
            self.__time4 = end - start
            return b
        elif b == 0:
            end = timer()
            self.__time4 = end - start
            return a
        elif a == b:
            end = timer()
            self.__time4 = end - start
            return a
        elif a == 1 or b == 1:
            end = timer()
            self.__time4 = end - start
            return 1
        while a != 0 and b != 0:
            if a % 2 == 0 and b % 2 == 0:
                nod *= 2
                a /= 2
                b /= 2
                continue
            if a % 2 == 0 and b % 2 != 0:
                a /= 2
                continue
            if a % 2 != 0 and b % 2 == 0:
                b /= 2
                continue
            if a > b:
                a, b = b, a
            a, b = (b - a)/2, a
        if a == 0:
            end = timer()
            self.__time4 = end - start
            return nod * b
        else:
            end = timer()
            self.__time4 = end - start
            return nod * a


    def Binary_2(self,a, b):
        start = timer()
        if a == 0:
            end = timer()
            self.__time5 = end - start
            return b
        elif b == 0:
            end = timer()
            self.__time5 = end - start
            return a
        shift = 0
        while ((a | b) & 1) == 0:
            a = a >> 1
            b = b >> 1
            shift+=1
        while (a & 1) == 0:
            a >>= 1
            while True:
                while (b & 1) == 0:
                    b = b >> 1
                if a > b:
                    a, b = b, a
                b -= a
                if b == 0:
                    break
        end = timer()
        self.__time5 = end - start
        return a << shift


