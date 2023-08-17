pagamento = 4.00
minutos = 60

horaEntrada = float(input("Insira a hora da entrada do veículo: "))
minutoEntrada = float(input("Insira o minuto da entrada do veículo: "))
horaSaida = float(input("Insira a hora da saída do veículo: "))
minutoSaida = float(input("Insira o minuto da saída do veículo: "))

precoEstacionamento = (horaSaida - horaEntrada) * minutos + minutoSaida - minutoEntrada

if (precoEstacionamento > minutos):
    pagamento += (precoEstacionamento - minutos) / 10

print("O valor do pagamento pelo estacionamento será ", pagamento, " reais")
print("O veículo ficou ", precoEstacionamento, " minutos no estacionamento")