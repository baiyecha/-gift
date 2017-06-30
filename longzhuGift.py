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
for array in js.loads(requests.get(allUrl).text):
    giftJson = {};
    giftJson["id"] = array["id"];
    giftJson["name"] = array["title"];
    giftJson["weight"] = array["costValue"];
    giftJson["iconUrl"] = array["pngUrl"];
    AllgiftJson[array["id"]] = giftJson;

saveFile("longzhuGift.json", AllgiftJson);
