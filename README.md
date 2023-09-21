# Raspi_Pico_to_FIWARE_Sample
 Sample code to acquire sensor data with Raspberry pi pico and send it to FIWARE

# 1. これはなに？
「浜松で地域課題解決やらまいか！ データ・フュージョン・キャンプ２０２３ ～浜松市データ連携基盤を活用したサービス開発実践プログラム～」にて、「Make our City data」チームで取り組んでいたものの一部です。
データが無ければ、自分たちで作ってしまえばいいじゃない。ということで、安く入手できるシングルボードコンピュータを使って、センサーデータを取得し、FIWAREへ送り込むサンプルコードです。

# 2. サンプルコードの機能
指定したFIWAREエンドポイントに対し、

# 3. 機器構成
- Raspberry Pi pico : RP2040マイコンを搭載した開発基板
- DHT22 (AM2302) : 温湿度センサ
  https://www.amazon.co.jp/DSD-TECH-Arduino-Raspberry-Pi%E7%94%A8%E6%B8%A9%E6%B9%BF%E5%BA%A6%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB/dp/B07CM2VLBK
線のつなぎ方は、別添構成図をご覧ください。

# 3. SpecialThanks
- O氏：FIWAREの仕様を調べてPythonで送り込む部分の大部分を作ってくれました。ありがとうございます。
- N氏：ピンヘッダをすごい勢いで半田付けしてくれました。ありがとうございます。
- U氏：ハマりにハマったurequestsのメモリ解放されない問題のフォローをしてもらいました。ありがとうございます。
