#Tratamento de dados

# try:
#     a = input("digite um número: ")
#     c = 1 + (a) #int foi retirado
#     print(c)

# except ValueError:
#     print("valor errado")
# except NameError:
#     print(" Nome errado ")
# except TypeError:
#     print("type errado")
# except:
#     print("Não especificado")
# finally:
#     print("Fim")


#Finally sempre vai acontecer, estando certo ou errado


#except final é como se fosse o else; usado apenas em produção

# Lógica de produção:
# 1 desenvolvimento
# janelas - criadas para que possa haver manutenção ("pode ser avisado ao cliente")
# 2 homologação -> interação para o cliente (cliente interno)
# 3 produção - cliente externo (não mexer)

#trocar o valor de erro do python por seus valores: facilita
# ex: quando tentar achar arquivos e não tiver; falhas em servidores

# estudar -> feature (início meio e fim)


# import unittest 

# # quem usa muito teste é banco
# # teste é obrigatório ter try
# # teste é separado do código

# def soma(a, b):
#     return a + b

# testcase = unittest.TestCase()

# #testcase é um nome já passado como uma variável, se colocar outro nome dará error

# try:
#     testcase.assertEqual(soma(12, 3), 5)
#     testcase.assertEqual(soma(-12, -3), -5)
#     print("todos os testes passaram")
# except AssertionError as e:
#     print("Erro de teste: ", e)



# asserEqual compara se o valor está certo ao passado 

# teste com mais de um função -> teste de integração

# pesquisar -> caixa preta, branca, cinza




        


