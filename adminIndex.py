import webapp2
from webapp2_extras import sessions
import session_module
import jinja2
import os
import models
from google.appengine.ext import db

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
#recibimos el sesion_module
class adminIndex(session_module.BaseSessionHandler):
    def get(self): 
        #si se intenta crear una sesion y ya existe la variable de una sesion solo imprimimos cual es el usuario de la sesion
        if self.session.get('usuario'):
            query = db.Query(models.Lugar)
            template = template_env.get_template('admin/adminIndex.html')
            try:
                idPens = int(self.request.get('idP'))   #Obtenemos ID de URL
                stat = self.request.get('status')
            except:
                print "No hay nada que actualizar"
            else:
                pension = models.Lugar.get_by_id(idPens)        #Buscamos la ID en la BD
                print "Actualizando pension: "+str(idPens)
                if stat == '1':
                    pension.int_publicarPension = 1
                    print "->1"
                if stat == '0':
                    pension.int_publicarPension = 0
                    print "->0"
                pension.put()
                self.redirect("/adminIndex")
            context = {
            	'query': query,
                'usr': self.session.get('usuario')
            }
            self.response.out.write(template.render(context))
        #si no existia, creamos la sesion
        else:
            self.redirect("/")
#End of MainHandler Class
#nombre del controlador, clase a la que pertenece, lo de la sesion y el debug
application = webapp2.WSGIApplication([('/adminIndex', adminIndex),], config = session_module.myconfig_dict, debug=True)