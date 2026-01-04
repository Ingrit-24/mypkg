# ネタ切れ
![test](https://github.com/Ingrit-24/mypkg/actions/workflows/test.yml/badge.svg)
## 各ノード概要

| ノード名 | 処理内容 | 入力トピック名 | 出力トピック名 | 注意点 |
|:---|:---|:---|:---|:---|
|inkinematics|制御周期ごとの座標データから二輪ロボットの左右車輪速度を求めデータを返す|・delta_t<br>・wheel_dist<br>・coordinates|・velocities|このノードは制御周期ごとにcoordinatesが更新されることを前提としています| 

## トピック概要
| トピック名 | データ型 | データの中身 | 注意点 |
|:---|:---|:---|:---| 
|delta_t|std_msgs.msg/Float32|制御周期|| 
|wheel_dist|std_msgs.msg/Float32|車輪間距離|| 
|coordinates|geometry_msgs.msg/Point|座標データ|このパッケージのノードではZを不使用| 
|velocities|std_msgs.msg/Float32MultiArray|車輪速度|配列番号0が右<br>配列番号1が左| 


## 必要なソフトウェア
- Python
- ROS2 Jazzy Jalisco
## 依存ライブラリ

## テスト環境
- Ubuntu 24.04 LTS

## ライセンス
- このROS2パッケージは、**三条項BSDライセンスの下**、再配布及び使用が許可されます。
- © 2025 Shogo Takizawa