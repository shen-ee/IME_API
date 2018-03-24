# coding:utf-8
import requests

url = "http://166.111.139.15:8081/submit_text_for_IME"
data = "我{de__}位置{zai__}哪{li__}?"
ret = requests.post(url = url,data=data)

print(ret.text)
