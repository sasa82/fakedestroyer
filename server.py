import random
import string

import cherrypy
import os



class FakeDestroyer(object):
	@cherrypy.expose
	def index(self, platform=''):
		path = os.path.abspath("fakedestroyer-front/index.html")
		return open(path)
				
#	@cherrypy.expose
#	def generate(self, length=8):
#		return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
	cherrypy.quickstart(FakeDestroyer())
