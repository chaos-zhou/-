#! python3
# -*- coding: utf-8 -*-
from aip import AipSpeech
import requests
import re
from bs4 import BeautifulSoup
'''
爬取天气网
http://www.weather.com.cn/weather/101010300.shtml
'''
def getHtmlText(url,code='utf-8'):
  try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=code

    return r.text
  except:
    return ''
def makeSoup(html):
  wstr=''
  if html =='':
      return '不知道天气'
  else:
      soup=BeautifulSoup(html,'html.parser')
      soup1=soup.find_all('meta',attrs={'name':'description'})
    #  print(soup1)
      str1=re.findall(r'"(.*?)"',str(soup1))
      for i in str1[0]:
         if i !='':
            wstr=wstr+i
      if '雨' in wstr:
         wstr+='，别忘了带伞，'
     # print(wstr)
     # print(str1)
      return wstr
'''
使用百度的 AIP将文字转成mp3文件
'''
def stringToMp3(strings_txt):
  strings_txt='早上好，快起床，天气如下， '+strings_txt
  APPID='********'
  APIKey='**************'
  SecretKey='*************'
  aipSpeech=AipSpeech(APPID,APIKey,SecretKey)
  result=aipSpeech.synthesis(strings_txt,'zh','1',\
                            {'vol':8,
                             'per':4,
                             'pit':6,
                             'spd':5})
  if not isinstance(result,dict):
     with open('test_tmp1.mp3','wb') as f:
         f.write(result)
'''
执行主程序
'''
def main():
 # url='http://www.weather.com.cn/weather/101010300.shtml'
  url='http://tianqi.moji.com/'
  html=getHtmlText(url)
  stringToMp3(makeSoup(html))

if __name__=='__main__':
  main()
