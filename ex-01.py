#1. Máximo Divisor Comum (MDC)

def mdc(a, b):
    
    if b == 0:
        return abs(a)
    
    return mdc(b, a % b)

print(mdc(48, 18))  
print(mdc(7, 3))    
print(mdc(-10, 5)) 