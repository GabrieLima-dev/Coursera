entrada_segundos = int(
    input("Por favor, entre com o número de segundos que deseja converter: "))

n_minutos = int(entrada_segundos/60)
n_segundos = int(n_minutos % 60)
n_horas = int(n_minutos/60)
n_dias = int(n_horas/24)
minutos = str(n_minutos)
segundos = str(n_segundos)
horas = str(n_horas)
dias = str(n_dias)

print(dias + " dias " + horas + " horas, " + minutos +
      " minutos e " + segundos + " segundos. ")
