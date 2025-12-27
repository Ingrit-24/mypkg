# お絵かきロボット軌道計画＆シミュレーション
![test](https://github.com/Ingrit-24/mypkg/actions/workflows/test.yml/badge.svg)

## パッケージ概要
- このROS2パッケージは二輪駆動の台車を任意の軌道で動かすための軌道計画及びシミュレーションを手助けするためのものです。
- パッケージ直下のcoordinatesdata.csvに制御周期ごとのX-Y座標を書き込みdataディレクトリ内のdrawing_robot.launch.pyを実行すると、シミュレーションが動きます。
- パッケージの構成は以下のようになっています。
```bash
mypkg
├── LICENCE
├── README.md
├── data
│   └── coordinatesdata.csv
├── launch
│   └── drawing_robot.launch.py
├── mypkg
│   ├── __init__.py
│   ├── calculate.py
│   ├── complement.py
│   └── odometry.py
├── package.xml
├── resource
│   └── mypkg
├── setup.cfg
├── setup.py
└── test
    ├── test.bash
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

## デモの動かし方
```bash
$ cd ~/ros2_ws
$ colcon build
$ . install/setup.bash
$ ros2 launch mypkg drawing_robot.launch.py
```
- ターミナルで上記のように実行すると下のようなシミュレーションが動き出します。初期状態のパッケージでは雪だるまが書けます。
![image](https://private-user-images.githubusercontent.com/238378492/530192869-4f002362-b620-4f25-a66d-f74665ea24fc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjY2NTk5OTYsIm5iZiI6MTc2NjY1OTY5NiwicGF0aCI6Ii8yMzgzNzg0OTIvNTMwMTkyODY5LTRmMDAyMzYyLWI2MjAtNGYyNS1hNjZkLWY3NDY2NWVhMjRmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMjI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTIyNVQxMDQ4MTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02OGVjYmRhMTU1NDA2ODFmNzVkMDc5MzMxOGJiOTllZGIxNzkyNjgwNjgzNzU2NjcyZmMyMGIwN2Y3NGQ4YjhkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.nUfEZaU4uK1NLfDxmNrDAt6t1_69Ijj2gqThrR26ErU)

## 各ノード・トピック概要
### complementノード
- complementノードはcoordinatesdata.csvに保存されたx-y座標データをスプライン補完により滑らかな軌道に変換し、complementトピックにx-y座標データのメッセージを流します。
### calculateノード
- calculateノードはcomplementトピックに流れるメッセージを受け取ります。受け取ったメッセージをもとに逆運動学を解き、ロボットの左右車輪速度を求めて、outputトピックに時刻と左右車輪速度のデータを流します。
### odometryノード
- odometryノードはoutputトピックに流れるメッセージを受け取り、データをターミナルに表示します。
```bash
[odometry-3] [INFO] [1766840125.699913951] [odometry]: |time:    0.10|VR:  105.94|VL:  104.37|
[odometry-3] [INFO] [1766840125.797276240] [odometry]: |time:    0.20|VR:  106.73|VL:  103.58|
[odometry-3] [INFO] [1766840125.844292783] [odometry]: |time:    0.30|VR:  106.73|VL:  103.58|
[odometry-3] [INFO] [1766840125.886361024] [odometry]: |time:    0.40|VR:  106.73|VL:  103.58|
[odometry-3] [INFO] [1766840125.928418837] [odometry]: |time:    0.50|VR:  106.73|VL:  103.58|

```
- また、受け取ったデータをもとに、ロボットの動きをシミュレーションします。

### complementトピック
- データ型はPoint。x-y-z座標のデータを流せますが、不要であるためｚは常に0になってます。
### outputトピック
- データ型はFloat32MultiArray。配列の番号が以下のように対応しています。
- array[0] = t [s] 時刻  　　
- array[1] = vr [mm/s]　右車輪速度 
- array[2] = vl [mm/s]　左車輪速度

## coordinatesdata.csvの形式
- coordinatesdata.csvには1列目にx座標、２列目にy座標を入れてください。
```csv
0.000000,0.000000
52.335956,1.370465
104.528463,5.478105
        .
        .
        .
```
## drawing_robot.launch.pyについて
- このlaunchファイルではすべてのノードを一斉に立ち上げることができます。
- launchファイルの中で以下の３つのパッケージ共通パラメータを設定しています。
  - 車輪間距離 
  - 制御周期  
  - デモ合計時間
```python
 6 robot_parameters={
 7    "wheel_dist": 130, #車輪間距離 [mm]
 8    "dt":0.1,          #制御周期   [s]
 9    "total_time": 120,  #デモ時間   [s]
10 }
```
## 必要なソフトウェア
- Python
- ROS2
## 依存ライブラリ
- NumPy
- SciPy
- Matplotlib

## テスト環境
- Ubuntu 24.04 LTS

## ライセンス
- このROS2パッケージは、**三条項BSDライセンスの下**、再配布及び使用が許可されます。
- © 2025 Shogo Takizawa