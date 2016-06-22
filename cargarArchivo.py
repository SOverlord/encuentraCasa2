import jinja2
import os
import webapp2
import models

from webapp2_extras import sessions
import crearSesion
import session_module

from google.appengine.ext import blobstore
from google.appengine.api import users
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import db

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))

class CargarArchivo(session_module.BaseSessionHandler, blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        idP = int(self.request.get('idPens'))    #Obtenemos ID de URL
        #print idPens
        pension = models.Lugar.get_by_id(idP)       #Buscamos la ID en la BD
        #iniciamos esta variable que almacenara el key del objeto blob
        blob_key = ''
        #'upload' es el nombre de la variable html que recibe el archivo
        archivo = self.request.get('file')
        print "Agregando foto"
        for blob_info in self.get_uploads('upload'):
            print archivo
            if archivo == "fotoperfil":
                #almacenamos la key obtenida
                blob_key = blob_info.key()
                #guardamos el archivo en un objeto userupload
                upload = models.UserUpload(blob = blob_key)
                upload.put()
                #buscamos el archivo en la base de datos, objeto userupload
                key_blob = 'x'
                myblob = db.Query(models.UserUpload).filter("blob", key_blob)
                myb = myblob.get()
                key_blob = upload.key()
                print "Es foto de perfil"
                pension.str_urlFotoPerfil = str(key_blob)
                pension.put()
        for blob_info in self.get_uploads('upload2'):
            if archivo == "fotoCarrete":
                #almacenamos la key obtenida
                blob_key = blob_info.key()
                #guardamos el archivo en un objeto userupload
                upload = models.UserUpload(blob = blob_key)
                upload.put()
                #buscamos el archivo en la base de datos, objeto userupload
                key_blob = 'x'
                myblob = db.Query(models.UserUpload).filter("blob", key_blob)
                myb = myblob.get()
                key_blob = upload.key()
                print "Es foto de carrete"
                crt = models.CarreteFotos()
                crt.str_LugarID = str(idP)
                crt.str_urlFoto = str(key_blob)
                crt.put()
        
        self.redirect("/editarPension?idPension="+str(idP))
        
application = webapp2.WSGIApplication([('/cargarArchivo', CargarArchivo)], config = session_module.myconfig_dict, debug=True)