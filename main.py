import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.api import users

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))


class MainPage(webapp2.RequestHandler):
  def get(self):
     
      template = template_env.get_template('index.html')
      context = {
       'errors' : ''
      }
      self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)