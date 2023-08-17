identificacaoVendedor = int(input("Insira o código do vendedor: "))
codigoPeca = int(input("Insira o código do peça: "))
precoUnitarioPeca = float(input("Insira o preço unitário da peça: "))
quantidadePecasVendidas = int(input("Insira a quantidade de peças vendidas: "))


if (identificacaoVendedor == 1):
    print("Cláudio")
elif (identificacaoVendedor == 2):
    print("Carlos")
elif (identificacaoVendedor == 3):
    print("Marcio")
elif (identificacaoVendedor == 4):
    print("Paulo")
else:
    print("Escola um vendedor")



if (codigoPeca == 1):
    print("Porca")
elif (codigoPeca == 2):
    print("Parafuso")
elif (codigoPeca == 3):
    print("Chave")
elif (codigoPeca == 4):
    print("Broca")
else:
    print("Escola um código de peça")
    

totalVendaPecas = quantidadePecasVendidas * precoUnitarioPeca

comissao = totalVendaPecas * 0.05

print("O código vendedor selecionado foi o ", identificacaoVendedor, "\n A peça escolhida foi a ", codigoPeca, "\n A quantidade de peças foi de ", quantidadePecasVendidas, "\n O Preço Unitário das peças eram de R$", precoUnitarioPeca, " reais")
print("As peças foram vendidas por R$", totalVendaPecas)
print("A comissão do ", identificacaoVendedor, " foi de R$", comissao, " reais")

