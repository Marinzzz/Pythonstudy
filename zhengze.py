import re
email=raw_input()
if(re.match(r'^\d{5,10}@qq.com',email)):
    print 'ok'
    
