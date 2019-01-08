#!/usr/bin/python
# -*- coding: utf-8 -*-
import module.output as show
import crayons
import colorama
import re
def index(data_log,log_num):#entrance function
	for i in range(log_num,len(data_log)):
		SecureSymbol(data_log[i])
def SecureSymbol(data_log):
	if data_log['protocol'] != 'https':
		p1 = r'Referer:(.*?)\n'
		referer = re.findall(p1, data_log['request']['headers'])
		if len(referer) > 0:
			referer = referer[0]
		else:
			referer = '0'
		f= open('poc/tmp/Http_secure_symbol_tmp.txt','r+')  # 避免多余的输出，并记录http没有标记的网页
		referers = f.readlines()
		if referer+"\n" not in referers :
			try:
				f.write(referer+"\n")
			except:
				pass
			show.output(data_log, "页面来源没有浏览器标记的安全小锁",crayons.red)
		f.close()

