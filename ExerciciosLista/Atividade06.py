dolares = float(input("Insira o valor em dólares no cofre: "))
cotacao = float(input("Insira a cotação do dólar do dia: "))

valorReais = dolares * cotacao

print(f"O valor da cotação está em ", cotacao, " e o valor em reais no cofre é de R$ {valorReais:.2f}")