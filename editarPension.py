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
		  	try:
		  		editarPens.key().id()
		  	except:
		  		print "Pension no encontrada"
		  		self.redirect("/adminIndex")
		  	else:
		  		print "Pension encontrada: "+str(editarPens.key().id())
			  	carrete = db.Query(models.CarreteFotos).filter("str_LugarID", str(idP))		#Cargamos carrete
			  	restFotos = 5	#Fotos maximas en el carrete

			  	#Paso 1-> Eliminamos una foto?
			  	if self.request.get('deletePhoto'):
			  		deleteKey = self.request.get('deletePhoto')
			  		for foto in carrete:
			  			if foto.str_urlFoto == deleteKey:
			  				foto.delete()
			  				restFotos = restFotos+1
			  			else:
			  				pass

			  	#Paso 2-> Comprobamos si existen fotos en el carrete
			  	if not carrete.get():
			  		hayFotosCarrete = 0
			  		#print "No hay fotos en carrete"
			  	else:
			  		hayFotosCarrete = 1
			  		#print "Hay fotos en carrete"
			  		for p in carrete:
			  			restFotos = restFotos - 1
			  		#print restFotos

			  	#Paso 3-> Cargamos las direcciones de template y url's de carga
				template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))
			  	template = template_env.get_template('admin/editarPension.html')
			  	upload_url = blobstore.create_upload_url('/cargarArchivo?file=fotoperfil&idPens='+str(idP))
			  	uploadCarrete = blobstore.create_upload_url('/cargarArchivo?file=fotoCarrete&idPens='+str(idP))

			  	#Paso 4-> Mandamos los datos al HTML
			  	context = {
			   		'editarPens': editarPens,
			   		'upload_url': upload_url,
			   		'uploadCarrete': uploadCarrete,
			   		'hayFotosCarrete': hayFotosCarrete,
			   		'carrete': carrete,
			   		'resFotos': restFotos
			  	}
			  	self.response.out.write(template.render(context))
		else:
		 	self.redirect("/")
application = webapp2.WSGIApplication([('/editarPension', editarPension)], config = session_module.myconfig_dict, debug=True)