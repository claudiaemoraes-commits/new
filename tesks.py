
# # Programa de verficação de empréstimos

idade = int(input("Digite a sua idade: "))
aposentado = str(input("Você é aposentado? (sim/não): "))

if idade >= 60:
    print("Você já é idoso.")
    if aposentado == "sim":
        print("Você é aposentado e pode conseguir empréstimos especiais.")
    else:
        print("Você não é aposentado, mas ainda pode conseguir empréstimos.")

elif idade >= 18 and idade < 60:
    print("Você já pode conseguir empréstimos!")

else:
    print("Você ainda é menor de idade e não pode conseguir empréstimos.")

valor_emprestimo = float(input("Digite o valor do empréstimo que deseja solicitar: "))
renda_declarada = float(input("Digite a sua renda declarada: "))


if renda_declarada >= ( 0.2 * valor_emprestimo):
    print("Sua renda declarada é maior que 20% do valor do empréstimo.")
elif renda_declarada < ( 0.2 * valor_emprestimo):
    print("Sua renda declarada é menor que 20% do valor do empréstimo, e não pode ser aprovado.")
else:
    print("Tente novamente!...")




#Política de descontos comerciais

print(" \nLimites de desconto por perfil:")

bronze = 0.5
prata = 0.10
ouro = 0.15
gerente = 0.25

perfil = str(input("Você é vendedor ou gerente? "))

if perfil == "vendedor":
    print(f" Você tem limites de desconto. São eles: \n bronze - {bronze} \n prata - {prata} \n ouro - {ouro}")

elif perfil == "gerente":
    print("Você pode utilizar 25% de desconto para qualquer categoria.")

else: 
    print("Você não pode utilizar descontos comerciais.")


print(" \nCompra do cliente: ")
valor_compra = float(input("Digite o valor da compra: "))
desconto_solicitado = float(input("Digite o valor do desconto solicitado: "))

if desconto_solicitado == bronze:
    print("Desconto aprovado para categoria bronze.")
    desconto_solicitado = valor_compra * bronze
elif desconto_solicitado == prata:
    print("Desconto aprovado para categoria prata.")
    desconto_solicitado = valor_compra * prata
elif desconto_solicitado == ouro:
    print("Desconto aprovado para categoria ouro.")
    desconto_solicitado = valor_compra * ouro
elif desconto_solicitado == gerente:
    print("Desconto aprovado para gerente.")
    desconto_solicitado = valor_compra * gerente
else:
    print("Desconto solicitado não aprovado.")

print("Valor final da compra: {}".format(valor_compra - desconto_solicitado))







    











