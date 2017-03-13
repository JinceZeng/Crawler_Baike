#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 15:02
# @Author  : Jince
# @File    : spider_main.py
# @Software: PyCharm
#import url_manager, html_downloader, html_parser, html_outputer
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' %(count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count ==10:
                    print 'craw finished!'
                    break

                count = count+1
            except:
                print 'craw failed!'
        self.outputer.output_html()



if __name__=='__main__':
    root_url = 'http://baike.baidu.com/link?url=g9BYPV5l-0kwr4V4r8T-CyQGMW9k8eKO1AoEqDADnRvwTbUKnj827DRN_RZtblho7lXAqDzX1CEGoOidLFdI6K'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)