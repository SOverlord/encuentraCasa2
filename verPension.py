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
		try:
			verPens.int_publicarPension == 1
		except:
			print "Pension no encontrada o inactiva"
			self.redirect("/")
		else:
				carrete = db.Query(models.CarreteFotos).filter("str_LugarID", str(idP))		#Cargamos carrete
				fotos = 0
				if not carrete.get():
			  		hayFotosCarrete = 0
			  		#print "No hay fotos en carrete"
			  	else:
			  		hayFotosCarrete = 1
			  		#print "Hay fotos en carrete"
				template = template_env.get_template('verPension.html')
				context = {
					'verPens': verPens, 		#Mandamos los datos al HTML
					'hayFotosCarrete': hayFotosCarrete,
			   		'carrete': carrete
				}
				self.response.out.write(template.render(context))
			
application = webapp2.WSGIApplication([('/verPension', verPension)], debug=True)