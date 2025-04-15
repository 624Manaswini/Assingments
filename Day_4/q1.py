class Poly:

    def __init__(self, *coeffs):
        self.coeffs = list(reversed(coeffs))
    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        result = [0] * max_len
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result[i] = a + b
        return Poly(*reversed(result))

    def __repr__(self):
        return f"({', '.join(map(str, reversed(self.coeffs)))})"

a = Poly(1,2,3)  
b = Poly(1,0,1,1,2,3)
c = a+b 
print(c)
