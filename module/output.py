#!/usr/bin/python
# -*- coding: utf-8 -*-
import html.parser
import crayons
import colorama
import re
h = html.parser.HTMLParser()
line="-----------------------------------------------------------------------"

def output(data_log,poc_result,color):
	colorama.init()  #输的色彩
	p1 = r'Referer:(.*?)\n'
	referer = re.findall(p1,data_log['request']['headers'])
	if len(referer)>0:
		referer = referer[0]
	else:
		referer = '无'
	if data_log["request"]["body"]!=None:
		data_log["request"]["body"]=h.unescape(data_log["request"]["body"])
	if data_log["request"]["command"]=="POST":

		print(color(line))
		print(color("域名:  "+data_log["hostname"]+"   端口:  "+str(data_log['port'])+"   请求方式:  "+data_log["request"]["command"]))
		print(color("漏洞地址:  "+data_log['protocol']+"://"+data_log["hostname"]+h.unescape(data_log["request"]["path"])))
		print(color("post value:  "+str(data_log["request"]["body"])))
		print(color("页面来源: " + referer))
		print(color("描述:  "+poc_result))
		print(color(line))
	else:
		print(color(line))
		print(color("域名:  "+data_log["hostname"]+"   端口:  "+str(data_log['port'])+"   请求方式:  "+data_log["request"]["command"]))
		print(color("漏洞地址:  "+data_log['protocol']+"://"+data_log["hostname"]+h.unescape(data_log["request"]["path"])))
		print(color("页面来源: " + referer))
		print(color("描述:  "+poc_result))
		print(color(line))
