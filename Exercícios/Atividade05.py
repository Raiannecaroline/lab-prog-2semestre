#Saída: PAG
#Entradas: HE, ME, HS, MS

pagamento = 4.00

horaEntrada = float(input("Insira as horas da entrada do veículo: "))
minutoEntrada = float(input("Insira os minutos da entrada do veículo: "))
horaSaida = float(input("Insira os minutos da saída do veículo: "))
minutoSaida = float(input("Insira os minutos da saída do veículo: "))

tempoPagamento = (horaSaida - horaEntrada) * 60 + minutoSaida - minutoEntrada


if (tempoPagamento > 60):
    pagamento += (tempoPagamento - 60) / 10

print("O valor do pagamento pelo estacionamento será ", pagamento, " reais")
print("O veículo ficou ", tempoPagamento, " minutos no estacionamento")