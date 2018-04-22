# coding:utf-8
import requests
import json

def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

def change_format(str):
    newstr=""
    purestr=""
    last_char = -1 # 0表示中文符号 1表示英文符号
    for char in str:
        if(is_alphabet(char)): # 英文
            if last_char == 0:
                newstr+="{"
            last_char = 1
        else : # 中文
            if last_char == 1:
                newstr+="__}"
            last_char = 0
            purestr = purestr+char
        newstr+=char
    return newstr,purestr

def show_result(res,purestr):
    num = len(res)
    purestr = list(purestr)
    for i in range(num):
        candidate = res[i]['candidates'][0][0]
        position = res[i]['position']
        print("第"+str(i+1)+"个字符为:"+candidate+",位置为:"+str(position))
        purestr.insert(position,candidate)
    purestr = "".join(purestr)
    print("\n新的字符串："+purestr)


original_str = "我de位置zai哪li?"

newstr,purestr=change_format(original_str)
print("原始字符串："+ original_str)
print("查询字符串："+ newstr)
print("纯字符串："+ purestr)

url = 'http://166.111.139.15:8081/submit_text_for_IME'
text = newstr
data = {"text":text}
ret = requests.post(url, data=data)
res = ret.json()['result']


show_result(res,purestr)
