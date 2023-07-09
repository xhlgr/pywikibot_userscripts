#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#寻找有中括号或大括号不相等的页面，即有问题页面

#import datetime
import re
import pywikibot
from pywikibot import pagegenerators
#from pywikibot.bot import ExistingPageBot

def main():
    # The site we want to run our bot on
    site = pywikibot.Site('zh','wikiname')#,'User'可加用户名
    
    #获取主命名空间所有页面
    gen = pagegenerators.AllpagesPageGenerator(start='!', namespace=0, includeredirects=False, site=site, total=None, content=False)
    countbig = 0#符合条件页面数计数
    countmid = 0#符合条件页面数计数
    for page in gen:
        #逐个页面判断下行最大值是否正确
        #print(page.title())
        #print(page.expand_text())#展开模板后text
        #删掉html注释内容
        text_delnote = re.sub(r'<!--[\s\S]*?-->','',page.expand_text())
        #匹配算出左右括号数量
        pattern = re.compile(r'\{')#查找页面左大括号\{
        lbigarr = pattern.findall(text_delnote)#找到所有左大括号
        lbigmax = len(lbigarr)#左大括号个数
        pattern = re.compile(r'}')#查找页面右大括号}
        rbigarr = pattern.findall(text_delnote)#找到所有右大括号
        rbigmax = len(rbigarr)#右大括号个数
        pattern = re.compile(r'\[')#查找页面左中括号\[
        lmidarr = pattern.findall(text_delnote)#找到所有左中括号
        lmidmax = len(lmidarr)#左中括号个数
        pattern = re.compile(r']')#查找页面右中括号]
        rmidarr = pattern.findall(text_delnote)#找到所有右中括号
        rmidmax = len(rmidarr)#右中括号个数
        if lbigmax != rbigmax:
            #\033[31m(31红色32绿色33黄色34蓝色35紫色36青色)，\033[0m结束
            print("\033[31m"+page.title()+"左右大括号不对等\033[0m")
            countbig = countbig + 1
        if lmidmax != rmidmax:
            print("\033[33m"+page.title()+"左右中括号不对等\033[0m")
            countmid = countmid + 1
    print("已执行完","共",countbig,"个页面大括号有问题","共",countmid,"个页面中括号有问题")

if __name__ == '__main__':
    main()
