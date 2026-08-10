with open ('teste.txt', encoding='utf-8') as files:
    for file in files:
        print(file)

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

# Contador de palavras e linhas em um arquivo de texto
with open('teste.txt', encoding='utf-8') as files:
    for file in files:
        palavras = file.split()
        print(f"O arquivo tem {len(palavras)} palavras.")
        print(f"O arquivo tem {len(file.splitlines())} linhas.")

