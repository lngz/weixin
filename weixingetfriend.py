# -*- encoding: utf-8 -*-


from wechat import wechat
import password


if __name__ == '__main__':
    w = wechat()
    username = password.username
    password = password.password
    w.login(username,password)
    w.getfriend()
    print w.friends['contacts']
    # for info in w.friends['contacts']:
    #       w.sendmsg( str(info['id']), info['nick_name'])

    for info in w.friends['contacts']:
        print info['id'], info['nick_name']

