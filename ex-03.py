#3. Inverter uma string

def inverter_string(s):
    
    if len(s) <= 1:
        return s
    
    return s[-1] + inverter_string(s[:-1])


print(inverter_string("python"))  
print(inverter_string("a"))       
print(inverter_string(""))        