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
#                                                               v1.0.5
# Fuente: 'ANSI Shadow' - Desde: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Impz

import time
import sys
import os



Autor = "LawlietJH"
Version = "v1.0.5"



def Imp_27(Minim=0):
	
	Total = 10000000
	CantCad = Total - Minim
	Tam = ((Total-Minim) / 100000) * 1.04
	
	os.system("cls && Title Creando Diccionario: Impz-27["+str(Minim)+" - "+str(Total-1)+"].ZioN")
	
	open("Impz-27["+str(Minim)+" - "+str(Total-1)+"].ZioN","a")
	Eny = open("Impz-27["+str(Minim)+" - "+str(Total-1)+"].ZioN","w")
	
	print("\n\n\n\t [+] Creando Diccionario. 99% Efectivo.")
	print("\n\t    [~] Para Hackear Redes: 'Cisco Pegatron'.")
	print("\n\t    [~] Archivo de Salida:  'Impz-27["+str(Minim)+" - "+str(Total-1)+"].ZioN'")
	print("\n\t    [~] Tamaño Salida Aprox:", Tam, "Mb")
	print("\n\t    [~] Cantidad de Cadenas:", CantCad, "\n\n\n\n")
	
	for x in range(Minim, Total):
				
		if x == 0: Progreso(x+1, Total)
		else:
			if x % 1000 == 0: Progreso(x, Total)
		
		Eny.write("27" + str(x).zfill(7) + "\n")
		
	Eny.close()



def Info():
	
	print("""
	
		[!] ESSID = Nombre De Red.
		[!] BSSID = Dirección MAC.
		[!] Key WPA = Contraseña De La Red. 

	[~] Información:
	
		[+] Las Contraseñas de estas Redes siempre son Números.
		[+] Siempre tienen una Contraseña de 9 Digitos.
		[+] Siempre Comienzan Con el Número 2.
		[+] El Segundo Digito Normalmente Es el 7.
		
			[*] El segundo Digito varia entre el 6 y el 8.
		
		[+] El Primer Diccionario recomendado Probar es el Imp-27.ZioN.
		
			[*] La Mayoria De Las Redes Cisco Pegatron empiezan con 27.
		
		[+] Las Redes 'Cisco Pegatron' Se Ven De La Siguiente Manera:
			
			[*] Ejemplo de ESSID, BSSID y Key WPA:
				
				[-] ~ ESSID = 1bf0a2
				[-] ~ BSSID = 00:71:C2:21:FE:A8
				[-] Key WPA = 274345388
				
			[*] Ejemplos de ESSID's:
				
				[-] c3f2ba
				[-] e922e8
				[-] aad92a
				[-] ab0cb8
				[-] b5967a
				    etc...
			
	""")



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
				
				while True:
					
					os.system("cls && Title Creación De Diccionario Con Prefijo 27. Max[10,000,000]")
					
					try:
						
						print("\n\n\t Creación De Diccionario Con Prefijo 27. Max[10,000,000]"+\
							  "\n\n\n\t [1] Iniciar En Algun Punto."+\
							  "\n\t [2] Iniciar Normal [Desde 0 - 9,999,999]."+\
							  "\n\t [0] Volver."+\
							  "\n\n\t >>> ", end="")
						
						Resp2 = int(input(""))
						
						if Resp2 == 1:
							
							try:
								
								Minim = int(input("\n\n\t Elige Un Número De Inicio [ 0 - 10,000,000 ]: "))
								
								if Minim >= 0 and Minim <= 10000000: Imp_27(Minim)
								else:
									print("\n\n\t Número Inválido. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Imp_27()
									
							except KeyboardInterrupt:
								print("\n\n\t Cancelando...")
								time.sleep(1.5)
								break
								
							except:
									print("\n\n\t Opción Inválida. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Imp_27()
						
							print("\n\n\n\t\t Terminado Con Exito!")
							time.sleep(3)
							
						elif Resp2 == 2: Imp_27()
						elif Resp2 == 0: break
						else:
							print("\n\n\n\t Elige Una Opción Correcta.")
							time.sleep(1.5)
						
					except KeyboardInterrupt:
						print("\n\n\t Cancelando...")
						time.sleep(1.5)
						return
					
					except:
						print("\n\n\n\t Elige Una Opción Correcta.")
						time.sleep(1.5)
			
			elif Resp == 9:
				
				Info()
				os.system("Pause > Nul")
				
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
		
