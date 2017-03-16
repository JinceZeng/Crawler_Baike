#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/14 15:34
# @Author  : Jince
# @File    : comments_163.py
# @Software: PyCharm
from selenium import webdriver
import datetime


#数据爬取类
class html_Parser():
    def __init__(self):
        # 这是一些配置 关闭loadimages可以加快速度 但是第二页的图片就不能获取了打开(默认)
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        # cap["phantomjs.page.settings.loadImages"] = False
        # cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
        self.driver = webdriver.PhantomJS(desired_capabilities=cap)

    #主爬取函数
    def parse(self, new_url):
        new_urls = set()
        self.driver.get(new_url)
        self.driver.switch_to.frame('contentFrame')#内嵌HTML定位
        list_title = self.driver.find_element_by_xpath('//div[@class="tit"]/h2').text
        try:
            songs = self.driver.find_elements_by_xpath('//span[@class="txt"]/a')
            for song in songs:
                songs_url = song.get_attribute('href')
                new_urls.add(songs_url)
        except Exception, e:
            print u'获取异常 %s' % e.message
        new_datas = self.parse_comments(new_urls)
        return list_title, new_datas

    #爬取歌单每首歌下的评论
    def parse_comments(self, new_urls):
        new_datas = []
        for url in new_urls:
            new_data = {}
            self.driver.get(url)
            self.driver.switch_to.frame('contentFrame')  # 内嵌HTML定位
            title = self.driver.find_element_by_xpath('//div[@class="tit"]/em').text
            new_data['url'] = url
            new_data['title'] = title
            #<div class ="cnt f-brk"><a href="/user/home?id=67087776" class ="s-fc7" > 请叫S小姐嫣芷妞 </a>：为什么</div >
            comments_drivers = self.driver.find_elements_by_xpath('//div[@class="cnt f-brk"]')
            comments = []
            for comments_driver in comments_drivers:
                #comment_name = comments_driver.find_element_by_xpath('//div[@class="cnt f-brk"]/a').text
                comment_cont = comments_driver.text   #.text获取为该标签下所有文本
                #comment = comment_name+comment_cont
                comments.append(comment_cont)
            new_data['comments'] = comments
            new_datas.append(new_data)
        return new_datas


#数据输出到.md文件
class html_Output():
    def output(self,list_title, datas):
        ####################MakeDown输出
        fout = open(list_title+'.md', 'w')
        # 使用MarkDown语法输出
        fout.write("# %s #\n" % list_title.encode('utf-8'))
        for data in datas:
            fout.write("## %s (%s)##\n" % (data['title'].encode('utf-8'), data['url'].encode('utf-8')))
            for comment in data['comments']:
                fout.write("- %s \n" % (comment.encode('utf-8')))
            fout.write('\n\n---------\n\n')  # 分隔线
        fout.close()

#主爬虫类
class spiderMain():
    def __init__(self):
        #self.manager = html_Manager()
        #self.downloader = html_Download()
        self.parser = html_Parser()
        self.outputer = html_Output()

    def craw(self, seed_url):
        begin_time = datetime.datetime.now()
        list_title, new_datas = self.parser.parse(seed_url)
        self.outputer.output(list_title, new_datas)
        end_time = datetime.datetime.now()
        print '用时：%s \n' % str(end_time-begin_time), 'craw finished!'


if __name__ == '__main__':
    seed_url = 'http://music.163.com/#/playlist?id=105095501'
    spider = spiderMain()
    spider.craw(seed_url)

