#4. Verificar palíndromo

def eh_palindromo(s):
    
    def verificar(texto):
    
        if len(texto) <= 1:
            return True
      
        if texto[0] != texto[-1]:
            return False
        
        return verificar(texto[1:-1])

    texto_limpo = "".join(c.lower() for c in s if c.isalnum())
    
    return verificar(texto_limpo)

print(eh_palindromo("arara"))                       
print(eh_palindromo("Aara"))                        
print(eh_palindromo("A man, a plan, a canal: Panama")) 
print(eh_palindromo("python"))                       