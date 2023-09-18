segundos = 0
minutos = 0
horas = 0

gramas = int(input("Insira o tamanho da massa em gramas: "))
massaFinal = gramas

while massaFinal > 0.50:
  if segundos > 60:
    minutos += minutos
    segundos = 50 - segundos
    segundos = segundos + 50
  if minutos > 59:
    horas: 1

  massaFinal = massaFinal /2

print("Massa Inicial: ", gramas, "\n Massa Final: ", massaFinal)
print(f"{horas}: {minutos}: {segundos}")

