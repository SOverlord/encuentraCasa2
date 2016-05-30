import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))


class editarPension(webapp2.RequestHandler):
	def get(self):
		#Recuperamos el ID de URL
		idP = int(self.request.get('idPension'))	#Obtenemos ID de URL
	  	editarPens = models.Lugar.get_by_id(idP)		#Buscamos la ID en la BD
	  	template = template_env.get_template('editarPension.html')
	  	context = {
	   		'editarPens': editarPens 		#Mandamos los datos al HTML
	  	}
	  	self.response.out.write(template.render(context))
application = webapp2.WSGIApplication([('/editarPension', editarPension)], debug=True)