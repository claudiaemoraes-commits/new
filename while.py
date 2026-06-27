from random import randint

# Senha

print("Digite até acertar!")

senha = ''
while senha != 1234:
    senha = int(input("Digite uma senha numérica: "))
    print(senha)
    if senha != 1234:
        print("Senha incorreta, tente novamente!")
    elif senha == 1234:
        print("Acesso permitido!")
    else:
        ("Erro...")
    break


# Notas de alunos

print("Cálculo de notas de alunos:")

media1 = ''
media2 = ''
soma = 0
while media1 != -1 and media2 != -1:
    media1 = float(input("Digite a nota de aluno: "))
    media2 = float(input("Digite a nota de aluno: "))
    soma = (media1 + media2)/2
    print(f"A média do aluno é {soma}")
    if media1 or media2 == -1:
        break


# Caixa eletrônico simples

print("Simulador de ciaxa eletrônico")

valor_disponivel = 1000
saque = float(input("Digite um valor para saque: "))
sub = (valor_disponivel - saque)

if saque < 1000:
    print("Seu saque foi aceito... Aguarde!")
    print(f"Saldo restante: {sub}")
else:
    while saque > 1000:
        print("Não temos saque maior que R$1000, tente novamente!")
        break

# Acúmulo de compras

total = 0
sair = -1

while sair != 0:
    valor = float(input("Digite o valor da sua compra: "))
    total = valor + total
    sair = int(input("Digite 0 para sair: "))

print(f"O valor final de sua compra é: {total}")

# Adivinhação de número:

import random

print("Adivinhação de números:")

i = (random.randint(1, 20))

usuario = int((input("Adivinhe o número ao qual gerei: ")))

while usuario != i:
    print("Tente novamente!")
    break
    
if usuario == i:
    print("Parabéns, você acertou!")

#Contador regressivo

num = int(input("Digite um número inteiro: "))

while num >= 0:
    print(num)
    num -= 1

print("fim da contagem")




# Conversor de temperatura
print("Conversor de Celsius para Fahrenheit")

F = 0
sair = -1

while sair != 0:
    
    C = int(input("Digite o grau Celsius: "))
    
    F = (C * 1.8)+ 32
    print(F)
    
    resp = int(input("Digite 0 para sair:"))
    if resp == 0:
        print ("Programa encerrado!")
        break









