# -*- coding: utf-8 -*-
import requests
import re
import json as js
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

AllgiftJson = {};

def saveFile(fileName, cnt):
    json = js.dumps(cnt, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4);
    json = json.replace('\\"', "");
    json = json.replace("\\r", "");
    print json;
    open(fileName, 'wb').write(json);

allUrl = 'https://www.douyu.com/directory/all';
allHtml = requests.get(allUrl).text;

maxPage = re.search(r'count: "(.+?)",' ,allHtml).groups(1);
print int(maxPage[0]);

for x in xrange(1,int(maxPage[0])):
    pageHtml = requests.get('https://www.douyu.com/directory/all?isAjax=1&page='+str(x)).text;
    hrefs = re.search(r'href="(.*?)"',pageHtml).groups(1);
    for url in hrefs:
        roomHtml = requests.get('https://www.douyu.com'+url).text;
        AllgiftData = re.finditer(r'data-giftid.+?\n.+?\n.+?\n.+?\n.+?', roomHtml);
        for giftData in AllgiftData:
            p = re.compile(r'\n');
            ss = p.split(giftData.group(0).replace(' ', ''));
            jsonData = {};
            giftid = '0';
            for data in ss:
                p = re.compile(r'=');
                s = p.split(data);
                if s[0] == '' or s[len(s)-1] == '':
                    continue;
                if s[0] == "data-giftid":
                    giftid = s[-1];
                print s[-1];
                jsonData[s[0]] = s[-1];
                print jsonData;
            AllgiftJson[giftid] = jsonData;
print AllgiftJson;
saveFile("douyu.json", AllgiftJson);