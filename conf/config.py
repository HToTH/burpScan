#config
#burp日志
logfile_name="request_log.txt"
#加载模块
poc_module=['poc.sensitive_info','poc.relect_xss',"poc.findmobile","poc.findIdCard"]
#poc_module=['poc.relect_xss']
#--------------------------------------------------------------------------#
#敏感信息设置
sensitive_info=['暂不使用该功能']

'''循环输出查找的敏感信息'''
print("************敏感信息************")
for i in  sensitive_info:
	print("************"+i+"************")
#--------------------------------------------------------------------------#
#proxy 代理设置
proxies = {
  "http": "http://10.200.70.143:33128",
  "https": "http://10.200.70.143:33128",
}
proxy_value=0 #1  use proxy ,0 don't use proxy
'''显示在terminal'''
if proxy_value==0:
	print("************未使用代理************")
else:
	print("************使用代理************")
use_proxy_domain=['']#配置使用代理访问的域名
#--------------------------------------------------------------------------#
