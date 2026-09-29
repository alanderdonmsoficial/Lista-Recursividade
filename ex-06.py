
#6. Encontrar todos os anagramas de uma string

def gerar_anagramas(s):
  
    if len(s) <= 1:
        return [s]

    anagramas = []

    for i in range(len(s)):
       
        caractere_atual = s[i]
        
       
        restante = s[:i] + s[i+1:]
        
      
        for sub_anagrama in gerar_anagramas(restante):
            anagramas.append(caractere_atual + sub_anagrama)

  
    return list(dict.fromkeys(anagramas))


resultado = gerar_anagramas("abc")
print(f"Total de anagramas: {len(resultado)}")
print(resultado)