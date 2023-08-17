taxaCarroAntes = 0.01
taxaCarroDepois = 0.015

anoCarro = int(input("Insira o ano do carro: "))
precoCarro = float(input("Insira o valor do carro: "))

if (anoCarro < 1990):
    taxaCarro = precoCarro * taxaCarroAntes
else:
    taxaCarro = precoCarro * taxaCarroDepois


print("O imposto a ser pago pelo carro é de R$", taxaCarro, "reais") 