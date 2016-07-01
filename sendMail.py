import webapp2
from google.appengine.api import mail
import jinja2

#Comportamiento doble para envio de formulario de comentarios a la pagina y contacto a las pensiones.
class sendMail(webapp2.RequestHandler):
	def get(self):
		#Recuperamos la informacion del HTML y la almacenamos en variables locales
		nombre = self.request.get('nombre')
		mailFrom = self.request.get('mailSender')
		mensaje = self.request.get('mensaje')

		try:
			#Buscamos si hay un correo extra.
			mailPension = self.reques.get('mailTo')
		except:
			#Si mailPension no existe, entonces estan enviando comentarios a la pagina
			print "Desde el formulario de contacto de index"
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
		else:
			#Si mailPension existe, estan contactando a la pension idP
			print "Desde el formulario de contacto de verPension"
			idP = self.reques.get('idPens')
			print idP
			if not mail.is_email_valid(mailFrom):
				self.response.out.write("El correo electronico es invalido")
			else:
				message = mail.EmailMessage(
					sender="encuentra-casa.appspot.com <sc210594@gmail.com>",
					subject="Te han enviado un correo desde tu perfil en Encuentra Casa"
				)
				message.to = mailPension
				message.bcc = "Aaron Santos <aesc91@hotmail.com>","Carlos Uscanga <carlos.07um@gmail.com>"
				message.body = mensaje+"Responder a: "+str(mailFrom)
				message.send()

				message2 = mail.EmailMessage(
					sender="encuentra-casa.appspot.com <sc210594@gmail.com>",
					subject="Gracias por tu contacto. En breve recibir\xc3s respuesta."
				)
				message2.to = mailFrom
				message2.body = mensaje
				message2.send()
				self.redirect("/verPension?idPension="+str(idP))
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/sendMail', sendMail)],debug=True)