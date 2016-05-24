from google.appengine.ext import db
from google.appengine.ext import blobstore

class Usuario(db.Model):
    str_email = db.StringProperty()
    str_password = db.StringProperty()

class Lugar(db.Model):
    str_urlFotoPerfil = db.StringProperty(default = "0")
    str_nombrePension = db.StringProperty(required=True)
    str_descripcion = db.StringProperty(required=True)
    
    str_nombreArrendador = db.StringProperty(required=True)
    str_ciudad = db.StringProperty(required=True)
    str_direccion = db.StringProperty(required=True)
    int_cp = db.IntegerProperty(required=True)



    int_telefonoCasa = db.IntegerProperty(required=True)
    int_telefonoCelular = db.IntegerProperty(required=True)
    
    str_urlFotos = db.StringProperty()

class UserUpload(db.Model):
    blob = blobstore.BlobReferenceProperty()
