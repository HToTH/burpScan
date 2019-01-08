#!/usr/bin/python
# _*_ coding:utf-8 _*_
import json
import cgi
import sys
import codecs
import os
def exportAsJSON(itemlist,filename):
    newitemlist = []
    for item in itemlist:
        newitemlist.append({'time':item['time'],
            'protocol':item['protocol'],#0
            'hostname':item['hostname'],#1
            'port':item['port'],#2
            'hostip':item['hostip'],#3
            'req_headers':item['request']['headers'],#4
            'req_body':item['request']['body'],#5
            'req_command':item['request']['command'],#6
            'req_path':item['request']['path'],#7
            'resp_headers':item['response']['headers'],#8
            'resp_body':item['response']['body'],#9
            'resp_status':item['response']['status'],#10
            'resp_reason':item['response']['reason']})#11
    outderdict = {'data':newitemlist}
    f = open(filename, 'w')
    f.write(json.dumps(outderdict,sort_keys=True,indent=4, separators=(',', ': ')))
    f.close()

def exportAsArray(itemlist):
    newitemlist = []
    for item in itemlist:
        newitemlist.append([item['time'],
            item['protocol'],
            item['hostname'],
            item['hostip'],
            item['port'],
            item['request']['command'],
            item['request']['path'],
            item['response']['status'],
            item['response']['reason'],
            item['request']['headers'],
            item['request']['body'],
            item['response']['headers'],
            item['response']['body']])
    for rowid,row in enumerate(newitemlist):
        for colid,col in enumerate(row):
            if col == None:
                newitemlist[rowid][colid]=''
    return newitemlist

def parseRequest(req):
    request = None
    try:
        splitreq = req.split('\n\n',1)
        firstline = splitreq[0].split('\n')[0]
        command = firstline.split(' ')[0]
        path =firstline.split(' ')[1]
        version = firstline.split(' ')[2]
        headers = splitreq[0].strip()
        body = None
        if len(splitreq[1].strip())!=0: #is there a request body?
            body = cgi.escape(splitreq[1].strip())
        request = {'command':command,'path':path,'version':version,'headers':headers,'body':body}
    except:
        request = {'command':None,'path':None,'version':None,'headers':None,'body':None}
    return request


def parseResponse(resp):
    response = None
    try:
        splitresp = resp.split('\n\n',1)
        firstline = splitresp[0].split('\n')[0]
        version = firstline.split(' ')[0]
        status =firstline.split(' ')[1]
        reason = firstline.split(' ')[2]
        headers = splitresp[0].strip()
        body = None
        if len(splitresp[1].strip())!=0: #is there a body?
            body = cgi.escape(splitresp[1].strip())
        response = {'version':version,'status':status,'reason':reason,'headers':headers,'body':body}
    except:
        response = {'version':None,'status':None,'reason':None,'headers':None,'body':None}
    return response
#清空文件
def clean(logfile_name):
    f = open(logfile_name, "r+")
    f.truncate()
    f.close()

def parse_log(logfile_name):
    fsize = os.path.getsize(logfile_name)
    if fsize < 1:
        return 0
    try:
        with open(logfile_name, mode= "r",encoding='unicode_escape') as f:
            logfile = f.read()
        f.close()
        clean(logfile_name)
    except Exception as e:
        print(e)
        clean(logfile_name)
        return 0

    logfile=str(logfile)+"\n\n======================================================\n"
    if "======================================================" in logfile.split('\n')[0]: #hacky bit to move first line
        lf2 = '\n'.join(logfile.split('\n')[1:])
        logfile = lf2

    pairsep = "======================================================\n\n\n\n======================================================\n"
    pairs = []
    for item in logfile.split(pairsep):
        hostinfo = item.split('\n')[0].split('  ')
        try:
            time = cgi.escape(hostinfo[0])
        except:
            time = None
        try:
            protocol = cgi.escape(hostinfo[1].rsplit(':',1)[0].split('://')[0])
        except:
            protocol = None
        try:
            hostname = cgi.escape(hostinfo[1].rsplit(':',1)[0].split('://')[1])
        except:
            hostname = None
        try:
            port = cgi.escape(hostinfo[1].rsplit(':',1)[1])
        except:
            port = None
        try:
            hostiptmp = hostinfo[2]
            hostip = cgi.escape(hostiptmp[1:-1])
        except:
            hostip = None

        if "======================================================\nHTTP" in item:#is there a response?
            #there is a response
            req = item.split("======================================================\n")[1]
            resp = item.split("======================================================\n")[2]
        else:
            #there isn't a response

            req = item.split("======================================================\n")[1]
            resp = None
        pairs.append({'time':time,'protocol':protocol,'hostname':hostname,'port':port,'hostip':hostip,'request':parseRequest(req),'response':parseResponse(resp)})
    return   pairs
