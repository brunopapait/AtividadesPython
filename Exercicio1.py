#Bruno Henrique Papait - Análise e desenvolvimento de sistemas - 6º Período
import math

# def exercicio1():
#   main();

# def main():
#   valorRaio = float(input("Informe o valor do raio da esfera ? \n").lower());
#   print(valorRaio);
#   print("Para calcular a área da esfera digite a letra 'a'");
#   print("Para calcular o volume da esfera digite a letra 'b'");
#   print("Para voltar ao menu principal digite a letra 'c'");

#   letraOpcao = str(input("Por favor informe a opção desejada ! \n"));

#   if letraOpcao == "a":
#     calculaAreaEsfera(valorRaio)
#   elif letraOpcao == "b":
#     calculaVolumeEsfera(valorRaio)
#   elif letraOpcao == "c":
#     main()

# def calculaAreaEsfera(valorRaio):
#   areaEsfera = 4 * math.pi * math.pow(valorRaio, 2);
#   print("O valor da Area é de %.2f" %areaEsfera)

# def calculaVolumeEsfera(valorRaio): 
#   volumeEsfera = 4 * math.pi * math.pow(valorRaio, 3) / 3
#   print("O valor do Volume é de %.2f" %volumeEsfera)

# exercicio1()


def exercicio2(): 
  salarioGoku = float(input("Informe o salário de Goku ? \n"));
  primeiraConta = float(input("Informe o valor da primeira conta ? \n"));
  segundaConta = float(input("Informe o valor da segunda conta ? \n"));
  quantidadeDias = int(input("Informe a quantidade de dias em atraso \n"));

  def calculaValoresDasMultas():
    valorPorcentagem = (quantidadeDias * 2) / 100;

    valorMultaPrimeiraConta = primeiraConta + (primeiraConta * valorPorcentagem)

    valorMultaSegundaConta = segundaConta + (segundaConta * valorPorcentagem)

    calculaValorSalario(valorMultaPrimeiraConta, valorMultaSegundaConta)


  def calculaValorSalario(valorMultaPrimeiraConta, valorMultaSegundaConta):
    valorTotalContas = valorMultaPrimeiraConta + valorMultaSegundaConta
    salario = salarioGoku - valorTotalContas;

    if (salario < 0):
      return print("Goku ficará devendo %.2f" %salario)
    else:
      print("O restante do salário de Goku é de %.2f" %salario)

  calculaValoresDasMultas()
  
exercicio2();


  



