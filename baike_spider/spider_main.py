#!usr/bin/python
# -*- coding: utf-8 -*-
from baike_spider import url_manager, html_downloader, html_parser, html_outputer

__author__ = "sunsn"

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "crawl %d: %s" % (count, new_url)
                html_cont = self.downloader.dowload(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break

                count += 1
            except:
                print "crawl failed"

        self.outputer.html_output()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()

    obj_spider.crawl(root_url)