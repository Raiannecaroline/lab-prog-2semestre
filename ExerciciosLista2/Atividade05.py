horasTrabalhadas = int(input("Insira as horas trabalhadas do dia: "))
valorHoraTrabalhada = float(input("Insira o valor da hora trabalhada: "))

salarioBruto = horasTrabalhadas * valorHoraTrabalhada

if (salarioBruto <= 800.45):
  inss = 0.0765 * salarioBruto
elif (salarioBruto > 800.46 and salarioBruto <= 900.00):
  inss = 0.0865 * salarioBruto
elif (salarioBruto > 900.01 and salarioBruto <= 1334.7):
  inss = 0.09 * salarioBruto
else:
  inss = 0.11 * salarioBruto

impostoDeRenda = 0

if (salarioBruto - inss <= 1257.12):
  impostoDeRenda = 0 * (salarioBruto - inss) - 0
elif (salarioBruto - inss > 1257.13 and salarioBruto - inss <= 2512.08):
  impostoDeRenda = 0.15 * (salarioBruto - inss) - 188.57
else:
  impostoDeRenda = 0.275 * (salarioBruto - inss) - 502.58

salarioLiquido = salarioBruto - inss - impostoDeRenda

print("O total do salário liquído é R$:", salarioLiquido)