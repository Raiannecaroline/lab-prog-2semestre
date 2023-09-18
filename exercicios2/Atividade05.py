from math import sqrt


x1 = float(input("Entre com a posição x do ponto P1..."))
y1 = float(input("Entre com a posição y do ponto P1..."))

x2 = float(input("Entre com a posição x do ponto P2..."))
y2 = float(input("Entre com a posição y do ponto P2..."))


print(F"A distancia entre os pontos é {sqrt(((x2-x1)**2)+((y2-y1)**2))}")