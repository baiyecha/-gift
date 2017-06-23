#-*- coding: utf-8 -*-
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

allUrl = 'http://configapi.plu.cn/item/getallitems';
allHtml = requests.get(allUrl).text;

AllgiftData = re.finditer(r'preActions":\[\],(.+?),"smallIcon', allHtml);
for giftData in AllgiftData:
    print giftData.group(1);
    p = re.compile(r',');
    ss = p.split(giftData.group(0));
    jsonData = {};
    giftid = '0';
    for data in ss:
        print data;
        p = re.compile(r':');
        s = p.split(data);
        print s[0];
        if s[0] == '' or s[len(s)-1] == '':
            continue;
        if s[0] == '"id"':
            giftid = s[-1];
        if s[0] == '"id"' or s[0] == '"title"' or s[0] == '"costValue"' :
            jsonData[s[0]] = s[-1];
        #print jsonData;
    AllgiftJson[giftid] = jsonData;
print AllgiftJson;
saveFile("longzhu.json", AllgiftJson);
