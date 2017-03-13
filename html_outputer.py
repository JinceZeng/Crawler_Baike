#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/12 15:03
# @Author  : Jince
# @File    : html_outputer.py
# @Software: PyCharm
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        ###################HTML输出
        # fout = open('output.html', 'w')
        #
        # fout.write('<html>')
        # fout.write('<head><meta charset="utf-8"></head>')
        # fout.write('<body>')
        # fout.write('<table>')
        #
        # for data in self.datas:
        #     fout.write('<tr>')
        #     fout.write('<td>%s</td>' % data['url'].encode('utf-8'))
        #     fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
        #     fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
        #     fout.write('</tr>')
        #
        # fout.write('</table>')
        # fout.write('</body>')
        # fout.write('</html>')


        ####################MakeDown输出
        fout = open('output.md', 'w')
        # 使用MarkDown语法输出
        fout.write('#BaiKe\n')
        for data in self.datas:
            fout.write("##[%s](%s)##\n" % (data['title'].encode('utf-8'), data['url'].encode('utf-8')))
            fout.write("> %s" % (data['summary'].encode('utf-8')))
            fout.write('\n\n---------\n\n')  # 分隔线
        fout.close()

        print 'output finished!'