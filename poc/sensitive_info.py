#!/usr/bin/python
# -*- coding: utf-8 -*-
import conf.config as config
import module.output as show
import crayons
import colorama
def index(data_log,log_num):#entrance function
	for i in range(log_num,len(data_log)):
		check_sensitive_info(data_log[i])
def check_sensitive_info(data_log):
	for i in config.sensitive_info:
		if data_log['response']['body']!=None:
			if data_log['response']['body'].find(i)>-1:
				show.output(data_log,"页面存在敏感信息:"+i,crayons.white)
				continue