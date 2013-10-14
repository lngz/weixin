
# -*- encoding: utf-8 -*-

import cookielib, urllib2
import urllib
import json
import hashlib
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

DEBUG = False

class wechat :

	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'), ]
	opener.addheaders += [('Referer', 'https://mp.weixin.qq.com/'), ]

	Token = ""

	def login(self, username, password) :
		values = {'username' : username,
				'pwd' : hashlib.md5(password).hexdigest(),
				'imgcode': '',
				'f' : 'json' }
		data = urllib.urlencode(values)
		try:
			search = self.opener.open('https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN',data)
			logined = search.read()
			loginmsg = json.loads(logined)
			if loginmsg['ErrCode'] != 0 :
				raise
		except :
			print "login failed"
			return
		
		if DEBUG :
			print values
			print logined
			print self.cj
		
		self.Token = loginmsg['ErrMsg'].split('&')[2].split('=')[1]

		if DEBUG :
			print self.Token
		search = self.opener.open('https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=' + self.Token)

	def loginMD5(self, username, password) :
		values = {'username' : username,
				'pwd' : password,
				'imgcode': '',
				'f' : 'json' }
		data = urllib.urlencode(values)
		try:
			search = self.opener.open('https://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN',data)
			logined = search.read()
			loginmsg = json.loads(logined)
			if loginmsg['ErrCode'] != 0 :
				raise
		except :
			print "login failed"
			return
		
		if DEBUG :
			print values
			print logined
			print self.cj
		
		self.Token = loginmsg['ErrMsg'].split('&')[2].split('=')[1]

		if DEBUG :
			print self.Token
		search = self.opener.open('https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=' + self.Token)


	def sendmsg(self,fakeid,textmsg) :
		
		values = {
		        'mask':'false',
		    'tofakeid':fakeid,
		    'imgcode':'',
		    'type':'1',
		    'content':textmsg,
		    'quickreplyid':'201',
		    'token':self.Token,
		    'lang':'zh_CN',
		    't':'ajax-response'
		}
		data = urllib.urlencode(values)

		self.opener.addheaders [1] = ('Referer', 'https://mp.weixin.qq.com/cgi-bin/singlemsgpage?msgid=&source=&count=20&t=wxm-singlechat&fromfakeid='+ fakeid +'&token='+self.Token+'&lang=zh_CN')
		search = self.opener.open('https://mp.weixin.qq.com/cgi-bin/singlesend?t=ajax-response&lang=zh_CN',data)

		return search.read()


	def getfriend(self) :
		

		search = self.opener.open('https://mp.weixin.qq.com/cgi-bin/contactmanage?t=user/index&pagesize=1000&pageidx=0&type=0&groupid=0&token=' + self.Token + '&lang=zh_CN')
		#print search.read()

		#print cj
		for html in search.readlines():
		    m = re.match('\s*friendsList.*\((.*)\).*',html)
		    if m :
		        friendsList = m.group(1) 


		self.friends = json.loads(friendsList)

		




if __name__ == '__main__':
	w = wechat()
	username = raw_input("username:")
	password = raw_input("password:")
	w.login(username,password)
	#w.sendmsg('2377600462',"hello weixin")
	w.getfriend()
	print w.friends['contacts']
	# for info in w.friends['contacts']:
	# 	    w.sendmsg( str(info['id']), info['nick_name'])
