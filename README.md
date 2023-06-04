# Monokey

<img src = "https://github.com/takashicompany/monokey/blob/master/images/01.jpg?raw=true" width = "600px" />

Monokey(モノキー)はキーホルダー型の1%キーボードです。  
ミニマムな外見ですが、XIAO RP2040を搭載し、USB接続でPC等と接続することで1キーのキーボードとしても使用可能です。  
とてもシンプルな構造ですので、自作キーボードの入門用としてももちろん、好きなキーキャップを取り付けてアクセサリとして使うことも可能です。

<img src = "https://github.com/takashicompany/monokey/blob/master/images/02.jpg?raw=true" width = "600px" />

## 組み立てに必要な部品

|部品|個数|備考|
|:--|:--|:--|
|Monokey 基板|1||
|[XIAO RP2040](https://talpkeyboard.net/items/63534f58f5197322fceb6487)|1||
|キースイッチ|1|Cherry MX互換スイッチとKailh Choc v1キースイッチのハンダ付けが可能|
|キーキャップ|1||
|ボールチェーン|1|キーホルダーとして利用する場合|

## 組み立てに必要な道具

|道具|備考|
|:--|:--|
|ハンダごて|おすすめは[HAKKO FX-600](https://www.hakko.com/japan/products/hakko_fx600.html)です。[こて台](https://www.hakko.com/japan/products/hakko_kote_board.html)もあると、より作業をスムーズに進められます。|
|ハンダ|[こちら](https://www.goot.jp/products/detail/se_06008)などを使う方が多いようです。|
|ピンセット|100均などで手に入るものでも充分利用できるかと思います。|
|ニッパー|100均などで手に入るものでも充分利用できるかと思いますが、1000円程度ものを買っても損では無いかと思います。|

## あるとさらに完成度が高くなる道具
|道具|備考|
|:--|:--|
|棒ヤスリ|基板の縁にあるバリを削るのに使います。|
|サインペン|基板の縁を塗るとより美しくなります。|
|マスキングテープ|キースイッチをハンダ付けする際に役立ちます。|

## 組み立て方

### 1.基板の表裏の確認

基板の表裏を正しく確認することでミスを減らし作業を円滑に進めることが可能です。

**表(キースイッチとキーキャップを載せる側)**

<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4936.jpg?raw=true" width = "600px" />

**裏**

<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4934.jpg?raw=true" width = "600px" />

### 2. 基板の縁を塗る
この工程は、後回しにしても構いません。実施しなくとも動作には影響ありませんが、よりキーボードが美しくなります。  
サインペンなどで基板の縁を塗ります。基板の色と同じ色のペンを用意すると良いです。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4929.jpg?raw=true" width = "600px" />

基板の面側にはみ出ないように塗るとより美しくなります。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4931.jpg?raw=true" width = "600px" />

### 3. キースイッチのハンダ付け

キースイッチを基板にハンダ付けをします。  
キースイッチはCherry MX互換キースイッチやKailh Choc v1キースイッチの取り付けに対応しております。  
今回の説明ではCherry MX互換キースイッチを例に解説をします。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4932.jpg?raw=true" width = "600px" />

キースイッチを基板の表面に載せます。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4937.jpg?raw=true" width = "600px" />

キースイッチと基板をマスキングテープなどで仮止めすると、後の作業が円滑に進めることができます。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4938.jpg?raw=true" width = "600px" />

基板を裏返します。この時キースイッチが基板から離れないようにご注意ください。  
Cherry MX互換キースイッチの場合は、赤丸の箇所からキースイッチの足が出ていることを確認してください。  
Kailh Choc v1キースイッチの場合は緑の丸の箇所からキースイッチの足が出ていることを確認ください。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4951_b.jpg?raw=true" width = "600px" />

基板とキースイッチの足をハンダ付けします。  
ハンダ付け後、基板からキースイッチが離れないことを確認します。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4953.jpg?raw=true" width = "600px" />

### 4. XIAO RP2040の取り付け

XIAO RP2040は、MCU(Micro Controller Unit)と呼ばれるもので、キースイッチの入力を処理しUSBケーブルで繋いだPCに伝達する役割があります。  
ハンダ付けには付属のピンヘッダを使用します。    
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4943.jpg?raw=true" width = "600px" />

ピンヘッダを下図と同じになるようにXIAO RP2040の穴に差し込みます。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4946.jpg?raw=true" width = "600px" />

XIAO RP2040とピンヘッダをハンダ付けします。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4949.jpg?raw=true" width = "600px" />

XIAO RP2040にハンダ付けしたピンを基板の裏面に差し込みます。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4955.jpg?raw=true" width = "600px" />

ピンヘッダのピンが基板の表側から出ていることを確認します。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4957.jpg?raw=true" width = "600px" />

ピンヘッダのピンをニッパーで短くします。  
短くしすぎると後のハンダ付けが難しくなりますので、少し残るぐらいが適切かと思います。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4959.jpg?raw=true" width = "600px" />

ピンと基板をハンダ付けします。キースイッチにハンダが付かないよう注意してください。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4960.jpg?raw=true" width = "600px" />

### 5. ファームウェアの書き込み

[KMK Firmware](https://github.com/KMKfw/kmk_firmware)を用いる場合です。  

[こちら](http://kmkfw.io/docs/Getting_Started/)のKMK Firmwareの導入手順も併せて読むと理解が深まると思います。

[こちら](https://circuitpython.org/board/seeeduino_xiao_rp2040/)から.uf2ファイルをダウンロードします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/47f0223c-b40d-4b95-8516-b403834db523" width = "600px" />

XIAO RP2040のUSB口とは反対側にある「B」と書かれたスイッチを押しながらUSBケーブルを差します。  
「RPI-RP2」という名前の外部デバイスが表示されれば成功です。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4954_b.jpg?raw=true" width = "600px" />

ダウンロードした.uf2を「RPI-RP2」に書き込みます。ドラッグアンドドロップかコピーペーストで書き込めます。  
書き込み完了後、「CIRCUITPY」という名前の外部デバイスが表示されれば成功です。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/1edcd0e8-89cb-49ea-af4f-ae5e574fdd37" width = "600px" />

[KMK Firmwareのソースコードのzip](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip)をダウンロードします。  
解凍後、フォルダ内の`boot.py`と`kmkフォルダ`をCIRCUITPYにドラッグアンドドロップ or コピーペーストします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/7f36a17a-5073-4edc-b0dd-3008e8e5ef75" width = "600px" />

[こちら](https://github.com/takashicompany/monokey/blob/master/firmware/kmk/code.py)からKMK Firmware用のソースコード`code.py`をダウンロードして、CIRCUITPYにドラッグアンドドロップ　or コピーペーストをします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/0bfe6c1c-1bc5-4667-b853-cea94f43abf7" width = "600px" />

USBをPCに繋いだ状態でキーを押し「This is Monokey.」と入力されれば成功です。  
もし、動作しない場合は一度USBを抜き差しして再試行してください。  
`code.py`の以下の箇所を書き換えると、指定のキーや文字列を入力することが可能です。  
!<img src = "https://github.com/takashicompany/monokey/assets/4215759/5d16fddb-9742-4e00-bda8-d9dce3846fe3" width = "600px" />

### 6. キーキャップの取り付け

キーキャップをキースイッチに取り付けます。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4961.jpg?raw=true" width = "600px" />

### 7. ボールチェーンの取り付け

ボールチェーンを取り付けることで、キーホルダーとして活用できます。  
<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_4962.jpg?raw=true" width = "600px" />

以上で完成となります。

### 完成したら

完成しましたら、ぜひSNSなどに写真を投稿頂ければと思います。
Twitterのハッシュタグは [`#Monokey #自作キーボード`](https://twitter.com/search?q=%23%E8%87%AA%E4%BD%9C%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89%20%23Monokey&src=typed_query) を付けていただけると幸いです。
キットを組み立てた感想や、キーボードを使った所感などをお待ちしております！

また、毎週日曜日の１9時より実施されている自作キーボード写真コンテスト[「#KEEP_PD」](https://twitter.com/hashtag/KEEB_PD?f=live)に投稿頂くこともオススメです。  
開催の告知は[@KEEB_PD](https://twitter.com/KEEB_PD)にて行われております。

ご不明な点などございましたら、[@takashicompany](https://twitter.com/takashicompany)にメンションやDM頂ければ回答できるかと思います。

