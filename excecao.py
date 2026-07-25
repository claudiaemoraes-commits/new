
# Alfabeto
def alfabeto(insira):
    alfabeto = chr(65, 67)
    print (alfabeto)


insira = str(input("insira um caractere: "))
print(alfabeto(insira))

try:
    if insira != alfabeto:
        print("Error")

except TypeError:
    print("Valor de dado errado")
finally:
    ("Fim")
          