
#!/usr/bin/python
# -*-  coding: UTF-8 -*-

from wechat import wechat
import getpass


if __name__ == '__main__':
    w = wechat()
    username = raw_input("username:")
    password = getpass.getpass("password:")
    w.login(username,password)
    #w.sendmsg('2377600462',"hello weixin")
    w.getfriend()
    print w.friends['contacts']
    touser = raw_input("input user id:")
    textmsg = raw_input("input text message:")
    w.sendmsg(touser, textmsg)

    # for info in w.friends['contacts']:
    #       w.sendmsg( str(info['id']), info['nick_name'])
