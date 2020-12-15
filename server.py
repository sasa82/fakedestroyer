import hashlib 
import random
import string
2801
import cherrypy
import os
from Cheetah.Template import Template
import json
import mysql.connector
import pymorphy2
import re



def First(tringg):
    stringg = ''.join(tringg)
    string_low = stringg.lower()
    s = re.sub(r"\d+", "", string_low, flags=re.UNICODE)
    table = str.maketrans({key: None for key in string.punctuation})
    string_nv = s.translate(table)
    array = string_nv.split()
    return array


def Normal_form(array):
    list = []
    i = 0
    count_arr = len(array)
    while i < count_arr:
        morph = pymorphy2.MorphAnalyzer(lang='uk')
        chose = morph.parse(array[i])[0]
        comfortable = chose.normal_form
        i += 1
        list.append(comfortable)
    return list


def normal_length(lists):
    list = []
    i = 0
    while i < (len(lists)):
        if len(lists[i]) > 3:
            comfortable = str(lists[i])
            list.append(comfortable)
            i = i + 1
        elif len(lists[i]) < 4:
            i = i + 1
    return list


def Form_hash(array):
    list = []
    i = 0
    len_hash = len(array) - 4
    while i < len_hash:
        h1 = str(array[i])
        h2 = str(array[i + 1])
        h3 = str(array[i + 2])
        h4 = str(array[i + 3])
        h5 = str(array[i + 4])
        five_wo = h1 + h2 + h3 + h4 + h5
        two_bites = str.encode(five_wo, encoding='utf-8')
        sha_hash = hashlib.sha1(two_bites)
        f_hash = sha_hash.hexdigest()
        i = i + 1
        list.append(f_hash)
    return list


def Compare(strr, str1):
    t = len(strr)
    d = len(str1)
    b = 0
    for i in range(t):
        k = strr[i]
        print("k = ", k)
        for j in range(d):
            p = str1[j]
            print("p = ", p)
            if k == p:
                b = b + 1
            else:
                b = b + 0
    if b >= (((t + d) / 2) / 100) * 60:
        sign = 2
    else:
        sign = 0
    return sign


def out(str1, str2):
    fed = First(str2)
    dd = Normal_form(fed)
    ddf = normal_length(dd)
    d1 = Form_hash(ddf)
    print(d1)
    for i in range(len(str1)):
        fk = str1[i][1]
        array = fk.split()
        #print(fk)
        #slt = First(fk)
        #st = Normal_form(slt)
        #rt = normal_length(st)
        #rtr = Form_hash(rt)
        #print(rtr)
        c = Compare(d1, array)
        if c > 1:
            fs = str1[i][2]
            print(fs)
            break
        else:
            fs = None
    return fs



def fetch_items(data):
	print("inside fetch items")
	connection = mysql.connector.connect(host="127.0.0.1", user="root", passwd="root", db="fakedestroyers", charset='utf8')
	cursor = connection.cursor(buffered=True)
	cursor.execute("SET NAMES 'utf8';")
	cursor.execute("SET CHARACTER SET 'utf8';")
	fetch_query = ("SELECT * FROM enntries")
	cursor.execute(fetch_query)
	result = cursor.fetchall()
	cursor.close()
	connection.close()
	return result

	
	
def perform_calculations(result, data):
	print("inside perform calculations")
    #сравнение запроса с текстом из базы данных
	reference = out(result,data)


	#perform calculations here
    
	return reference

def generate_response(data):
	print("inside generate response")
	response = {'reference' : None, 'error': None, 'data': None}
	try:
		result = fetch_items(data)
		print("result items")
		print(result)
		response['data'] = result # to remove in production mode
		
		
		
		calc_result = perform_calculations(result, data)
		response['reference'] = calc_result
		
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
