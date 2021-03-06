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
#                                                               v1.1.1
# Fuente: 'ANSI Shadow' - Desde: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Impz

import time
import sys
import os



Autor = "LawlietJH"
Version = "v1.1.1"



# Función Que Permite Esconder El Cursor de la Pantalla (La rayita que parpadea xD).
def HiddenCursor(imp="Hide"):
	
	#~ imp = imp.title()		#Devuelve la cadena solo con la primera letra de cada palabra en mayuscula
	imp = imp.capitalize()		#Devuelve la cadena solo con la primera letra de la primer palabra en mayuscula

	if os.name == 'nt':
		import msvcrt
		import ctypes

		class _CursorInfo(ctypes.Structure):
			_fields_ = [("size", ctypes.c_int),
						("visible", ctypes.c_byte)]
	
	def hide_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = False
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25l")
			sys.stdout.flush()

	def show_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = True
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25h")
			sys.stdout.flush()
	
		
	if imp == "Hide": hide_cursor()
	elif imp =="Show": show_cursor()
	else: return



def Pausa():
	
	os.system("Pause > Nul ")



#=======================================================================



# Abre Una Nueva Ventana Para Ejecutar Otro Script.
def Run(Programa=""):
	
	#=======================================================================
	
	def Chk_Dep():
		
		try:
			import win32api
			
		except ModuleNotFoundError:
			print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
			os.system("Title Instalando pypiwin32 && pip install pypiwin32 > Nul && cls && Title Pandoraz.py            By: LawlietJH")
			
		except Exception as ex:
			print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.
	
	Chk_Dep()				#~ Se instala el módulo keyboard si este no esta instalado.
	try:
		import win32api, win32con, win32event, win32process	# Se Importan Módulos de pypiwin32.
		from win32com.shell.shell import ShellExecuteEx
		from win32com.shell import shellcon
	except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
		print("\n\n   No se pudo instalar correctamente el Módulo 'pypiwin32'.")
		print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
		print("\n\t 'pip install keyboard'   o   ' pip3 install keyboard'")
		
		try:
			os.system("Pause > Nul")
		except KeyboardInterrupt: pass
		
		#~ Dat()
		Salir(0)
	
	#=======================================================================
	
	import traceback, types
	
	showCmd = win32con.SW_SHOWNORMAL
	cmd = Programa
	params = ''
	cmdDir = ''
	lpVerb = ''
	
	procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)
	#~ procInfo = ShellExecuteEx(nShow=showCmd, fMask=shellcon.SEE_MASK_NOCLOSEPROCESS, lpVerb=lpVerb, lpFile=cmd, lpParameters=params)
	
	#~ http://pt.stackoverflow.com/questions/6929/como-rodar-um-subprocess-com-permiss%C3%A3o-de-administrador



#=======================================================================



def Impz_27(Minim=0):
	
	Total = 10000000
	CantCad = Total - Minim
	Tam = ((Total-Minim) / 100000) * 1.04
	
	Cony = str(Minim)+" - "+str(Total-1)
	
	os.system("cls && Title Creando Diccionario: Impz-27["+Cony+"].ZioN")
	
	open("Impz-27["+Cony+"].ZioN","a")
	Eny = open("Impz-27["+Cony+"].ZioN","w")
	
	print("\n\n\n\t [+] Creando Diccionario. 99% Efectivo.")
	print("\n\t    [~] Para Hackear Redes: 'Cisco Pegatron'.")
	print("\n\t    [~] Archivo de Salida:  'Impz-27["+Cony+"].ZioN'")
	print("\n\t    [~] Tamaño Salida Aprox:", Tam, "Mb")
	print("\n\t    [~] Cantidad de Cadenas:", CantCad, "\n\n\n\n")
	
	for x in range(Minim, Total):
				
		if x == 0: Progreso(x+1, Total)
		else:
			if x % 1000 == 0: Progreso(x, Total)
		
		Eny.write("27" + str(x).zfill(7) + "\n")
		
	Eny.close()



def Impz_28(Minim=0):
	
	Total = 10000000
	CantCad = Total - Minim
	Tam = ((Total-Minim) / 100000) * 1.04
	
	Cony = str(Minim)+" - "+str(Total-1)
	
	os.system("cls && Title Creando Diccionario: Impz-28["+Cony+"].ZioN")
	
	open("Impz-28["+Cony+"].ZioN","a")
	Eny = open("Impz-28["+Cony+"].ZioN","w")
	
	print("\n\n\n\t [+] Creando Diccionario. 99% Efectivo.")
	print("\n\t    [~] Para Hackear Redes: 'Cisco Pegatron'.")
	print("\n\t    [~] Archivo de Salida:  'Impz-28["+Cony+"].ZioN'")
	print("\n\t    [~] Tamaño Salida Aprox:", Tam, "Mb")
	print("\n\t    [~] Cantidad de Cadenas:", CantCad, "\n\n\n\n")
	
	for x in range(Minim, Total):
				
		if x == 0: Progreso(x+1, Total)
		else:
			if x % 1000 == 0: Progreso(x, Total)
		
		Eny.write("28" + str(x).zfill(7) + "\n")
		
	Eny.close()



