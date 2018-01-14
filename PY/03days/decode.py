#-*-coding:utf-8-*-
import time
def deco(Auth_type):
    #print(Auth_type)
    def warpper(func):
        def hi(*args,**kwargs):
            if Auth_type == 'local':
                start_time = time.time()
                res = func(*args,**kwargs)
                end_time = time.time() - start_time
                print('program runtime is %s' %end_time)
                return res
            else:
                print('shit')
        return hi
    return warpper
@deco(Auth_type = 'ladp')
def hello():
    time.sleep(3)
    print('hello world')
@deco(Auth_type = 'local')
def world(name):
    time.sleep(2)
    print('%s welcome to chian' % name)
hello()
world('alan')
