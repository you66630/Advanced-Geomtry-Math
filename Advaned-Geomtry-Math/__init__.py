import math

class Geo:

    def pa(Sides,Length):
        
        return  (1/4)*Sides*(Length**2)*(1/math.tan(math.pi/Sides))       

    def cfd(diameter):
    
        return  math.pi * diameter

    def cfr(radius):
    
        return  2 * math.pi * radius 

    def rfd(diameter):
    
        return  diameter/2

    def dfr(raduis):
    
        return   raduis*2
    
    def sr(num):
    
        return  math.sqrt(num)
    
    def cr(num):
        return math.cbrt(num)
    def pth(num1,num2):

        return math.sqrt(num1+num2)

    def pts(num1,num2):
        return math.sqrt(num1-num2)

    def sn(num):
        """Converts a given number to its scientific notation representation."""
        if num == 0:
           return "0e0"
        exponent = 0
        mantissa = num
    
            # Normalize the mantissa to the range [1, 10)
        while abs(mantissa) >= 10:
            mantissa /= 10
            exponent += 1
        while abs(mantissa) < 1:
            mantissa *= 10
            exponent -= 1
    
        return f"{mantissa}e{exponent}"

    
    def pr(part, total):
        if total == 0:
            raise ValueError("Total value cannot be zero.")
    
        percentage = part / total * 100
        return   percentage,"%"



