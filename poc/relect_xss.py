#!/usr/bin/python
# -*- coding: utf-8 -*-
import module.output as show
import requests
import html.parser
import conf.config as config
import crayons
import colorama


h = html.parser.HTMLParser()
def index(data_log,log_num):#entrance function 
	for i in range(log_num,len(data_log)):
		check_relect_xss(data_log[i])
def check_relect_xss(data_log):
	try:
		if data_log["response"]["headers"].find("text/html") >-1 and data_log["response"]["body"].find("!DOCTYPE")==-1 and data_log["response"]["body"]!="None" and data_log["request"]["command"]=="GET":
			check_relect_xss_step_2(data_log)		
	except:
		pass
def check_relect_xss_step_2(data_log):
	
	header_data=data_log["request"]["headers"].split("\n")
	headers={}
	for i in range(1,len(header_data)-1):
		key=header_data[i].split(": ")[0]
		value=header_data[i].split(": ")[1]
		headers[key]=value
	url_path=h.unescape(data_log["request"]["path"])
	if url_path==None:
		url_path=""
	if url_path.split("p")[0]=="htt":#judge Url_path is path or url path
		url=url_path
	else:
		url=data_log['protocol']+"://"+data_log['hostname']+url_path

	if h.unescape(data_log["request"]["path"]).find("?")>-1:
		keyworlds={'&jsonpcallback=<95272333>','&jsoncallback=<95272333>','&callback=<95272333>'}
	else:
		keyworlds={'?jsonpcallback=<95272333>','?jsoncallback=<95272333>','?callback=<95272333>'}
	check_domain=0
	for keyworld in keyworlds:
		try:
			if data_log['hostname'].split(".")[-2] in config.use_proxy_domain:
				check_domain=1
			if config.proxy_value==1 and check_domain==1:
				r=requests.get(url+keyworld,headers=headers,proxies=config.proxies, timeout=2)
			else:
				r=requests.get(url+keyworld,headers=headers, timeout=2)
			html=r.text
			if len(html)!=0:
				if html.find("<95272333>") >-1:
					show.output(data_log,"存在反射型xss,poc:"+keyworld,crayons.yellow)
		except Exception as e:
			pass
			#print(e)
		
