import random
import string

import cherrypy
import os
from Cheetah.Template import Template


cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 80})
css_path = os.path.abspath("fakedestroyer-front/assets/style/style.css")


class FakeDestroyer(object):
	@cherrypy.expose
	def index(self, platform=''):
		templ_path = os.path.abspath("fakedestroyer-front/index.html")
		html_template = Template(file=templ_path)
		html_template.css_scripts=[css_path]
		return str(html_template)
		#return open(path)
		
	@cherrypy.expose
	def check(self):
		path = os.path.abspath("fakedestroyer-front/check.html")
		return open(path)
		
	@cherrypy.expose
	def about(self):
		path = os.path.abspath("fakedestroyer-front/about.html")
		return open(path)
				
	@cherrypy.expose
	def api_check(self):
		print("inside api request")


if __name__ == '__main__':
	cherrypy.quickstart(FakeDestroyer())
