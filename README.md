# mypkg
[![test](https://github.com/harus860723/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/harus860723/mypkg/actions/workflows/test.yml)
## 概要説明
* 2023年千葉工業大学未来ロボティクス学科ロボットシステム学の授業で使用したリポジトリ。
* ロボットシステム学の課題2で提出したコマンド。

## ノードの説明

### 1.talker.py

### 機能
* 実行するとメッセージを送信する。
* 1秒ごとに0からの数字を送信するノード

### 実行

```
$ ros2 run mypkg talker
```

### 実行結果
* 実行しても何も表示されない。

### 2.listener

### 機能
* 実行するとメッセージを受け取り出力する。
* 受け取った数字を二乗し、12をかけ34を足した数を出力する。 

### 実行

```
$ ros2 run mypkg listener
```

### 実行結果
* 実行しても何も表示されない。

## トピック
* 今回は

## 使用方法

## テスト環境
* Ubuntu 22.04.2 LTS
* ROS2 Humble

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再領布および使用が許可される。

* このコードは、ロボットシステム学の授業で使用したスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものである。
	* [ryuichiueda/my_slides/robosys_2022/](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

© 2023 Haruki Matsushita
