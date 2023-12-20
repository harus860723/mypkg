# robosys2023
* 2023年ロボットシステム学の授業で使用したリポジトリ。
* plusコマンドはロボットシステム学の課題1で機能を追加したコマンド。

# plusコマンド
[![test](https://github.com/harus860723/robosys2023/actions/workflows/test.yml/badge.svg)](https://github.com/harus860723/robosys2023/actions/workflows/test.yml)

## plusコマンドについて

* 標準入力から読み込んだ数字を足す。
* 計算結果の値が偶数か奇数かを調べ出力。
* 偶数の場合はその値に2で割った値を出力。
* 奇数の場合はその値に2を掛けた値を出力。

## 使い方

### インストール

* robosys2023をcloneする。
```
$ git clone https://github.com/harus860723/robosys2023.git
```

### 実行例
* コードの実行例を下に示す。

```
$ seq 5 | ./plus
```

### 実行結果
* 実行例の結果を下に示す。

```
合計値:15
odd number
値に2をかけた数: 30
```

## 必要なソフトウェア
* Python
  * テスト済み: 3.7〜3.10

## テスト環境
* Ubuntu 22.04.2 LTS

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再領布および使用が許可される。

* このコードは、ロボットシステム学の授業で使用したスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものである。
	* [ryuichiueda/my_slides/robosys_2022/](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

© 2023 Haruki Matsushita
