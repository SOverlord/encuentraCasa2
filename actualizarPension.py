import jinja2
import os
import webapp2
import models
from webapp2_extras import sessions
import crearSesion
import session_module

from google.appengine.api import users
from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))

class actualizarPension(session_module.BaseSessionHandler, webapp2.RequestHandler):
	def post(self):
		#Recuperamos el ID de la pension
		idPens = int(self.request.get('idP'))	#Obtenemos ID de URL
		try:
			pension = models.Lugar.get_by_id(idPens)		#Buscamos la ID en la BD
		except:
			print "Error recuperando pension"
		else:
			print "Pension a editar: "+str(idPens)
			#Recuperamos la informacion del HTML y la almacenamos en variables locales
			new_NombrePension = self.request.get('nombrePension')
			new_NombreArrendador = self.request.get('nombreArrendador')
			new_Ciudad = self.request.get('nombreCiudad')
			new_Direccion = self.request.get('direccion')
			new_CP = self.request.get('cp')
			new_email = self.request.get('email', default_value='0')
			new_telefonoCasa = self.request.get('telefonoCasa')
			new_telefonoCelular = self.request.get('telefonoCelular')

			new_TipoLugar = self.request.get('tipoLugar')
			new_Tipo = self.request.get('tipo')
			new_RentaMensual = int(self.request.get('rentaMensual'))
			new_descripcion = self.request.get('descripcion')

			l_luz = self.request.get('servicio1', default_value='False')
			l_internet = self.request.get('servicio2', default_value='False')
			l_cable = self.request.get('servicio3', default_value='False')
			l_telefono = self.request.get('servicio4', default_value='False')
			l_lavanderia = self.request.get('servicio5', default_value='False')
			l_comida = self.request.get('servicio6', default_value='False')
			l_aguaCaliente = self.request.get('servicio7', default_value='False')
			l_amueblado = self.request.get('servicio8', default_value='False')
			l_limpieza = self.request.get('servicio9', default_value='False')

			pension.str_nombrePension = new_NombrePension
			pension.str_nombreArrendador = new_NombreArrendador
			pension.str_ciudad = new_Ciudad
			pension.str_direccion = new_Direccion
			pension.str_cp = new_CP
			pension.str_email = new_email
			pension.str_telefonoCasa = new_telefonoCasa
			pension.str_telefonoCelular = new_telefonoCelular
			pension.str_tipo = new_Tipo
			pension.str_tipoLugar = new_TipoLugar
			pension.txt_descripcion = new_descripcion
			pension.int_rentaMensual = new_RentaMensual
			pension.str_luz = l_luz
			pension.str_internet = l_internet
			pension.str_cable = l_cable
			pension.str_telefono = l_telefono
			pension.str_lavanderia = l_lavanderia
			pension.str_comida = l_comida
			pension.str_aguaCaliente = l_aguaCaliente
			pension.str_amueblado = l_amueblado
			pension.str_limpieza = l_limpieza
			pension.put()
			self.redirect("/editarPension?idPension="+str(idPens))

		#/actualizarPension?idP={{editarPens.key().id()}}
#controler, clase, debug
application = webapp2.WSGIApplication([('/actualizarPension', actualizarPension)],config = session_module.myconfig_dict,debug=True)
