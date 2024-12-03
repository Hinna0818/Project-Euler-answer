class triangle_number:
    def __init__(self, min):
        self.min = min ## 最小因子数
        self.num = 1
        self.i = 1
        self.factors = set()
    
    def count_factors(self, n):
        factors = set()
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                factors.add(i)
                factors.add(n//i)
        return len(factors)
    
    def triangle(self):
        while True:
            if self.i%2 == 0:
                factors = self.count_factors(self.i // 2) * self.count_factors(self.i + 1)
            else:
                factors = self.count_factors(self.i) * self.count_factors((self.i + 1) // 2)
            
            if factors >= self.min:
                return self.num
        
            self.i += 1
            self.num += self.i

a = triangle_number(500)
print(a.triangle())