import math
x_ponto1 = float(input("Digite o valor do x do primeiro ponto: "))
y_ponto1 = float(input("Digite o valor do y do primeiro ponto: "))
x_ponto2 = float(input("Digite o valor do x do segundo ponto: "))
y_ponto2 = float(input("Digite o valor do y do segundo ponto: "))
distancia = math.sqrt(((x_ponto1-x_ponto2)**2) + ((y_ponto1-y_ponto2)**2))

if distancia >= 10:
    print("longe")
else:
    print("perto")
