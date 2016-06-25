from google.appengine.ext import db
from google.appengine.ext import blobstore

class Usuario(db.Model):
    str_email = db.StringProperty()
    str_password = db.StringProperty()

query = db.Query(Usuario)
if query.count() == 0:
    newUsr = Usuario(str_email="def@def.com", str_password="1")
    print("Nuevo usuario agregado")
    newUsr.put()

class Lugar(db.Model):
    #int_LugarID = ID autogenerado por GAE
    int_rentaMensual = db.IntegerProperty()
    str_fechaRegistro = db.StringProperty()
    int_fechaRegistro = db.IntegerProperty()
    int_publicarPension = db.IntegerProperty(default=0)
    str_urlFotoPerfil = db.StringProperty(default = "0")
    str_nombrePension = db.StringProperty()
    txt_descripcion = db.TextProperty()
    str_nombreArrendador = db.StringProperty()
    str_tipoLugar = db.StringProperty()
    str_ciudad = db.StringProperty()
    str_direccion = db.StringProperty()
    str_cp = db.StringProperty()
    str_tipo = db.StringProperty()
    str_telefonoCasa = db.StringProperty()
    str_telefonoCelular = db.StringProperty()
    str_email = db.StringProperty()

    str_luz = db.StringProperty(default="False")
    str_internet = db.StringProperty(default="False")
    str_cable = db.StringProperty(default="False")
    str_telefono = db.StringProperty(default="False")
    str_lavanderia = db.StringProperty(default="False")
    str_comidas = db.StringProperty(default="False")
    str_aguaCaliente = db.StringProperty(default="False")
    str_amueblado = db.StringProperty(default="False")
    str_limpieza = db.StringProperty(default="False")

class UserUpload(db.Model):
    blob = blobstore.BlobReferenceProperty()

class CarreteFotos(db.Model):
    str_LugarID = db.StringProperty()
    str_urlFoto = db.StringProperty()