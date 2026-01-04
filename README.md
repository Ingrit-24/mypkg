# 二輪ロボットのためのパッケージ
![test](https://github.com/Ingrit-24/mypkg/actions/workflows/test.yml/badge.svg)
## 各ノード概要

| ノード名 | 処理内容 |入力トピック|出力トピック| 
|:---:|:---:|:---|:---|
|inkinematics|座標データから二輪ロボットの左右車輪速度を求め、<br>メッセージを流す|・delta_t<br>・wheel_dist<br>・coordinates|・velocities|
|odometry|左右車輪速度から現在位置を推定し、メッセージを流す|・delta_t<br>・wheel_dist<br>・velocities|・|
## 各トピック概要
| トピック名 | データ型 | データの中身 | 注意点 |
|:---|:---|:---|:---| 
|delta_t|std_msgs.msg/Float32|制御周期[s]|| 
|wheel_dist|std_msgs.msg/Float32|車輪間距離[mm]|| 
|coordinates|geometry_msgs.msg/Point|座標データ[mm]|このパッケージのノードではzを不使用| 
|velocities|std_msgs.msg/Float32MultiArray|車輪速度[mm/s]|data[0]が右<br>data[1]が左| 

## 使用の際の注意点
- inkinematicsは制御周期ごとにcoordinates内のメッセージが外部ノードによってパブリッシュされることを前提として作成されています。
- odometryは制御周期ごとにvelocities内のメッセージが外部ノードによってパブリッシュされることを前提として作成されています。
- このパッケージのノードはロボットの初期位置(0,0)・初期姿勢ｘ軸正の方向であるものとして計算されています。
## 必要なソフトウェア
- Python
- ROS2 Jazzy Jalisco
## 依存ライブラリ
- NumPy
## テスト環境
- Ubuntu 24.04 LTS

## ライセンス
- このROS2パッケージは、**三条項BSDライセンスの下**、再配布及び使用が許可されます。
- © 2025 Shogo Takizawa