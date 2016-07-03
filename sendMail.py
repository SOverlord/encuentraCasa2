import webapp2
from google.appengine.api import mail
import jinja2
import os


class sendMail(webapp2.RequestHandler):
	def get(self):
		#Recuperamos la informacion del HTML y la almacenamos en variables locales
		nombre = self.request.get('nombre')
		mailFrom = self.request.get('mailSender')
		mensaje = self.request.get('mensaje')

		#si no metio un correo valido muestra un mensaje un mensaje
		if not mail.is_email_valid(mailFrom):
			self.response.out.write("El correo electronico es invalido")
		else:
			message = mail.EmailMessage(
				sender="encuentra-casa.appspot.com <sc210594@gmail.com>",
				subject="Gracias por tus comentarios"
				)
			message.to = mailFrom
			message.bcc = "Aaron Santos <aesc91@hotmail.com>","Carlos Uscanga <carlos.07um@gmail.com>"
			message.body = mensaje
			message.send()
			self.redirect("/")
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/sendMail', sendMail)],debug=True)