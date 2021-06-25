entrada_segundos = int(
    input("Por favor, entre com o número de segundos que deseja converter: "))

dias = int(entrada_segundos / 86400)

segundos_resto = entrada_segundos % 86400
horas = segundos_resto // 3600

segundos_restantes = int(entrada_segundos % 3600)

minutos = int(segundos_restantes / 60)

segundos_restantes_final = int(segundos_restantes % 60)

horas_str = str(horas)
dias_str = str(dias)
minutos_str = str(minutos)
segundos_str = str(segundos_restantes_final)

print(dias_str + " dias, " + horas_str + " horas, " + minutos_str +
      " minutos e " + segundos_str + " segundos. ")
