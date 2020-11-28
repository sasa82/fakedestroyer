import random
import string

import cherrypy
import os


cherrypy.server.socket_host = '0.0.0.0'

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
				
#	@cherrypy.expose
#	def generate(self, length=8):
#		return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
	cherrypy.quickstart(FakeDestroyer())
