#!/usr/bin/python
# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.parser import Parser
import smtplib
import poplib
from time import sleep
import sys
import os

#datos

password = 'AreaMicro1'
origen = 'estufa.unsl@gmail.com'

Lista = ["Foto","foto","FOTO","Captura","captura","CAPTURA","Imagen","imagen",
	"IMAGEN","Enviar foto","enviar foto", "Enviar Foto", "enviar Foto",
	"ENVIAR FOTO", "Re: Foto Cultivo Bacteriano", "Re: Foto", "Re: Captura",
	"Re: foto","Re: FOTO"]

# Se establece conexion con el servidor pop de gmail para ver si hay emails nuevos.

m = poplib.POP3_SSL('pop.gmail.com',995)
m.user(origen)
m.pass_(password)

#Me fijo la cantidad de nuevos mensajes
numero = len(m.list()[1])
print numero
#Si numero es distinto de cero es por que hay mensajes nuevos.
j = 0
if numero != 0:
	#Se toma la foto
	os.system("python /home/micro/Estufa/led.py on && sleep 5 && fswebcam /home/micro/Estufa/images/Estufa.jpeg && python /home/micro/Estufa/led.py off")

	#Se establece conexion con smtp.gmail.com
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	msg = MIMEMultipart()
	msg["From"] = origen
	msg["subject"] = "Foto Cultivo Bacteriano"

	server.login(msg["From"],password)

	#Analizo los mensajes
	for i in range(numero):
		j = j+1
		# Se lee el mensaje
		response, headerLines, bytes = m.retr(i+1)

		#Se une todo en un solo string
		mensaje='\n'.join(headerLines)

		#Se parsea el mensaje
		p = Parser()
	 	email = p.parsestr(mensaje)

		#Aqui ya se tienen los datos de forma entendible

		if email["Subject"] in Lista:

			# setup the parameters of the message

			msg['To'] = email["From"]

			#Adjunto la foto del cultivo bacteriano

			file = open("/home/micro/Estufa/images/Estufa.jpeg", "rb")
			contenido = MIMEImage(file.read())
			contenido.add_header('Content-Disposition', 'attachment; filename = "Estufa.jpeg"')
			msg.attach(contenido)

			# send the message via the server.
			server.sendmail(msg['From'], msg['To'], msg.as_string())

		sleep(5)
	server.quit()
m.quit()
