# coding= utf-8
# coding= ascii
import webapp2
from google.appengine.api import mail
import jinja2
import os


class sendMailTo(webapp2.RequestHandler):
	def get(self):
		#Recuperamos la informacion del HTML y la almacenamos en variables locales
		nombre = self.request.get('nombre')
		mailFrom = self.request.get('mailSender')
		mensaje = self.request.get('mensaje')
		mailTo = self.request.get('mailTo')
		idPens = self.request.get('idPens')
		nombrePension = self.request.get('namePens')

		#si no metio un correo valido muestra un mensaje un mensaje
		if not mail.is_email_valid(mailFrom):
			self.response.out.write("El correo electronico es invalido")
		else:
			#Mensaje para la pension
			messageToPension = mail.EmailMessage(
				sender="encuentra-casa.appspot.com <sc210594@gmail.com>",
				subject="Has recibido un correo desde tu perfil."
				)
			messageToPension.to = mailTo
			messageToPension.body = """
				Has recibido un mensaje de {}:
				{}
				Para mantener el contacto, responde a la siguiente direccion: {}

				ATENTAMENTE
				El equipo de Encuentra Casa
				Servicio de Respuesta Automática (SRA)
				http://encuentra-casa.appspot.com
			""".format(nombre.encode('utf-8'), mensaje.encode('utf-8'), mailFrom)
			messageToPension.send()
			#TERMINA Mensaje para la pension

			#Mensaje para el que contacto
			messageToSender = mail.EmailMessage(
				sender="encuentra-casa.appspot.com <sc210594@gmail.com>",
				subject="Has enviado un correo a una pension."
				)
			messageToSender.to = mailFrom
			messageToSender.body = """
				Has enviado el siguiente mensaje a la pensión {}:
				{}
				Para regresar a ver esta pensió, haz click en el siguiente link: {}


				ATENTAMENTE
				El equipo de Encuentra Casa
				Servicio de Respuesta Automática (SRA)
				http://encuentra-casa.appspot.com
			""".format(nombrePension.encode('utf-8'), mensaje.encode('utf-8'), "http://encuentra-casa.appspot.com/verPension?idPension="+idPens )
			messageToSender.send()
			#TERMINA Mensaje para el que contacto

			#Mensaje para nosotros
			messageToAdmin = mail.EmailMessage(
				sender="encuentra-casa.appspot.com <sc210594@gmail.com>",
				subject="Han enviado un mensaje."
			)
			messageToAdmin.to = "Aaron Santos <aesc91@hotmail.com>","Carlos Uscanga <carlos.07um@gmail.com>"
			messageToAdmin.body = """
				Se ha enviado el siguiente mensaje: {}
				De: {}
				Para: {}
				IdPension: {}
			""".format(mensaje.encode('utf-8'), mailFrom.encode('utf-8'), mailTo.encode('utf-8'), idPens)
			messageToAdmin.send()
			#TERMINA Mensaje para nosotros

		self.redirect("/verPension?idPension="+idPens)
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/sendMailTo', sendMailTo)],debug=True)