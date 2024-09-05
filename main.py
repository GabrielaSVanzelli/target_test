
# Verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


numero = int(input("Digite um número: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


# Contar a ocorrência da letra 'a' em uma string
def contar_a(s):
    return s.lower().count('a')

string = input("Digite uma string: ")
quantidade = contar_a(string)
print(f"A letra 'a' aparece {quantidade} vezes na string.")



# Valor da variável SOMA após o processamento do código
indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)
