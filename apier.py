import requests

class apier:
	def setmethod(o, method):
		o.method=method

	def execute(o):
		o.r=requests.request(url=o.url, method=o.method, params=o.params, headers=o.heads)
		o.res=o.r.content
		o.status=o.r.status_code

	def addparams(o, param):
		for k in param:
			o.params[k]=param[k]
	def addheads(o, head):
		for k in head:
				o.heads[k]=head[k]

	def seturl(o, url):
		o.url=url

	def __init__(o):
		o.url=""
		o.params={}
		o.heads={}
		o.method="GET"
		o.status=0
