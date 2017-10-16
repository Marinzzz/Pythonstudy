#coding=utf-8
import re
with open('1.txt','r') as f:
    a=f.readlines()
for i in a:
    #if(re.match(r'http://\w{1,20}.com/',i)):
    #print i
    if(re.findall(r'https?://[^/]+?/',i)):
        print str(re.findall(r'https?://[^/]+?/',i))