def Impz_26(Minim=0):
	
	Total = 10000000
	CantCad = Total - Minim
	Tam = ((Total-Minim) / 100000) * 1.04
	
	Cony = str(Minim)+" - "+str(Total-1)
	
	os.system("cls && Title Creando Diccionario: Impz-26["+Cony+"].ZioN")
	
	open("Impz-26["+Cony+"].ZioN","a")
	Eny = open("Impz-26["+Cony+"].ZioN","w")
	
	print("\n\n\n\t [+] Creando Diccionario. 99% Efectivo.")
	print("\n\t    [~] Para Hackear Redes: 'Cisco Pegatron'.")
	print("\n\t    [~] Archivo de Salida:  'Impz-26["+Cony+"].ZioN'")
	print("\n\t    [~] Tamaño Salida Aprox:", Tam, "Mb")
	print("\n\t    [~] Cantidad de Cadenas:", CantCad, "\n\n\n\n")
	
	for x in range(Minim, Total):
				
		if x == 0: Progreso(x+1, Total)
		else:
			if x % 1000 == 0: Progreso(x, Total)
		
		Eny.write("26" + str(x).zfill(7) + "\n")
		
	Eny.close()



def Impz():
	
	while True:
		
		os.system("cls && Title Impz.py                "+\
		   "By: LawlietJH                "+Version+"    ")
		
		print("""
		
			 Menú
	
	[1] - Diccionario Con Prefijo 27. Max[10,000,000] - (Recomendado)
	
	[2] - Diccionario Con Prefijo 28. Max[10,000,000]
	
	[3] - Diccionario Con Prefijo 26. Max[10,000,000]
	
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
							  "\n\n\n\t [1] Iniciar Normal [Desde 0 - 9,999,999]."+\
							  "\n\t [2] Iniciar En Algun Punto."+\
							  "\n\t [0] Volver."+\
							  "\n\n\t >>> ", end="")
						
						Resp2 = int(input(""))
						
						if Resp2 == 1: Impz_27()
						elif Resp2 == 2:
							
							try:
								
								Minim = int(input("\n\n\t Elige Un Número De Inicio [ 0 - 10,000,000 ]: "))
								
								if Minim >= 0 and Minim <= 10000000: Impz_27(Minim)
								else:
									print("\n\n\t Número Inválido. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Impz_27()
									
							except KeyboardInterrupt:
								print("\n\n\t Cancelando...")
								time.sleep(1.5)
								break
								
							except:
									print("\n\n\t Opción Inválida. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Impz_27()
						
							print("\n\n\n\t\t Terminado Con Exito!")
							Pausa()
							
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
			
			if Resp == 2:
				
				while True:
					
					os.system("cls && Title Creación De Diccionario Con Prefijo 28. Max[10,000,000]")
					
					try:
						
						print("\n\n\t Creación De Diccionario Con Prefijo 28. Max[10,000,000]"+\
							  "\n\n\n\t [1] Iniciar Normal [Desde 0 - 9,999,999]."+\
							  "\n\t [2] Iniciar En Algun Punto."+\
							  "\n\t [0] Volver."+\
							  "\n\n\t >>> ", end="")
						
						Resp2 = int(input(""))
						
						if Resp2 == 1: Impz_28()
						elif Resp2 == 2:
							
							try:
								
								Minim = int(input("\n\n\t Elige Un Número De Inicio [ 0 - 10,000,000 ]: "))
								
								if Minim >= 0 and Minim <= 10000000: Impz_28(Minim)
								else:
									print("\n\n\t Número Inválido. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Impz_28()
									
							except KeyboardInterrupt:
								print("\n\n\t Cancelando...")
								time.sleep(1.5)
								break
								
							except:
									print("\n\n\t Opción Inválida. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Impz_28()
						
							print("\n\n\n\t\t Terminado Con Exito!")
							Pausa()
							
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
			
			if Resp == 3:
				
				while True:
					
					os.system("cls && Title Creación De Diccionario Con Prefijo 26. Max[10,000,000]")
					
					try:
						
						print("\n\n\t Creación De Diccionario Con Prefijo 26. Max[10,000,000]"+\
							  "\n\n\n\t [1] Iniciar Normal [Desde 0 - 9,999,999]."+\
							  "\n\t [2] Iniciar En Algun Punto."+\
							  "\n\t [0] Volver."+\
							  "\n\n\t >>> ", end="")
						
						Resp2 = int(input(""))
						
						if Resp2 == 1: Impz_26()
						elif Resp2 == 2:
							
							try:
								
								Minim = int(input("\n\n\t Elige Un Número De Inicio [ 0 - 10,000,000 ]: "))
								
								if Minim >= 0 and Minim <= 10000000: Impz_26(Minim)
								else:
									print("\n\n\t Número Inválido. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Impz_26()
									
							except KeyboardInterrupt:
								print("\n\n\t Cancelando...")
								time.sleep(1.5)
								break
								
							except:
									print("\n\n\t Opción Inválida. Se Usara El 0 por Defecto.")
									time.sleep(1.5)
									Impz_26()
						
							print("\n\n\n\t\t Terminado Con Exito!")
							Pausa()
							
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
				
				Run("Info.py")
				
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
	
	HiddenCursor()
	
	try:
		Impz()
	except KeyboardInterrupt:
		pass
		
