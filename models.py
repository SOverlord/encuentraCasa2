from google.appengine.ext import db
from google.appengine.ext import blobstore

class Usuario(db.Model):
    str_email = db.StringProperty()
    str_password = db.StringProperty()
#Agregar un usuario predeterminado


class Lugar(db.Model):
    #int_LugarID = ID autogenerado por GAE
    int_publicarPension = db.IntegerProperty(default=0)
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

class UserUpload(db.Model):
    int_LugarKey = db.IntegerProperty(default=0)
    blob = blobstore.BlobReferenceProperty()
