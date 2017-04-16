


import os



os.system("cls && Title Impz.py                "+\
		"By: LawlietJH                v1.0.7    ")



# Función Que Permite Cambiar el Tamaño de la Pantalla.
def WinSize(Ancho=82, Alto=55):
	
	os.system("mode con: cols={} lines={}".format(Ancho, Alto))



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
		
		[+] El Primer Diccionario recomendado Probar es el Impz-27[0 - 9999999].ZioN.
		
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



if __name__ == "__main__":
	
	WinSize(95,42)
	
	Info()
	
	os.system("Pause")
