import webapp2
from google.appengine.api import mail
import models
import jinja2
import os
from datetime import datetime
import time
import horaMx

from google.appengine.ext import db

class registrarNuevaPension(webapp2.RequestHandler):
    def post(self):
        #Recuperamos la informacion del HTML y la almacenamos en variables locales
        YY = str(horaMx.mexTime().getAno())
        MM = str(horaMx.mexTime().getMes())
        DD = str(horaMx.mexTime().getDia())
        hh = str(horaMx.mexTime().getHora())
        mm = str(horaMx.mexTime().getMinuto())

        int_registerDate = int(YY+MM+DD+hh+mm)
        str_registerDate = str(YY+"-"+DD+"-"+MM+" "+hh+":"+mm)

        l_renta = int(self.request.get('costoRenta'))
        l_nombrePension = self.request.get('nombrePension')
        l_nombreArrendador = self.request.get('nombreArrendador')
        l_ciudad = self.request.get('ciudad')
        l_direccion = self.request.get('direccion')
        l_cp = self.request.get('cp')
        l_email = self.request.get('email', default_value='0')
        l_telCasa = self.request.get('telefonoCasa')
        l_telCel = self.request.get('telefonoCelular')
        l_tipo = self.request.get('tipo')
        l_tipoLugar = self.request.get('tipoLugar')
        l_descripcion = self.request.get('descripcion')

        l_luz = self.request.get('servicio1', default_value='False')
        l_internet = self.request.get('servicio2', default_value='False')
        l_cable = self.request.get('servicio3', default_value='False')
        l_telefono = self.request.get('servicio4', default_value='False')
        l_lavanderia = self.request.get('servicio5', default_value='False')
        l_comida = self.request.get('servicio6', default_value='False')
        l_aguaCaliente = self.request.get('servicio7', default_value='False')
        l_amueblado = self.request.get('servicio8', default_value='False')
        l_limpieza = self.request.get('servicio9', default_value='False')

        #Almacenamos el contenido de las variables locales en la base de datos
        pension = models.Lugar()
        pension.str_fechaRegistro = str_registerDate
        pension.int_fechaRegistro = int_registerDate
        pension.int_rentaMensual = l_renta
        pension.str_nombrePension = l_nombrePension
        pension.str_nombreArrendador = l_nombreArrendador
        pension.str_ciudad = l_ciudad
        pension.str_direccion = l_direccion
        pension.str_cp = l_cp
        pension.str_email = l_email
        pension.str_telefonoCasa = l_telCasa
        pension.str_telefonoCelular = l_telCel
        pension.str_tipo = l_tipo
        pension.str_tipoLugar = l_tipoLugar
        pension.txt_descripcion = l_descripcion

        pension.str_luz = l_luz
        pension.str_internet = l_internet
        pension.str_cable = l_cable
        pension.str_telefono = l_telefono
        pension.str_lavanderia = l_lavanderia
        pension.str_comidas = l_comida
        pension.str_aguaCaliente = l_aguaCaliente
        pension.str_amueblado = l_amueblado
        pension.str_limpieza = l_limpieza
        
        pension.int_publicarPension = 1 #Se publica automaticamente
        pension.str_urlFotoPerfil = "0" #significa que no tiene imagen
        #colocamos esas variables en el objeto pension
        pension.put()

        #keyPension = str(pension.key())
        #print "Nueva pension. KEY-> "+keyPension
        #self.redirect("/adminIndex")

        idPension = str(pension.key().id_or_name())
        #print "Nueva pension. ID -> "+idPension #4748790720364544
        self.redirect("/editarPension?idPension="+idPension)
	
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/registrarNuevaPension', registrarNuevaPension)],debug=True)


