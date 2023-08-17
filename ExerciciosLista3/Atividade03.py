valor = float(input("Insira o valor que quer sacar: "))

valor100 = valor / 100
valor = valor - (valor100 * 100)

valor50 = valor / 50
valor = valor - (valor50 * 50)

valor20 = valor / 20
valor = valor - (valor20 * 20)

valor10 = valor / 10
valor = valor - (valor10 * 10)

valor5 = valor / 5
valor = valor - (valor5 * 5)

valor1 = valor

print(f"O número de notas de 100 é de {valor100:.0f}")
print(f"O número de notas de 50 é de {valor50:.0f}")
print(f"O número de notas de 20 é de {valor20:.0f}")
print(f"O número de notas de 10 é de {valor10:.0f}")
print(f"O número de notas de 5 é de {valor5:.0f}")
print(f"O número de notas de 1 é de {valor1:.0f}")