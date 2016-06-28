import datetime
import jinja2
import os
import webapp2
import models

from webapp2_extras import json
from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))


class MainPage(webapp2.RequestHandler):
  def get(self):
    #Solo mostramos las pensiones que esten activas
    self.response.content_type = 'application/json'
    showPensiones = db.Query(models.Lugar).filter("int_publicarPension", 1)
    self.response.write(json.encode(showPensiones))
    

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)