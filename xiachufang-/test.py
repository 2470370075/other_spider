import requests
import re
# req=requests.get('http://www.xiachufang.com')
# print(req.text)
#
# pat=re.compile(r'src="(http://.*?.jpg)')
# print(pat.findall(req.text))



str='aaaasrc="asd"'
pat=re.compile(r'=\"')
print(pat.findall(str))