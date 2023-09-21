# Raspi_Pico_to_FIWARE_Sample
 Sample code to acquire sensor data with Raspberry pi pico and send it to FIWARE

# 1. これはなに？
「浜松で地域課題解決やらまいか！ データ・フュージョン・キャンプ２０２３ ～浜松市データ連携基盤を活用したサービス開発実践プログラム～」にて、「Make our City data」チームで取り組んでいたものの一部です。
データが無ければ、自分たちで作ってしまえばいいじゃない。ということで、安く入手できるシングルボードコンピュータを使って、センサーデータを取得し、FIWAREへ送り込むサンプルコードです。

# 2. 機器構成・環境
- Raspberry Pi Pico W: RP2040マイコンを搭載した開発基板（Wi-Fi搭載版）
- DHT22 (AM2302) : 温湿度センサ
  https://www.amazon.co.jp/DSD-TECH-Arduino-Raspberry-Pi%E7%94%A8%E6%B8%A9%E6%B9%BF%E5%BA%A6%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB/dp/B07CM2VLBK

Raspberry Pi Pico W自体の設定～Wi-Fi接続までは以下のURLを参考にしました。
https://sozorablog.com/raspberry-pi-pico-w-review/

線のつなぎ方は、以下の構成図をご覧ください。
![構成図](/構成図.png)


# 3. サンプルコードの機能
Raspberry Pi Pico Wから、指定したWi-Fiアクセスポイントに接続します。
FIWARE Orionのエンドポイントに対し、センサーから取得した温度・湿度のデータを、現在時刻＝更新日時とともに送り込み、10秒待機することを繰り返します。
エンティティが無いとデータの更新ができないため、電源を入れて1回目は、エンティティを作成しにいき、2回目以降のループで更新をかけます。

# 4. 必要なモジュール
以下のモジュールを使用しています
- https://github.com/danjperron/PicoDHT22

# 5. SpecialThanks
- O氏：FIWAREの仕様を調べてPythonで送り込む部分の大部分を作ってくれました。ありがとうございます。
- N氏：ピンヘッダをすごい勢いで半田付けしてくれました。ありがとうございます。
- U?氏：ハマりにハマったurequestsのメモリ解放されない問題のフォローをしてもらいました。ありがとうございます。
