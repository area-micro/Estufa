#!/usr/bin/python
import time
import os
import sys 

comilla = '"'
porcentaje = '%'

#Se obtiene la fecha y hora
fyh = time.strftime("%c")
print(fyh)
#Se abre el archivo 
f= open('index.html','r+')	#lectura y escritura

# Se comienza a leer el archivo
linea = f.readline();


#Se encuentra la linea donde se especifica la fecha y hora, y se actualiza
while linea != '':	#mientras no se termine el archivo
	linea = f.readline()
	#Cuando se encuentra el sector de codigo donde se especifica la fecha y hora, se modifica
	if linea == '				<!-- FECHA Y HORA -->\n':
		print(f.tell())
		f.seek(f.tell(),0)
		f.write('				<font size=%c30%c%c>%s</font>\n'%(comilla,porcentaje,comilla,fyh))
		linea = ''
	
#Se cierra el archivo
f.close()



#Se ejecutan comandos de git, para actualizar la informacion
#os.system('cd /home/micro/Estufa')
#os.system('git add -A')
#os.system('git commit -m "%s"'%(fyh))
#os.system('git push origin gh-pages')
