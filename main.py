# coding=utf-8
# --auth--=Archie
# todo='need this program to check if the exist file is alright'
import urllib2
import urllib
import cookielib
import re
import pickle
import os
from time import *

ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
url = 'http://zccx.tyb.njupt.edu.cn'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
req = urllib2.urlopen(url)

for index,cookie in enumerate(cj):
    ck = re.findall('AT=(.*?)"', cookie.value)
    # print cookie
# print ck

url += '/student'

post_list = {}
exist = False
try:
    f = open('data.dat','rb+')
    exist = True
except IOError:
    f = open('data.dat','wb')
select = 0
if exist:
    select = int(raw_input('do you want to query the lastest user\'s status? (press 1 to use,0 to use others)'))

if select is 0 or not exist :
    name = raw_input('请输入姓名(input your name):'.decode('utf-8'))
    # Because in Windows OS,the input function return a gbk code
    name = name.decode('gbk')
    name = name.encode('utf-8')

    number = raw_input('请输入学号(input your number):'.decode('utf-8'))
    post_list = {
        'authenticityToken': ck[0],
        'name': name,
        'number': number
    }
else:
        post_list = pickle.load(f)

sleep(1)
req = urllib2.urlopen(url,data=urllib.urlencode(post_list))
content = req.read()


os.system('cls')
# print content
result = re.findall('>([0-9]+)</',content)

try:
    if select is 1:
        for name in post_list:
            print name, ':', post_list[name].decode('utf-8')
    print '跑操次数(run times):'.decode('UTF-8'), result[0]
except IndexError:
    print '你输错了( error for you provided a wrong user info)'.decode('utf-8')
else:
    if select == 0:
        pickle.dump(post_list, f)
f.close()
os.system('pause')
