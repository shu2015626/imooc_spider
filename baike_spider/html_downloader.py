#!usr/bin/python
# -*- coding: utf-8 -*-
import cookielib
import urllib2

__author__ = "sunsn"


class HtmlDownloader(object):
    def dowload(self, url):
        if url is None:
            return

        # 构建增强型的urllib2
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        request = urllib2.Request(url)
        request.add_header("User-Agent","Mozilla/5.0")
        response = urllib2.urlopen(request)

        if response.getcode() != 200:
            return

        return response.read()