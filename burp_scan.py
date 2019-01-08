#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import importlib
import time
import conf.config as config
import module.parse_burp_log as parse
import module.output as show
poc_module=config.poc_module
logfile_name=config.logfile_name


#load poc moudle
poc_modules=[]
for poc in poc_module:
    try:
        poc_modules.append(importlib.import_module(poc))
        print("[!]"+poc+" load success")
    except Exception as e:
        print(e)
        print("poc_module don't exist")
if __name__ == '__main__':
    while 1:
        log_num = 0
        data_log = parse.parse_log(logfile_name)
        if data_log != 0:
            for poc_module in poc_modules:
                poc_module.index(data_log, log_num)
        time.sleep(2)