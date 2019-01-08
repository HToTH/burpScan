#!/usr/bin/python
# -*- coding: utf-8 -*-
#接口返回手机号的信息
import conf.config as config
import module.output as show
import crayons
import colorama
import re
def index(data_log,log_num):#entrance function
	for i in range(log_num,len(data_log)):
		findmobile(data_log[i])
def judgeMobile(mobile,notmobile):
    for i in notmobile:
        if mobile in i:
            return False
def findmobile(data_log):
    if data_log['response']['body']!=None:
        mobilere = "[1][3,4,5,7,8][0-9]{9}" #正常手机号
        notmobilere = "[1][3,4,5,7,8][0-9]{10}" #手机号后面有没有数字
        beforemobiere = "[0-9][1][3,4,5,7,8][0-9]{9}" #手机号前面有没有数字
        res = re.findall(mobilere,data_log['response']['body'])
        tmp = re.findall(notmobilere,data_log['response']['body'])
        beforetmp = re.findall(beforemobiere,data_log['response']['body'])
        for mobile in res:
            if  judgeMobile(mobile,tmp)!=False and judgeMobile(mobile,beforetmp)!=False:
                if len(mobile) == 11:
                    show.output(data_log,"页面发现手机号"+mobile,crayons.cyan)
                    return 1