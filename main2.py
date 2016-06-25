import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))


class MainPage(webapp2.RequestHandler):
  def get(self):
    #Solo mostramos las pensiones que esten activas
    showPensiones = db.Query(models.Lugar).filter("int_publicarPension", 1)
    for pension in showPensiones:
    	self.response.out.write(pension.key().id())
    	self.response.out.write(" - "+pension.str_nombrePension)
    	self.response.out.write("<br>")

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)