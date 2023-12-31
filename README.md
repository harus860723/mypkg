# mypkg
[![test](https://github.com/harus860723/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/harus860723/mypkg/actions/workflows/test.yml)

## 概要説明
* 2023年千葉工業大学未来ロボティクス学科ロボットシステム学のROS2の授業で使用したリポジトリ。
* ロボットシステム学の課題2で提出したコマンド。
* talker.pyとlistener.pyの2つのノードがある。

## ノードの説明

### 1. talker.py

### 機能
* パブリッシャを持つノードである。
* 1秒ごとに0からの数字をカウントし送信する。

### 実行

```
$ ros2 run mypkg talker
```

### 実行結果
* 実行しても何も表示されない。

### 2. listener

### 機能
* サブスクライバを持つノードである。
* トピックからメッセージを受け取る。
* 受け取った数字を二乗し、12をかけ34を足した数を出力する。 

### 実行

```
$ ros2 run mypkg listener
```

### 実行結果
* 実行しても何も表示されない。

## トピック
* メッセージはtalkerでカウントされた数字である。
* メッセージの型は16ビットの符号つき整数。

## ノードの使用方法

### 準備
* ROS2が使える環境を整える。
* cloneコマンドを使用しリポジトリをインストールする。

```
$ git clone https://github.com/harus860723/mypkg?tab=readme-ov-file
```

* インストールしたリポジトリをビルドする。

### 実行方法
* 端末1でtalkerを実行する。

```
$ ros2 run mypkg talker
```

* 端末2でlistenerを実行する。

```
$ ros2 run mypkg listener
```

### 実行結果

* 端末1は何も表示されない。
* 端末２

```
[INFO] [1703587822.661840100] [listener]: Answer: 34
[INFO] [1703587823.624772700] [listener]: Answer: 46
[INFO] [1703587824.624063900] [listener]: Answer: 82
[INFO] [1703587825.625573200] [listener]: Answer: 142
[INFO] [1703587826.624655700] [listener]: Answer: 226
[INFO] [1703587827.623980500] [listener]: Answer: 334
[INFO] [1703587828.624138500] [listener]: Answer: 466
[INFO] [1703587829.624617300] [listener]: Answer: 622
[INFO] [1703587830.624348000] [listener]: Answer: 802
[INFO] [1703587831.624600600] [listener]: Answer: 1006
```

* １秒ごとに計算結果が表示される。

## launchの使用方法

### 機能
* 複数のノードを一度に立ち上げることができる。
* ノードごとに実行しなくてもよい。

### 実行方法
* 端末でlaunchを実行

```
$ ros2 launch mypkg talk_listen.launch.py
```

### 実行結果

```
[INFO] [launch]: All log files can be found below /home/haru/.ros/log/2023-12-27-14-25-30-463360-MyComputer-1671
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [1672]
[listener-2] [INFO] [1703654731.884197200] [listener]: Answer: 34
[listener-2] [INFO] [1703654732.873949000] [listener]: Answer: 46
[listener-2] [INFO] [1703654733.873977300] [listener]: Answer: 82
[listener-2] [INFO] [1703654734.873437700] [listener]: Answer: 142
[listener-2] [INFO] [1703654735.873878100] [listener]: Answer: 226
[listener-2] [INFO] [1703654736.873827200] [listener]: Answer: 334
[listener-2] [INFO] [1703654737.873776300] [listener]: Answer: 466
[listener-2] [INFO] [1703654738.872654700] [listener]: Answer: 622
[listener-2] [INFO] [1703654739.873408200] [listener]: Answer: 802
[listener-2] [INFO] [1703654740.873788300] [listener]: Answer: 1006
```


## テスト環境
* Ubuntu 22.04.2 LTS
* ROS2 Humble

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再領布および使用が許可される。

* このコードは、ロボットシステム学の授業で使用したスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものである。
	* [ryuichiueda/my_slides/robosys_2022/](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

© 2023 Haruki Matsushita
