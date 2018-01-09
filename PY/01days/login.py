#-*-coding:utf-8-*-
import getpass
File = open('userinfo','r+')
UserInfo = File.readlines()
File.close()
User = eval(UserInfo[0])
Count = 0
while Count <3:
    username = input('username:')
    if username in User.keys():
        while Count <3:
            pwd = getpass.getpass('password:')
            if pwd == User.get(username):
                print('欢迎%s登录' % username)
                break
            else:
                Count+=1
                if Count == 3:
                    print('密码输入错误超过3次，账号已经被锁定。请联系管理员进行解锁')
                else:
                    print('密码错误请重新输入')
    else:
        print('用户名不存在，请重新输入')
        Count+=1
        if Count == 3:
            print('输入错误超过3次，退出程序')