#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************#
#  Programa de Transferencia de Archivos  #
#       Ing. Kennedy Sanchez              #
#   (Security + MGP + PS. Auditor)        #
#     @ksanchez_cld on twitter            #  
# **************************************** 

'''
1- Escannerar red en busca de ip
2- Conectarse a Servicio SSH
3- Verificar el Hostname y Maccadd
4- Verificar existencia de carpetas a resguardar.
5- Verificar carpeta de destino.
6- Transeferir los datos.
7- Comprimirlos en el disco local.
8- Colocar Password.
9- Eliminar la carpeta sin comprimir una vez complete.
10- Enviar un correo de notificacion.
'''
import paramiko
import os
import subprocess
import time

class color:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

FIXEDIPADD   = ''
SMARTPHONENAME = 'android'
SMARTPHONEMACADD = ''
PORT       = 22
USERNAME   = 'root'
PASSWORD   = ''
WLAN       = ''
ETH        = ''

def scanSmartPhone(FIXEDIPADD):
	ping = subprocess.Popen(['ping', '-c 1', FIXEDIPADD], stdout= subprocess.PIPE)
	stdout = ping.stdout.read()
	if "bytes from" in stdout:
		os.system('clear')
		print "*"*50
		print color.BLUE + "Se conecto el bandido. Let's back it up! :D" + color.ENDC
		print "*"*50
		time.sleep(5)
		sshConnect()
	else:
		print "*"*50
		print color.RED + "I'm sorry. We have some connection issues :(" + color.ENDC
		print "*"*50

def sshConnect():

	cnx = paramiko.Transport((FIXEDIPADD, PORT))
	#cnx.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	time.sleep(3)
	try:
		print "Trying to Connect...!"
		cnx.connect(username = USERNAME, password = PASSWORD)
		

	except paramiko.AuthenticationException:
		print "[-]Failed to connect..."
	
#	channel = cnx.open_session()
#	channel.exec_command('hostname')

#	salida = channel.makefile('rb', -1).readlines()
#	if salida:
#		print salida
#	else:
#		print channel.makefile_stderr('rb', -1).readlines()

#STARTTESTING...
	sftp = paramiko.SFTPClient.from_transport(cnx)
	files2txfr = sftp.listdir('/tmp/test/')
	for files in files2txfr:
		print color.RED + "*"*50
		print color.GREEN + "Hold on. Copying files...", files + color.ENDC
		print color.RED + "*"*50 + color.ENDC
		sftp.get(os.path.join('/tmp/test/',files),files)
	#cnx.close()
#ENDTESTING...

def nodeVrfy():
	pass

def dataTxfr():
	sftp = paramiko.SFTPClient.from_transport(cnx)
	files2txfr = sftp.listdir('/tmp/test/')
	for files in files2txfr:
		print color.RED + "*"*50 + color.ENDC
		print color.GREEN + "Hold on. Copying files...", files + color.ENDC
		print color.RED + "*"*50 + color.ENDC
		sftp.get(os.path.join('/tmp/test/', files), files)
	cnx.close()


def dataCompress():
	pass

def emailNotify():
	pass

def cleaningUp():
	pass

if __name__== "__main__":
	scanSmartPhone(FIXEDIPADD)