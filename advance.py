
# -*- encoding: utf-8 -*-
# 微信创建自定义菜单的方法
import urllib
import urllib2
from urllib import urlencode
import json
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import password

appid = password.appid
secret = password.secret


gettoken = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret

f = urllib2.urlopen( gettoken )


stringjson = f.read() 

access_token = json.loads(stringjson)['access_token']

print access_token




posturl = "https://api.weixin.qq.com/cgi-bin/user/get?access_token=" + access_token +"&next_openid="



request = urllib2.urlopen(posturl)

print request.read()
