alunos = int(input("Insira o número de alunos na sua turma: "))

count = 0
soma = 0

while count <= alunos:
    count += 1
    notas = float(input("Insira a nota dos aluno(a)s: "))
    soma += notas

quantidadeNotas = int(input("Insira o número de provas: "))

mediaAritmetica = soma / quantidadeNotas

print("A média aritmetica é: ", mediaAritmetica)
   