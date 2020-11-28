import random
import string

import cherrypy
import os
from Cheetah.Template import Template
import json
import mysql.connector


def fetch_items(data):
	print("inside fetch items")
	connection = mysql.connector.connect(host="127.0.0.1", user="root", passwd="root", db="fakedestroyers", charset='utf8')
	cursor = connection.cursor(buffered=True)
	cursor.execute("SET NAMES 'utf8';")
	cursor.execute("SET CHARACTER SET 'utf8';")
	fetch_query = ("SELECT * FROM entries")
	cursor.execute(fetch_query)
	result = cursor.fetchall()
	cursor.close()
	connection.close()
	return result
	
	
def perform_calculations(result):
	print("perform all calcs here!!!!!")


def generate_response(data):
	print("inside generate response")
	response = {'exists' : False, 'error': None, 'data': None}
	try:
		result = fetch_items(data)
		print("result items")
		print(result)
		response['data'] = result # to remove in production mode
		
		
		calc_result = perform_calculations(result)
		
	except Exception as e:
		response['error'] = str(e)
	
	
	
	return response
	

class FakeDestroyer(object):
	@cherrypy.expose
	def index(self, platform=''):
		html_template = Template(file='templates/index.html')
		html_template.css_scripts=['static/style/style.css']
		return str(html_template)
		
	@cherrypy.expose
	def check(self):
		html_template = Template(file='templates/check.html')
		html_template.css_scripts=['static/style/style.css']
		return str(html_template)
		
	@cherrypy.expose
	def about(self):
		html_template = Template(file='templates/about.html')
		html_template.css_scripts=['static/style/style.css']
		return str(html_template)
				
	@cherrypy.expose
	def api(self, data):
		response = generate_response(data)
		return json.dumps(response)




current_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
config = {
'global': {
	'environment': 'production',
	'log.screen': True,
	'server.socket_host': '0.0.0.0',
	'server.socket_port': 80,
	'engine.autoreload_on': True,
	'log.error_file': os.path.join(current_dir, 'errors.log'),
	'log.access_file': os.path.join(current_dir, 'access.log'),
	},
	'/':{
	'tools.staticdir.root' : current_dir,
	},
	'/static':{
	'tools.staticdir.on' : True,
	'tools.staticdir.dir' : 'static',
	},
}


if __name__ == '__main__':
	cherrypy.quickstart(FakeDestroyer(), '/', config)
