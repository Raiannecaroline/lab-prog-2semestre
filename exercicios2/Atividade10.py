sucoLaranja = str(input("Laranja"))
sucoAcerola = str(input("Acerola"))

print("Antes da troca")
print("Copo com o suco de Acerola", sucoAcerola)
print("Copo com o suco de Laranja: ", sucoLaranja)

copoVazio = sucoLaranja
sucoLaranja = sucoAcerola
sucoAcerola = copoVazio

print("Depois da Troca")
print("Copo com o suco de Acerola: ", sucoLaranja)
print("Copo com o suco de Laranja: ", sucoAcerola)