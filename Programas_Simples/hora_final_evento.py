#La tareaes preparar un código simple para evaluar o encontrar el tiempo final de un periodo
#de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59. El resultado debe ser mostrado en la consola.
#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
# coloca tu código aqui
tiempo_final_min = (hora * 60) + min + dura
tiempo_final_hor = tiempo_final_min//60
min_restantes = tiempo_final_min % 60
print ("El evento comienza a las " + str(hora) + ":" + str(min) + " y dura " + str(dura) + " minutos ")
print ("El evento terminara a las " + str(tiempo_final_hor) + ":" + str(min_restantes))
