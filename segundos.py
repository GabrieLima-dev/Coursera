entrada_segundos = int(
    input("Por favor, entre com o número de segundos que deseja converter: "))

horas = entrada_segundos // 3600
dias = horas // 86400
segundos_restantes = entrada_segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

horas_str = str(horas)
dias_str = str(dias)
minutos_str = str(minutos)
segundos_str = str(segundos_restantes_final)

print(dias_str + " dias " + horas_str + " horas, " + minutos_str +
      " minutos e " + segundos_str + " segundos. ")
