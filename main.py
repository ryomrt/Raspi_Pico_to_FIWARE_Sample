#動作環境
#Raspberry Pi pico W + DHT22(AM2302) ※温湿度センサーモジュール

#必要なモジュールをインポート
import json
import urequests
import os

import time
import network
import socket
from machine import Pin

import gc #メモリ管理

#以下のモジュールは外部モジュールなので、以下からダウンロードして別途Pi pico Wに送信しておく
#https://github.com/danjperron/PicoDHT22/blob/main/PicoDHT22.py
from PicoDHT22 import PicoDHT22

#温湿度センサのイニシャライズ。GPIO 16に接続されている想定
dht22 = PicoDHT22(Pin(16,Pin.IN,Pin.PULL_UP))

#FIWARE Orionの設定項目
authorization = 'yourauthorizationkey'
orion_endpoint = 'http://yourendpoint/'
Fiware_Service = 'make_our_city_data_sample' 
Fiware_ServicePath = '/'

#接続先のWi-FiのSSIDとパスワードを入力
ssid = 'YourWiFiSSID'
password = 'YourWiFiPassword'

#ネットワークへ接続
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

##タイムアウト処理(10回失敗したら例外を吐く)
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

#ISO形式で現在時刻を取得する関数(日本のローカル時刻+09:00を想定)
def getNowIsoFormatString():
    now = time.localtime()
    return "{}-{}-{}T{}:{}:{}+09:00".format(now[0],now[1],now[2],now[3],now[4],now[5],now[6]) #もっとスマートなコードありそう

#FIWARE Orionにデータを送信する関数
def DataSend(APIurl, PayLoad):
    headers = {
        'content-type': 'application/json',
        'Fiware-Service': Fiware_Service,
        'Fiware-ServicePath': Fiware_ServicePath,
        'Authorization': authorization
    }
    try:
        response = urequests.post(orion_endpoint + APIurl, headers=headers, data=json.dumps(PayLoad))
        status = response.status_code
    except:
        print("err")
        status = 0
    response.close()
    return status

#初回のループは、エンティティを作成しにいくのでフラグで管理する
FirstLoop = True

#データの設定項目
dataType = "Room"
entityId = "ConferenceRoom"

while True:
    #温度と湿度を取得
    T, H = dht22.read()
    
    #一応取れたデータを表示する
    if T is None:
        print("T=----\xdfC H=----}%")
    else:
        print("T={:3.1f}\xdfC H={:3.1f}%".format(T,H))
    
    if FirstLoop:
        #エンティティ自体を作成する（すでに存在する場合はHTTP 422のエラーが返ってくるが問題ない）
        #参考：https://fiware-orion.letsfiware.jp/orion-api/#create-entity-post-v2entities
        data = {
            "type": dataType,
            "id": entityId,
            "temperature": {
                "value": T,
                "type" : "Float",
                "metadata": {}
            },
            "humidity": {
                "value": H,
                "type" : "Float",
                "metadata": {}
            },
            "updatedAt": {"value": getNowIsoFormatString(), "type": "DateTime"}
        }
        status = DataSend(APIurl="/v2/entities", PayLoad=data)
        print(status)
        
        FirstLoop = False
    else:
        #指定したエンティティIDのエンティティが持つ属性データを全て更新する（無いものは追加される）
        #参考：https://fiware-orion.letsfiware.jp/orion-api/#update-or-append-entity-attributes-post-v2entitiesentityidattrs
        data = {
            "temperature": {
                "value": T,
                "type" : "Float",
                "metadata": {}
            },
            "humidity": {
                "value": H,
                "type" : "Float",
                "metadata": {}
            },
            "updatedAt": {"value": getNowIsoFormatString(), "type": "DateTime"}
        }
        status = DataSend(APIurl="/v2/entities/" + entityId +"/attrs", PayLoad=data)
        print(status)
    
    gc.collect()
    time.sleep(10)
    