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
		findcard(data_log[i])
def judgeCard(idcard,notidcard):
    for i in notidcard:
        if idcard in i:
            return False
def findcard(data_log):
    if data_log['response']['body']!=None:
        idcardre = r'[1-9]\d{5}[1-3]\d{3}[0-1][0-9][0-3]\d{4}[0-9Xx]' #身份证号
        idcardreb = r'[0-9][1-9]\d{5}[1-3]\d{3}[0-1][0-9][0-3]\d{4}[0-9Xx]' #身份证前
        idcardrea = r'[1-9]\d{5}[1-3]\d{3}[0-1][0-9][0-3]\d{4}[0-9Xx][0-9]' #身份证后
        res = re.findall(idcardre,data_log['response']['body'])
        idtmpb = re.findall(idcardreb,data_log['response']['body'])
        idtmpa = re.findall(idcardrea,data_log['response']['body'])
        for card in res:
            if judgeCard(card,idtmpb)!=False and judgeCard(card,idtmpa)!=False:
                show.output(data_log,"页面发现身份证号"+card,crayons.cyan)
