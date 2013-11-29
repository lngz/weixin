
#!/usr/bin/python
# -*-  coding: UTF-8 -*-

from wechat import wechat
import password 


if __name__ == '__main__':
    w = wechat()
    username = password.username
    password = password.password
    w.login(username,password)
    #w.sendmsg('2377600462',"hello weixin")
    w.getfriend()

    for info in w.friends['contacts']:
        print info['id'], info['nick_name']

    touser = raw_input("input user id:")
    textmsg = raw_input("input text message:")
    print w.sendmsg(touser, textmsg)

    # for info in w.friends['contacts']:
    #       w.sendmsg( str(info['id']), info['nick_name'])
