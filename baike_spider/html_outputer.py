#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "sunsn"


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def html_output(self):
        fout = open("output.html", "w")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border=1px>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"].encode("utf-8"))
            fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()