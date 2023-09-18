pratoPrincipal = input("Insira o prato principal: ")
sobremesa = input("Insira a sobremesa: ")
bebida = input("Insira a bebeida: ")


if pratoPrincipal == "Vegetariano":
  pratoPrincipal = 180;
elif pratoPrincipal == "Peixe":
  pratoPrincipal = 230;
elif pratoPrincipal == "Frango":
  pratoPrincipal = 250;
elif pratoPrincipal == "Carne":
  pratoPrincipal = 350;

if sobremesa == "Abacaxi":
  sobremesa = 75;
elif sobremesa == "Sorvete diet":
  sobremesa = 110;
elif sobremesa == "Mouse diet":
  sobremesa = 170;
elif sobremesa == "Mouse chocolate":
  sobremesa = 200;

if bebida == "Chá":
  bebida = 20;
if bebida == "Suco de laranja":
  bebida = 70;
if bebida == "Suco de melão":
  bebida = 100;
if bebida == "Refrigerante diet":
  bebida = 65;


calorias = pratoPrincipal + sobremesa + bebida

print("Ao todo com prato principal, sobremesa e bebida foram ingeridos um total de: ", calorias)
