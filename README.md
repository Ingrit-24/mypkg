# 二輪ロボットのためのパッケージ
![test](https://github.com/Ingrit-24/mypkg/actions/workflows/test.yml/badge.svg)
- このパッケージは二輪ロボットに関する,逆運動学・オドメトリの実行及び結果のグラフィカル表示を目的としたものです。

## 各ノード概要
| ノード名 | 処理内容 |入力トピック|出力トピック|<nobr>パラメータ</nobr>|
|:---:|:---:|:---|:---|:---|
|inkinematics|座標データから<br>左右車輪速度を求め<br>メッセージを流す|coordinates_inkine|velocities_inkine| delta_t <br> wheel_dist|
| graph_v | 速度データをグラフで表示 |velocities_inkine|無し|delta_t|
|odometry|左右車輪速度から<br>現在位置を推定し<br>メッセージを流す|velocities_odo|coordinates_odo|delta_t <br> wheel_dist|
| graph_c |  座標データからロボの軌跡を表示　|coordinates_odo|無し|delta_t|

## 各トピック概要
| トピック名 | データ型 | データの中身 | 注意点 |
|:---|:---|:---|:---| 
|coordinates_inkine|geometry_msgs.msg/Point|逆運動学用座標データ[mm]|msg.zを不使用| 
|velocities_inkine|std_msgs.msg/Float32MultiArray|逆運動学解　車輪速度[mm/s]|data[0]が右車輪<br>data[1]が左車輪| 
|coordinates_odo|geometry_msgs.msg/Point|オドメトリ結果[mm]|msg.zを不使用| 
|velocities_odo|std_msgs.msg/Float32MultiArray|オドメトリ用車輪速度[mm/s]|data[0]が右車輪<br>data[1]が左車輪| 

## 各パラメータ概要
| パラメータ名 | データ型　|データの中身 | 
|:---|:---|:---|
| delta_t | 浮動小数 |制御周期（メッセージ更新周期）[s]|
| wheel_dist | 浮動小数 | 車輪間距離　[mm]|
- このパッケージのノードを使用する際、実行時にパラメータを渡してください。

## ノードの連携について。
- 各ノードの連携の例は次のようなものです。
```bash
                                            graph_v
                                               ↑
　　　　　　　 ------------→ inkinematics ------------→
上位制御ノード　(座標データ)                (速度データ)  ロボット本体
　　　　　　　 ←------------   odometry   ←------------
                    ↓
                 graph_c
```

## 使用の際の注意点
- inkinematicsは制御周期ごとにcoordinates_inkine内のメッセージが外部ノードによってパブリッシュされることを前提として作成されています。
- odometryは制御周期ごとにvelocities_odo内のメッセージが外部ノードによってパブリッシュされることを前提として作成されています。
- このパッケージのノードはロボットの初期位置(0,0)・初期姿勢ｘ軸正の方向であるものとして計算されています。
## 必要なソフトウェア
- Python
- ROS2 Jazzy Jalisco
## 依存ライブラリ
- NumPy
- matplotlib
## テスト環境
- Ubuntu 24.04 LTS

## ライセンス
- このROS2パッケージは、**三条項BSDライセンスの下**、再配布及び使用が許可されます。
- © 2026 Shogo Takizawa