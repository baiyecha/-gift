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

allUrl = 'https://www.zhanqi.tv/api/static/v2.1/live/list/10/1.json';
allHtml = requests.get(allUrl).text;

maxPage = re.search(r'"cnt":(\d+),' ,allHtml).groups(1);
print int(maxPage[0]);

for x in xrange(1,int(maxPage[0])+1):
    pageHtml = requests.get('https://www.zhanqi.tv/api/static/v2.1/live/list/1500/' + str(x) + '.json').text;
    responseJSON = js.loads(pageHtml);
    for item in responseJSON['data']['rooms']:
        giftHtml = requests.get('https://www.zhanqi.tv/api/static/v2.1/gifts/' + item['id'] + '.json').text;
        giftJson = js.loads(giftHtml);
        for array in giftJson["data"]:
            oneGiftJson = {};
            oneGiftJson["id"] = array["id"];
            oneGiftJson["name"] = array["name"];
            oneGiftJson["price"] = array["price"];
            AllgiftJson[array["id"]] = oneGiftJson;

saveFile("zhanqiGift.json", AllgiftJson);
