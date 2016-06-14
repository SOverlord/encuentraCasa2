import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.api import users

template_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.getcwd()))

class adminLogin(webapp2.RequestHandler):
  def get(self):
    template = template_env.get_template('admin/adminLogin.html')
    context = {}
    self.response.out.write(template.render(context))
    
application = webapp2.WSGIApplication([('/adminLogin', adminLogin)], debug=True)