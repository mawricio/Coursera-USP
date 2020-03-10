#PROGRAMA QUANTIDADE DE SEGUNDOS
segundos_str =  input('Por favor, etre com o nº segundos que deseja converter: ')
total_segs = int(segundos_str)
dias = total_segs // 86400
segs_restantes = total_segs % 86400
horas = segs_restantes // 3600
segs_restantes = segs_restantes % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60
print(dias, 'dia(s)', horas, 'hora(s)', minutos, 'minuto(s) e ', segs_restantes_final, 'segundo(s)' )

