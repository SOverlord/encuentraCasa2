import jinja2
import os
import webapp2
from webapp2_extras import sessions
import crearSesion
import session_module
from google.appengine.ext import blobstore
import models
from google.appengine.ext import db

class editarPension(session_module.BaseSessionHandler):
	def get(self):
		#Recuperamos el ID de URL
		if self.session.get('usuario'):
			idP = int(self.request.get('idPension'))	#Obtenemos ID de URL
		  	editarPens = models.Lugar.get_by_id(idP)		#Buscamos la ID en la BD
			template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))
		  	template = template_env.get_template('admin/editarPension.html')

		  	upload_url = blobstore.create_upload_url('/cargarArchivo?file=fotoperfil&idPens='+str(idP))
		  	context = {
		  		#Mandamos los datos al HTML
		   		'editarPens': editarPens,
		   		'upload_url': upload_url
		  	}
		  	self.response.out.write(template.render(context))
		else:
		 	self.redirect("/")
application = webapp2.WSGIApplication([('/editarPension', editarPension)], config = session_module.myconfig_dict, debug=True)