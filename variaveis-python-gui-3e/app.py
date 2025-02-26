#Exemplo 1: Calculando a área de um retângulo
#Declaração de variáveis
largura = 5
altura = 3

#Calculo da área usando operador de multiplicação
area = largura * altura

#Exibindo o resultado
print('A área do retângulo é:', area)
############################################
# Exemplo 2: Usando operadores matemáticos diversos
num1 = 10
num2 = 4

#Operações básicas
soma = num1 + num2 
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
modulo = num1 % num2 # Resto do divisão
potencia = num1 ** num2 #10 elevado a 4

print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}, Módulo: {modulo}, Potência: {potencia}")
########################################################################################
#Exemplo 3: Verificando se um número é positivo, negativo ou zero
numero = float(input("Digite um número"))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')

#Verificando partidade (par/impar)
if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é impar.')
############################################################################################################################################################
'''Exemplo 4: COntagem regressiva com while'''
contador = 5
while contador > 0:
    print(contador)
    contador -= 1 #Decrescente o contador
print('Fogo!')

#Loop for para somar elementos de uma lista
numeros = [1, 2, 3, 4, 5]
soma = 0
for num in numeros:
    soma += num
print("Soma da lista:", soma)

#Tabuada com for aninhado
for i in range(1, 6): #1 a 5
    for j in range(1, 11): #1 a 10
        print(f"{i} x {j} = {i*j}")
    print("------------")

