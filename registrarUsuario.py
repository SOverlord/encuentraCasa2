import webapp2
from google.appengine.api import mail
import models
import jinja2
import os
import datetime

from google.appengine.ext import db

class registrarUsuario(webapp2.RequestHandler):
    def post(self):
        #Recuperamos la informacion del HTML y la almacenamos en variables locales
        nombre = self.request.get('str_nombre')
        apellidos = self.request.get('str_apellidos')
        email = self.request.get('str_email')
        contrasena = self.request.get('str_password')
        
        #Almacenamos el contenido de las variables locales en la base de datos
        usuario = models.Usuario()	
        usuario.int_nuevo = 0
        usuario.str_nombre = nombre
        usuario.str_apellidos = apellidos
        usuario.str_email = email
        usuario.str_password = contrasena
        usuario.str_urlFotoPerfil = "0" #significa que no tiene imagen
        #colocamos esas variables en el objeto usuario
        usuario.put()

        #si no metio un correo valido muestra un mensaje un mensaje
        if not mail.is_email_valid(email):
            self.response.out.write("El correo electronico es invalido")
            #enviamos un correo para informarle de su registro
        else:
            sender_address = "sc210594@gmail.com"
            email = usuario.str_email
            subject = "Bienvenido a Encuentra Casa"
            body = """Gracias por registrarte en el mejor sitio para encontrar tu casa, departamento o pension ideal. Tu nombre usuario es %s y tu contrasena es %s""" %(email, contrasena) 
            mail.send_mail(sender_address, email, subject, body)
            
            #Despues de haber registrado nos dirigimos al controler de crearSesion (dentro de este se redireccionara a configuracion)
            self.redirect("/crearSesion?user=" + email + "&py=registrar")
	
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/registrarUsuario', registrarUsuario)],debug=True)
