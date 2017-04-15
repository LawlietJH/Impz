# -*- Coding: UTF-8 -*-
# 14/04/2017
# Python 3
# Windows
#                       ██╗███╗   ███╗██████╗ ███████╗
#                       ██║████╗ ████║██╔══██╗╚══███╔╝
#                       ██║██╔████╔██║██████╔╝  ███╔╝ 
#                       ██║██║╚██╔╝██║██╔═══╝  ███╔╝  
#                       ██║██║ ╚═╝ ██║██║     ███████╗
#                       ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝
#                                                         By: LawlietJH
#                                                               v1.0.0
# Fuente: 'ANSI Shadow' - Desde: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Impz

import time
import sys
import os



Autor = "LawlietJH"
Version = "v1.0.0"



def Impz():
	
	Total = 10000000
	Minim = 0

	open("Impz-27.ZioN","a")
	Eny = open("Impz-27.ZioN","w")
	
	print("\n\n\n\t [+] Creando Diccionario. 99% Efectivo.")
	print("\n\t    [~] Para Hackear Redes: 'Cisco Pegatron'.")
	print("\n\t    [~] Archivo de Salida:  'Imp-27.ZioN'.")
	print("\n\t    [~] Tamaño Salida Aprox: 100 Mb.")
	print("\n\t    [~] Cantidad de Cadenas:", Total-Minim, "\n\n\n\n")
	
	for x in range(Minim, Total):
				
		if x == 0: Progreso(x+1, Total)
		else:
			if x % 1000 == 0: Progreso(x, Total)
		
		Eny.write("27" + str(x).zfill(7) + "\n")
		
	Eny.close()



def Progreso(x, Total):
	
	TamBar = 30
	Progreso = (x * 100) / Total
	Actual = x / Total
	
	TiempoTransc = int(time.clock()) + 1
	BarraAct = int(Actual * TamBar)
	
	bar = "\r Progreso: {:.2f}%".format(Progreso)
	bar += ' |' + '█'.join(['' for _ in range(BarraAct)])  # Imprimir Progreso.
	bar += ' '.join(['' for _ in range(int(TamBar - BarraAct))]) + '|'
	bar += " [" + Tiempo((Total - x) * (TiempoTransc / x))  + "] "	# Imprimir Tiempo Restante.
	
	sys.stdout.write(bar)



def Tiempo(sec):
	if sec >= 3600:  # Convierte a Horas
		return '{0:d} hora(s)'.format(int(sec / 3600))
	elif sec >= 60:  # Convierte a Minutos
		return '{0:d} minuto(s)'.format(int(sec / 60))
	else:            # Sin Conversión
		return '{0:d} segundo(s)'.format(int(sec))



if __name__ == "__main__":
	
	try:
		Impz()
	except KeyboardInterrupt:
		pass
		
