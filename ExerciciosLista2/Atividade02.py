idade = int(input("Insira a idade do paciente: "))
peso = int(input("Insira o peso do paciente: "))

dosagem = 0

if (idade >= 12 and peso > 60):
    dosagem = 1000 / 25
    print("Idade: ", idade, "\nPeso: ", peso, "\nO paciente deve tomar 1000mg = ", dosagem, " gotas")

elif (idade >= 12 and peso < 60):
    dosagem = 875 / 25
    print("Idade: ", idade, "\nPeso: ", peso, "\nO paciente deve tomar 1000mg = ", dosagem, " gotas")
        
elif (peso > 5 and peso <= 9 ):
    dosagem = 125 / 25
    print("Idade: ", idade, "\nPeso: ", peso, "\nO paciente deve tomar 1000mg = ", dosagem, " gotas")

elif (peso > 9.1 and peso <= 16):
    dosagem = 250 / 25
    print("Idade: ", idade, "\nPeso: ", peso, "\nO paciente deve tomar 1000mg = ", dosagem, " gotas")

elif (peso > 16.1 and peso <= 24):
    dosagem = 375 / 25
    print("Idade: ", idade, "\nPeso: ", peso, "\nO paciente deve tomar 1000mg = ", dosagem, " gotas")

elif (peso > 24.1 and peso <= 30):
    dosagem = 500 / 25
    print("Idade: ", idade, "\nPeso: ", peso, "\nO paciente deve tomar 1000mg = ", dosagem, " gotas")

elif (peso > 30):
    dosagem = 750 / 25   
    print("Idade: ", idade, "\nPeso: ", peso, "\nO paciente deve tomar 1000mg = ", dosagem, " gotas")                    
