# Monokey

Monokey(モノキー)はキーホルダー型の1%キーボードです。  
ミニマムな外見ですが、XIAO RP2040を搭載し、USB接続でPC等と接続することで1キーのキーボードとしても使用可能です。  
とてもシンプルな構造ですので、自作キーボードの入門用としてももちろん、好きなキーキャップを取り付けてアクセサリとして使うことも可能です。

## 組み立てに必要な部品

|部品|個数|備考|
|:--|:--|:--|
|Monokey 基板|1||
|[XIAO RP2040](https://talpkeyboard.net/items/63534f58f5197322fceb6487)|1||
|キースイッチ|1|Cherry MX互換スイッチとKailh Choc v1キースイッチのハンダ付けが可能|
|キーキャップ|1||
|ボールチェーン|1|キーホルダーとして利用する場合|

## 組み立てに必要な道具
- ハンダごて
- ハンダ
- ニッパー
- サインペン
- マスキングテープ

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


<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_49.jpg?raw=true" width = "600px" />

<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_49.jpg?raw=true" width = "600px" />

<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_49.jpg?raw=true" width = "600px" />

<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_49.jpg?raw=true" width = "600px" />

<img src = "https://github.com/takashicompany/monokey/blob/master/images/build/IMG_49.jpg?raw=true" width = "600px" />
