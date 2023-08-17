nomeCorretor = str(input("Insira o nome do corretor: "))
quantidadeCasasVendidas = int(input("Insira a quantidade de casas vendidas: "))
valorTotalvendas = float(input("Insira o valor total de suas vendas: "))

salarioBase = 1500
comissao = 200

salarioFinal = salarioBase + comissao * quantidadeCasasVendidas + valorTotalvendas * 0.05

print("O corretor ", nomeCorretor, " vendeu ", quantidadeCasasVendidas, " casa(s) e conseguiu ao final um salário de R$:", salarioFinal, " reais")

