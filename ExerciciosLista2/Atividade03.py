juiz1 = float(input("Digite a nota do primeiro Juíz: "))
juiz2 = float(input("Digite a nota do segundo Juíz "))
juiz3 = float(input("Digite a nota do terceiro Juíz "))
juiz4 = float(input("Digite a nota do quarto Juíz "))
juiz5 = float(input("Digite a nota do quinto Juíz "))
juiz6 = float(input("Digite a nota do sexto Juíz "))

maiorNota = max(juiz1, juiz2, juiz3, juiz4,juiz5, juiz6)
menorNota = min(juiz1, juiz2, juiz3, juiz4,juiz5, juiz6)

mediaNotas = juiz1 + juiz2 + juiz3 + juiz4 + juiz5 + juiz6 - maiorNota - menorNota

print("Menor nota: ", menorNota, "\nMaior nota: ", maiorNota)
print("Nota final: ", mediaNotas)
