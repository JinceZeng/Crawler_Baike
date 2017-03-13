#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 15:03
# @Author  : Jince
# @File    : html_downloader.py
# @Software: PyCharm


import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        else:
            response = urllib2.urlopen(url)
            if response.getcode() != 200:
                return

            return response.read()