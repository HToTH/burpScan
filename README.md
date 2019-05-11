# burpScan

#### 介绍
burp被动扫描

#### 业务场景
渗透测试中容易忽略的接口信息检查。


#### 使用说明

1. 打开burpsuite记录日志project option-->misc-->logging->proxy

![配置图片]https://github.com/HToTH/burpScan/blob/master/image.png
2. 在/conf/config.py里面配置敏感信息
3. 在poc里面增加插件
4. python版本>=python3.0
