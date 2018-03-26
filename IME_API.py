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
    newstr=''
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
        newstr+=char
    return newstr



original_str = "我de位置zai哪li?"

print("原始字符串："+ original_str)
print("查询字符串："+ change_format(original_str))

# url = 'http://166.111.139.15:8081/submit_text_for_IME'
# d = format(original_str)
# ret = requests.post(url, data=d)
#
# print(ret.text)
