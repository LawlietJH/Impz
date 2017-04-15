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
#                                                               v1.0.2
# Fuente: 'ANSI Shadow' - Desde: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Impz

import time
import sys
import os



Autor = "LawlietJH"
Version = "v1.0.2"



def Imp_27(Minim=0):
	
	os.system("cls && Title Creando Diccionario: Impz-27.ZioN.")
	
	Total = 10000000

	open("Impz-27["+str(Minim)+" - "+str(Total-1)+"].ZioN","a")
	Eny = open("Impz-27["+str(Minim)+" - "+str(Total-1)+"].ZioN","w")
	
	print("\n\n\n\t [+] Creando Diccionario. 99% Efectivo.")
	print("\n\t    [~] Para Hackear Redes: 'Cisco Pegatron'.")
	print("\n\t    [~] Archivo de Salida:  'Impz-27["+str(Minim)+" - "+str(Total-1)+"].ZioN'")
	print("\n\t    [~] Tamaño Salida Aprox:", (Total-Minim) / 100000, "Mb")
	print("\n\t    [~] Cantidad de Cadenas:", Total-Minim, "\n\n\n\n")
	
	for x in range(Minim, Total):
				
		if x == 0: Progreso(x+1, Total)
		else:
			if x % 1000 == 0: Progreso(x, Total)
		
		Eny.write("27" + str(x).zfill(7) + "\n")
		
	Eny.close()



def Impz():
	
	while True:
		
		os.system("cls && Title Impz.py                     By: LawlietJH"+\
		          "                    "+Version)
		
		print("""
		
			Menú
		
		[1] - Diccionario Con Prefijo 27. Max[10,000,000]
		[9] - Info.
		[0] - Salir
		
		   >>> """, end="")
		
		try:
			Resp = int(input(""))
			if Resp == 1:
				try:
					if input("\n\n\t Iniciar En Algun Punto [S/N]: ").lower() in ['s','si']:
						try:
							Minim = int(input("\n\n\t Elige Un Número De Inicio [ 0 - 10,000,000 ]: "))
							if Minim >= 0 and Minim <= 10000000: Imp_27(Minim)
							else:
								print("\n\n\t Número Inválido. Se Usara El 0 por Defecto.")
								time.sleep(1.5)
								Imp_27()
						except:
								print("\n\n\t Opción Inválida. Se Usara El 0 por Defecto.")
								time.sleep(1.5)
								Imp_27()
					print("\n\n\n\t\t Terminado Con Exito!")
					time.sleep(3)
				except KeyboardInterrupt:
					print("\n\n\t Cancelando...")
					time.sleep(1.5)
					return
			elif Resp == 9: pass
			elif Resp == 0: break
			else:
				print("\n\n\n\t Elige Una Opción Correcta.")
				time.sleep(1.5)
		except KeyboardInterrupt:
			print("\n\n\t Saliendo...")
			time.sleep(1.5)
			exit(1)
		except:
			print("\n\n\n\t Elige Una Opción Correcta.")
			time.sleep(1.5)
		
		
	
	


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
		
