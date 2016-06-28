import jinja2
import os
import webapp2
import models
import datetime
from webapp2_extras import sessions
import session_module
from google.appengine.api import users

template_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.getcwd()))

class adminLogin(session_module.BaseSessionHandler, webapp2.RequestHandler):
	def get(self):
		if self.session.get('usuario'):
			self.redirect("/adminIndex")
		else:
			template = template_env.get_template('admin/adminLogin.html')
			context = {}
			self.response.out.write(template.render(context))
    
application = webapp2.WSGIApplication([('/adminLogin', adminLogin)], config = session_module.myconfig_dict, debug=True)