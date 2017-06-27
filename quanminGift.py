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

allUrl = 'http://www.quanmin.tv/shouyin_api/public/config/gift/pc?debug&categoryId=1&_=1497928439407';
allHtml = requests.get(allUrl).text;

allJson = js.loads(allHtml);
print allJson["data"]["lists"][0]["cid"];
for array in allJson["data"]["lists"]:
    giftJson = {};
    giftJson["id"] = array["id"];
    giftJson["name"] = array["name"];
    giftJson["weight"] = array["weight"];
    AllgiftJson[array["id"]] = giftJson;

saveFile("quanminGift.json", AllgiftJson);