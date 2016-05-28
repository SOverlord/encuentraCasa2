import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.ext import db

template_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.getcwd()))


class MainPage(webapp2.RequestHandler):
  def get(self):
    showPensiones = db.Query(models.Lugar)
    template = template_env.get_template('index.html')
    context = {
    	'showPensiones': showPensiones
    }
    self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)

  	
