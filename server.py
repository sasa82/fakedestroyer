import random
import string

import cherrypy
import os


cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 80})

class FakeDestroyer(object):
	@cherrypy.expose
	def index(self, platform=''):
		path = os.path.abspath("fakedestroyer-front/index.html")
		return open(path)
		
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
