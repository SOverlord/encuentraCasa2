from google.appengine.ext import db
from google.appengine.ext import blobstore

class Usuario(db.Model):
    str_email = db.StringProperty()
    str_password = db.StringProperty()

class Lugar(db.Model):
    str_urlFotoPerfil = db.StringProperty(default = "0")
    str_nombrePension = db.StringProperty()
    str_descripcion = db.StringProperty()
    str_nombreArrendador = db.StringProperty()
    str_ciudad = db.StringProperty()
    str_direccion = db.StringProperty()
    str_cp = db.StringProperty()
    str_tipo = db.StringProperty()
    str_telefonoCasa = db.StringProperty()
    str_telefonoCelular = db.StringProperty()
    str_urlFotos = db.StringProperty(default="")

class UserUpload(db.Model):
    blob = blobstore.BlobReferenceProperty()
