import webapp2
from google.appengine.api import mail
import models
import jinja2
import os
import datetime

from google.appengine.ext import db

class registrarNuevaPension(webapp2.RequestHandler):
    def post(self):
        #Recuperamos la informacion del HTML y la almacenamos en variables locales
        l_nombrePension = self.request.get('nombrePension')
        l_nombreArrendador = self.request.get('nombreArrendador')
        l_ciudad = self.request.get('ciudad')
        l_direccion = self.request.get('direccion')
        l_cp = self.request.get('cp')
        l_telCasa = self.request.get('telefonoCasa')
        l_telCel = self.request.get('telefonoCelular')
        l_tipo = self.request.get('tipo')
        l_descripcion = self.request.get('descripcion')
        
        
        #Almacenamos el contenido de las variables locales en la base de datos
        pension = models.Lugar()
        pension.str_nombrePension = l_nombrePension
        pension.str_nombreArrendador = l_nombreArrendador
        pension.str_ciudad = l_ciudad
        pension.str_direccion = l_direccion
        pension.str_cp = l_cp
        pension.str_tipo = l_tipo
        pension.str_telefonoCasa = l_telCasa
        pension.str_telefonoCelular = l_telCel
        pension.str_descripcion = l_descripcion
        
        pension.str_urlFotoPerfil = "0" #significa que no tiene imagen
        #colocamos esas variables en el objeto usuario
        pension.put()

        #si no metio un correo valido muestra un mensaje un mensaje
        self.redirect("/adminIndex")
	
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/registrarNuevaPension', registrarNuevaPension)],debug=True)


