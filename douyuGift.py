# -*- coding: utf-8 -*-
import requests
import re
import json


def saveFile(fileName, cnt):
    handle = open(fileName, 'wb')
    handle.write(cnt.decode('utf8'))
    handle.close()

allUrl = 'https://www.douyu.com/directory/all';
allHtml = requests.get(allUrl).text;

maxPage = re.search(r'count: "(.+?)",' ,allHtml).groups(1);
print int(maxPage[0]);

for x in xrange(1,int(maxPage[0])):
    pageHtml = requests.get('https://www.douyu.com/directory/all?isAjax=1&page='+str(x)).text;
    hrefs = re.search(r'href="(.*?)"',pageHtml).groups(1);
    for url in hrefs:
        roomHtml = requests.get('https://www.douyu.com'+url).text;
        AllgiftData = re.finditer(r'data-giftid.+?\n.+?\n.+?\n.+?', roomHtml);
        for giftData in AllgiftData:
            print giftData.group(0);
            p = re.compile(r'\n');
            ss = p.split(giftData.group(0).replace(' ', ''));
            jsonData = {};
            for data in ss:
                p = re.compile(r'=');
                s = p.split(data);
                if s[0] == '' or s[len(s)-1] == '':
                    continue;
                # print type(s[0]);
                print s[len(s)-1];
                jsonData[s[0]] = s[len(s)-1];
                print jsonData;
            json = json.dumps(jsonData);
            for _ in eval(json).values():
                print _, type(_)
            saveFile('list.json', json);
            exit(0);
#        try:
#            my.feed(roomHtml)
#            time.sleep(10)
#        except Exception as e:
#            print 'error'
#            pass