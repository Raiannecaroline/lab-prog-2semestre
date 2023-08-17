i = int(input("Insira o número positivo: "))
a = float(input("Insira o número real: "))
b = float(input("Insira o número real: "))
c = float(input("Insira o número real: "))

if i == 1:
  if a < b and a < c and b < c:
    print(f"{a:.2f}, {b:.2f}, {c:.2f}")
  if a < c and a < b and c < b:
    print(f"{a:.2f}, {b:.2f}, {c:.2f}")
  if b < c and b < a and c < a:
    print(f"{b:.2f}, {a:.2f}, {c:.2f}")
  if b < a and b < c and a < c:
    print(f"{b:.2f}, {c:.2f}, {a:.2f}")
  if c < a and c < b and a < b:
    print(f"{c:.2f}, {b:.2}, {a:.2}")
  if c < b and c < a and b < a:
    print(f"{c:.2f}, {a:.2}, {b:.2}")

if i == 2:
  if a > b and a > c and b > c:
    print(f"{a:.2f}, {b:.2f}, {c:.2f}")
  if a > c and a > b and c > b:
    print(f"{a:.2f}, {b:.2f}, {c:.2f}")
  if b > c and b > a and c > a:
    print(f"{b:.2f}, {a:.2f}, {c:.2f}")
  if b > a and b > c and a > c:
    print(f"{b:.2f}, {c:.2f}, {a:.2f}")
  if c > a and c > b and a > b:
    print(f"{c:.2f}, {b:.2}, {a:.2}")
  if c > b and c > a and b > a:
    print(f"{c:.2f}, {a:.2}, {b:.2}")   

if i == 3:
  if a > b and a > c:
    print(f"{b}, {a}, {c}")
  if b > a and b > c:
    print(f"{a}, {b}, {c}")
  if c > a and c > b:
    print(f"{a}, {c}, {b}") 


