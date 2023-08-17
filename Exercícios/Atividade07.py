#Entrada: comprimentoTijolo, larguraTijolo, comprimentoParede, larguraParede
#Saída: quantidadeTijolo

comprimentoTijolo = float(input("Insira o comprimento do Tijolo em centimetros: "))
larguraTijolo = float(input("Insira a largura do Tijolo em centimetros: "))
comprimentoParede = float(input("Insira o comprimento da Parede em metros: "))
larguraParede = float(input("Insira a largura da Parede em metros: "))

areaTijolo = comprimentoTijolo * larguraTijolo
areaParede = comprimentoParede * larguraParede

quantidadeTijolo = (1 / areaTijolo) * areaParede

print("O número de tijolos para a parede é de ", quantidadeTijolo, " tijolos") 