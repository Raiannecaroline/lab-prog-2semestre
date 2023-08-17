tarifaA = 0.5
tarifaB = 0.8
tarifaC = 1.0

classeConsumidora = int(input("Selecione a sua classe consumidora entre \n1 - Classe A (Residencial) \n2 - Classe B (Rural) \n3 - Classe C (Indústrial ou Comercial): "))
consumoKwh = float(input("Insira o seu consumo de KW/h: "))

if (classeConsumidora == 1):
    vf = consumoKwh * tarifaA
elif (classeConsumidora == 2):
    vf = consumoKwh * tarifaB
elif (classeConsumidora == 3):
    vf = consumoKwh * tarifaC
else:
    print("Selecione uma opção!!")

icms = 0.3 * vf
vp = vf + icms


print("Valor do fornecimento: ", vf)
print("Valor a Pagar em R$: ", vp, " reais")