import fontTools
from fontTools.ttLib.ttFont import TTFont
#
font = TTFont('maoyan7.woff')

font.saveXML('local_fonts7.xml')


# # 每一个数字虽然对应多个16进制，但是对应一个唯一坐标
# f = font.getGlyphOrder()[2]
# print(f)
# print(font['glyf'][f].coordinates)
# print(font['glyf'][f].coordinates.array)
# print(font['glyf'][f].coordinates.array.tobytes())
# print(font['glyf'][f].coordinates.array.tobytes().hex())
# '7e01f5ff1d01e2ff2401230206010402d900e601a400c7017200bb0170000f02b0003102f90064020f01760221018c023001af025201cc027e01d1027e01e6ff'
# '7f01f1ff1e01e6ff2401230203011102c900e6019d00b8016900b70174001a02ac003102f40064020b017702210196022f01ae024401bd028201d1027801e6ff'
# '7f01e6ff2401e6ff24011e020301fe01ce00db019000b9016700ba0170000b02b600310201015e0206017d02260196023801b8024a01c6027001c2027e01e5ff'
#
# # print(font.keys())  # ['GlyphOrder', 'head', 'hhea', 'maxp', 'OS/2', 'hmtx', 'cmap', 'loca', 'glyf', 'name', 'post', 'GSUB']
# #
# # # 获取getGlyphOrder节点的name值，返回为列表
# # print(font.getGlyphOrder())  # ['glyph00000', 'x', 'uniF013', 'uniF4D4', 'uniEE40', 'uniF7E1', 'uniF34B', 'uniE1A0', 'uniF1BE', 'uniE91E', 'uniF16F', 'uniF724']
# # print(font.getGlyphNames())
# # print(font.getBestCmap())
# #
# s =""""""
# print(s)
# print(ord(s))
# '&#xf2d1;&#xf7cd;'
#
# #
# dec = ord(s)






import re
import requests


# def get_cookies(cookies_string):
#     cookies_string = '; ' + cookies_string + ';'
#     keys = re.findall('; (.*?)=', cookies_string)
#     values = re.findall('=(.*?);', cookies_string)
#     cookies = dict(zip(keys, values))
#     return cookies
#
# cookies_str = '__mta=46011163.1586164010929.1586164023247.1586164053672.4; uuid_n_v=v1; uuid=3A8EEC5077E611EAB94CB3AA241DB1BC2B262789B09744949DDABB9017794081; _csrf=85946e464629738304d3ec3e1d080103526d546df95e201c89289b5de00315f3; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1714ebe0c91c8-0df0ece2c085eb-3a36510f-144000-1714ebe0c91c8; _lxsdk=3A8EEC5077E611EAB94CB3AA241DB1BC2B262789B09744949DDABB9017794081; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1586164010; __mta=46011163.1586164010929.1586164010929.1586164010929.1; mojo-uuid=841eeb4e30d6c9694e330b8659315f92; mojo-session-id={"id":"0a4e6f5134db1e7b958b8fa925815b3c","time":1586164011000}; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1586164053; _lxsdk_s=1714ebe0c93-e9d-d39-da1%7C%7C10'
# cookies = get_cookies(cookies_str)
#
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
#
# headers = {
#     'User-Agent':user_agent
# }
# r = requests.get('https://maoyan.com/films/1218273',headers=headers,cookies=cookies)
#
# print(r.text)

