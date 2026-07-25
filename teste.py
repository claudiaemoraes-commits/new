#Função soma  
import unittest

def soma(a, b):
    return a + b


testcase = unittest.TestCase()


try:
    testcase.assertEqual(soma(2, 3), 5)
    testcase.assertEqual(soma(-2, 2), 0)
    testcase.assertNotEqual(soma(10, 5), 20)
    print("Todos os valores passaram!")
except AssertionError as e:
    print("O valor passado está errado", e)


# as e é como se você desse um apelido para ele


# ~~~~~~~~~~~~~~~~~~~~
# Função par

def funcao(a, b):

    if a % 2 == 0 and b % 2 == 0:
        print("Par")
    else:
        print("Ímpar")


a = int(input("Insira um valor: "))
b = int(input("Insira outro valor: "))
print(funcao(a, b))

try:
    if a == 5 or b == 5:
        print("ímpar")

except TypeError:
    print("Tipo de valor passado está errado!")
    
        

# ~~~~~~~~~~~~~~~~~~~~
# Inverter texto

# def inverter(texto):
    
#     invertido = texto[::-1]
#     return invertido



# texto = str(input("insira um texto: "))
# print(inverter(texto))

