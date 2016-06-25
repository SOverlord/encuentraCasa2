import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))


class verPension(webapp2.RequestHandler):
	def get(self):
		#Recuperamos el ID de URL
		idP = int(self.request.get('idPension'))	#Obtenemos ID de URL
		verPens = models.Lugar.get_by_id(idP)		#Buscamos la ID en la BD
		if verPens.int_publicarPension == 1:
			print "Pension activa"
			template = template_env.get_template('verPension.html')
			context = {
				'verPens': verPens 		#Mandamos los datos al HTML
			}
			self.response.out.write(template.render(context))
		else:
			print "Pension no encontrada o no activa"
			self.redirect("/")
application = webapp2.WSGIApplication([('/verPension', verPension)], debug=True)