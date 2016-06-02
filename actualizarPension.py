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
        idPens = int(self.request.get('idP'))    #Obtenemos ID de URL
        print idPens
        pension = models.Lugar.get_by_id(idPens)       #Buscamos la ID en la BD

        if pension:
            #Recuperamos la informacion del HTML y la almacenamos en variables locales
            new_Pension = self.request.get('nombrePension')
            new_NombreArrendador = self.request.get('nombreArrendador')
            new_Ciudad = self.request.get('nombreCiudad')
            new_Tipo = self.request.get('tipo')
            new_telefonoCasa = self.request.get('telefonoCasa')
            new_telefonoCelular = self.request.get('telefonoCelular')
            new_descripcion = self.request.get('descripcion')
        
            #Almacenamos el contenido de las variables locales en la base de datos
            #usuarioF = usr.get()
            #usuarioF.str_sexo = sexo
            #usuarioF.put()

            #actualizacion = pension.get()
            pension.str_nombrePension = new_Pension
            pension.str_descripcion = new_descripcion
            pension.str_nombreArrendador = new_NombreArrendador
            pension.str_ciudad = new_Ciudad
            pension.str_tipo = new_Tipo
            pension.str_telefonoCelular = new_telefonoCelular
            pension.str_telefonoCasa = new_telefonoCasa
            pension.put()

            self.redirect("/adminIndex")
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/actualizarPension', actualizarPension)],config = session_module.myconfig_dict,debug=True)
