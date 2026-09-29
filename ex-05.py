#5. Soma dos dígitos de um número inteiro positivo

def soma_digitos(n):
    
    if n < 10:
        return n

    else:
        return (n % 10) + soma_digitos(n // 10)

numero = 12345
print(f"A soma dos dígitos de {numero} é {soma_digitos(numero)}") # Saída: 15