#Entrada: valorReal, cotacaoDolar
#Saída: valorDolar

cotacao = 4.81

valorDolar = float(input("Insira o valor em dólares que tem guardado no cofre: "))

valorReal = valorDolar * cotacao

print("O valor da cotação está em ", cotacao, " e o valor em dólares no cofre é de $", valorReal)