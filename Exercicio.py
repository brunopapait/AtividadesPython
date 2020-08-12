# Bruno Henrique Papait - Análise e desenvolvimento de sistemas - 6º Período
import math

# def exercicio1():
#   main()

# def main():
#   valorRaio = float(input("Informe o valor do raio da esfera ? \n").lower())
#   print(valorRaio)
#   print("Para calcular a área da esfera digite a letra 'a'")
#   print("Para calcular o volume da esfera digite a letra 'b'")
#   print("Para voltar ao menu principal digite a letra 'c'")

#   letraOpcao = str(input("Por favor informe a opção desejada ! \n"))

#   if letraOpcao == "a":
#     calculaAreaEsfera(valorRaio)
#   elif letraOpcao == "b":
#     calculaVolumeEsfera(valorRaio)
#   elif letraOpcao == "c":
#     main()

# def calculaAreaEsfera(valorRaio):
#   areaEsfera = 4 * math.pi * math.pow(valorRaio, 2)
#   print("O valor da Area é de %.2f" %areaEsfera)

# def calculaVolumeEsfera(valorRaio):
#   volumeEsfera = 4 * math.pi * math.pow(valorRaio, 3) / 3
#   print("O valor do Volume é de %.2f" %volumeEsfera)

# exercicio1()


# def exercicio2():
#   salarioGoku = float(input("Informe o salário de Goku ? \n"))
#   primeiraConta = float(input("Informe o valor da primeira conta ? \n"))
#   segundaConta = float(input("Informe o valor da segunda conta ? \n"))
#   quantidadeDias = int(input("Informe a quantidade de dias em atraso \n"))

#   def calculaValoresDasMultas():
#     valorPorcentagem = (quantidadeDias * 2) / 100

#     valorMultaPrimeiraConta = primeiraConta + (primeiraConta * valorPorcentagem)

#     valorMultaSegundaConta = segundaConta + (segundaConta * valorPorcentagem)

#     calculaValorSalario(valorMultaPrimeiraConta, valorMultaSegundaConta)


#   def calculaValorSalario(valorMultaPrimeiraConta, valorMultaSegundaConta):
#     valorTotalContas = valorMultaPrimeiraConta + valorMultaSegundaConta
#     salario = salarioGoku - valorTotalContas

#     if (salario < 0):
#       return print("Goku ficará devendo %.2f" %salario)
#     else:
#       print("O restante do salário de Goku é de %.2f" %salario)

#   calculaValoresDasMultas()

# exercicio2()

# def exercicio3():
#   altura = float(input("Informe a altura ? \n"))
#   sexo = str(input("Informe o sexo da pessoa ? \n M -> Masculino, F -> Feminino \n").upper());

#   if (sexo == "M" or sexo == "F"):
#     if sexo == "M":
#       pesoIdeal = (72.2 * altura) - 58;
#     else:
#       pesoIdeal = (62.1 * altura) - 44.7;
#   else:
#     print("Por favor informe os caracteres corretamente.")
#     return

#   print("O peso ideal é de %.2f" %pesoIdeal)

# exercicio3()

# def exercicio4():
#   salario = float(input("Informe o salário do funcionário ? \n"))

#   if salario <= 300.00:
#    porcentagem = 15
#   elif salario <= 600.00:
#    porcentagem = 10
#   elif salario <= 900.00:
#    porcentagem = 5
#   else:
#    porcentagem = 2

#   percentual = porcentagem / 100
#   valorAumento = percentual * salario
#   novoSalario = salario + valorAumento


#   print("O novo salário é de R$%.2f" %novoSalario)

# exercicio4()


# def exercicio5():
#     contador = 0
#     nomeMasculino = []
#     nomeFeminino = []
#     salarioMasculino = []
#     salarioFeminino = []
#     mediaSalarioMasculino = 0
#     mediaSalarioFeminino = 0
#     contadorMasculino = 0
#     contadorFeminino = 0
#     quantidadeFuncionarios = int(
#         input("Informe a quantidade de funcionários ? \n"))

#     while(contador < quantidadeFuncionarios):
#         nome = str(input("Informe o nome do funcionário ? \n"))
#         sexo = str(input(
#             "Informe o sexo do funcionário ? \n M -> Masculino, F -> Feminino \n").upper())
#         salario = float(input("Informe o salário do funcionário ? \n"))

#         if sexo == "M":
#             contadorMasculino = contadorMasculino + 1
#             nomeMasculino.append(nome)
#             salarioMasculino.append(salario)
#             mediaSalarioMasculino = (
#             mediaSalarioMasculino + salario) / contadorMasculino
#         else:
#             contadorFeminino = contadorFeminino + 1
#             nomeFeminino.append(nome)
#             salarioFeminino.append(salario)
#             mediaSalarioFeminino = (
#             mediaSalarioFeminino + salario) / contadorFeminino

#         contador = contador + 1
#         print(contador)
    
#     if len(salarioMasculino) > 0:
#         print("O maior salário dos funcionários masculinos é de R$ %.2f", max(salarioMasculino))
#         print("O média dos salários dos funcionários masculinos é de R$ %.2f \n\n\n", mediaSalarioMasculino)
#     else:
#         print("Não existe nenhum funcionário do sexo masculino \n\n\n!")

#     if len(salarioFeminino) > 0:
#         print("O maior salário das funcionárias femininas é de R$ %.2f", max(salarioFeminino))
#         print("O média dos salários das funcionárias femininas é de R$ %.2f", mediaSalarioFeminino)
#     else:
#         print("Não existe nenhuma funcionária do sexo feminino !")
    
# exercicio5()


# def exercicio6():
#     found = False
#     numeros = []
#     contador = 0
#     oldValue = 0
#     pos = 0

#     while (found == False):
#         numero = int(input("Informe um valor do tipo inteiro ? \n"))
#         numeros.append(numero)
#         if contador > 0:
#             pos = len(numeros) - 2
#             oldValue = numeros[pos]
#             if (numero > (oldValue ** 2)):
#                 found = True

#         contador = contador + 1
    
#     print("Valor maior que o dobro do valor anterior encontrado ..")
    

# exercicio6()

def exercicio7():
    found = False
    numeros = []
    contador = 0
    oldValue = 0
    pos = 0

    while (found == False):
        numero = int(input("Informe um valor do tipo inteiro ? \n"))
        numeros.append(numero)
        if contador > 0:
            pos = len(numeros) - 2
            oldValue = numeros[pos]
            if (numero == oldValue):
                numeros.pop();
                numeros.pop();
                print(numeros)
                found = True
        contador = contador + 1

    print("A soma dos valores é de", sum(numeros))

exercicio7()

