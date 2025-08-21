'''
Ejercicio 10: Determinar el Día de la Semana Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
dia_semana = int(input('Introduce el número del día de la semana: '))
if dia_semana ==1:
  print ('El dia de la semana es lunes')
elif dia_semana ==2:
  print ('El día de la semana es martes')
elif dia_semana ==3:
  print ('El día de la semana es miércoles')
elif dia_semana ==4:
  print ('El día de la semana es jueves')
elif dia_semana ==5:
  print ('El día de la semana es viernes')
elif dia_semana ==6:
  print ('El día de la semana es sabado')
elif dia_semana ==7:
  print ('El día de la semana es domingo')
else:
  print ('no existe este día de la semana')