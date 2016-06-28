import datetime
import jinja2
import os
import webapp2
import models
import json


class getLugaresREST(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/json'
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    #Query para obtener todos los registros de pensiones
    showPensiones = models.Lugar.all()

    #Corchete para enviar arreglo de objetos
    self.response.out.write("[")

    i = 0

    for pension in showPensiones:

        #Si hay mas de un objeto, ponemos comas para separarlos
    	if i != 0 :
    		self.response.out.write(",")

        #Aumentamos el contador
    	i = i + 1

        #Creamos el arreglo del objeto correspondiente al registro de una pension
    	qanek = {
    		"ID" : pension.key().id(),
            "int_rentaMensual" : pension.int_rentaMensual,
            "str_fechaRegistro" : pension.str_fechaRegistro,
            "int_publicarPension" : pension.int_publicarPension,
            "str_nombrePension" : pension.str_nombrePension,
            "str_nombreArrendador" : pension.str_nombreArrendador,
            "str_urlFotoPerfil" : pension.str_urlFotoPerfil,
            "txt_descripcion" : pension.txt_descripcion,
            "str_tipoLugar" : pension.str_tipoLugar,
            "str_ciudad" : pension.str_ciudad,
            "str_direccion" : pension.str_direccion,
            "str_cp" : pension.str_cp,
            "str_tipo" : pension.str_tipo,
            "str_telefonoCasa" : pension.str_telefonoCasa,
            "str_telefonoCelular" : pension.str_telefonoCelular,
            "str_email" : pension.str_email,
            
            "str_luz" : pension.str_luz,
            "str_internet" : pension.str_internet,
            "str_cable" : pension.str_cable,
            "str_telefono" : pension.str_telefono,
            "str_lavanderia" : pension.str_lavanderia,
            "str_comidas" : pension.str_comidas,
            "str_aguaCaliente" : pension.str_aguaCaliente,
            "str_amueblado" : pension.str_amueblado,
            "str_limpieza" : pension.str_limpieza
    	}

        #Imprimimos el objeto en json
    	self.response.out.write(json.dumps(qanek))

    #Cerramos el arreglo de objetos con el corchete
    self.response.out.write("]")
    

application = webapp2.WSGIApplication([('/getLugaresREST', getLugaresREST)], debug=True)