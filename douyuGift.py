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
        try:
            AllgiftData =  js.loads(re.search(r'\$ROOM.propBatterConfig = (.+?);', roomHtml).group(1));
        except AttributeError:
            continue;
        for key in AllgiftData:
            print key ,"\n", AllgiftData[key];
            giftJson = {};
            giftJson["id"] = key;
            giftJson["name"] = AllgiftData[key]["name"];
            giftJson["weight"] = AllgiftData[key]["pc"];
            giftJson["iconUrl"] = AllgiftData[key]["small_effect_icon"];
            AllgiftJson[key] = giftJson;

saveFile("douyuGift.json", AllgiftJson);