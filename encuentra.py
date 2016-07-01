import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))


class encuentra(webapp2.RequestHandler):
  def get(self):
    #Solo mostramos las pensiones que esten activas
    ciudadBuscar = self.request.get('ciudad')
    template = template_env.get_template('encuentra.html')
    context = {
    	'ciudad': ciudadBuscar
    }
    self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/encuentra', encuentra)], debug=True)