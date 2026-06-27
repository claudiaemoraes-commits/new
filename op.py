import random

# 1. 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = n1 + n2
print("A soma dos números é: {}".format(n3))

# 2. 
n3 = n1 - n2
print("A subtração dos números é: {}".format(n3))

# 3. 
n3 = n1 * n2
print("A multiplicação dos números é: {}".format(n3))
n3 = n1 // n2
print("A divisão inteira dos números é: {}".format(n3))
n3 = n1 % n2
print("O resto da divisão dos números é: {}".format(n3))
n3 = n1 ** n2
print("A potência dos números é: {}".format(n3))

# 4. 
if n1 > n2:
    print("O primeiro número é maior que o segundo.")
elif n1 < n2:
    print("O primeiro número é menor que o segundo.")
elif n1 >= n2:
    print("O primeiro número é maior ou igual ao segundo.")
elif n1 <= n2:
    print("O primeiro número é menor ou igual ao segundo.")
else:
    print("Tente novamente.")


# 5. 
sacola = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_sorteado = random.choice(sacola)
print("O número sorteado é: {}".format(numero_sorteado))

# 6. 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
produto = n1 * n2
subtracao = n2 - n3
resultado = produto + subtracao
print("O resultado do cálculo é: {}".format(resultado))


# 7.





