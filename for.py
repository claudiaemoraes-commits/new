with open ('teste.txt', encoding='utf-8') as files:
    for file in files:
        print(file)


# Números
par = list(range (1, 21))
for numero in par:
    print(numero)

# Tabuada
num = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Listas ZIP

a = [1,2,3]
b = [4,5,6]
for a, b in zip (a, b):
    print(a + b)

# Nomes e idades ZIP
nomes = ['Ana', 'Pedro', 'João']
idades = [20, 25, 30]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")

#Frutas
frutas = ['maçã', 'banana', 'uva']
for i, fruta in enumerate(frutas):
    print(f"A fruta de índice {i} é {fruta}")

#Manipulação de tuplas
pessoas = [('Ana', 20), ('Pedro', 25), ('João', 30)]

for i, pessoa in enumerate(pessoas):
    nome, idade = pessoa
    print(f"A pessoa de índice {i} é {nome} e tem {idade} anos.")
    if idade >= 18:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} é menor de idade.")

# Contador de palavras e linhas em um arquivo de texto
with open('teste.txt', encoding='utf-8') as files:
    for file in files:
        palavras = file.split()
        print(f"O arquivo tem {len(palavras)} palavras.")
        print(f"O arquivo tem {len(file.splitlines())} linhas.")

# Dicionário de notas:

notas = {'Ana': 8, 'Pedro': 7, 'João': 9}

for nome, nota in notas.items():
    if nota >= 8:
        print(f"{nome} tem nota {nota} e está aprovado.")
    else:
        print(f"{nome} aluno reprovado!")


