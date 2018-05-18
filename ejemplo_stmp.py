from smtplib import SMTP

servidor=SMTP('hotmail.com')
remitente='surionelda@hotmail.com'
destinatario='goenitz7137@hotmail.com'
mensaje='From: %s\nTo: %s\n\n'%(remitente,destinatario)
mensaje+='Hola.\n'
mensaje+='Hasta Luego.\n'

servidor.sendmail(remitente,destinatario,mesnaje)
