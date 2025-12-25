# お絵かきロボット軌道計画＆シミュレーション
![test](https://github.com/Ingrit-24/mypkg/actions/workflows/test.yml/badge.svg)

## デモの動かし方
```bash
$ cd ~/ros2_ws
$ colcon bulid
$ ros2 launch mypkg drowing_robot.launch.py
```
- ターミナルで上記のように実行すると下のようなシミュレーションが動き出します。初期状態のパッケージでは雪だるまが書けます。
![image](https://private-user-images.githubusercontent.com/238378492/530192869-4f002362-b620-4f25-a66d-f74665ea24fc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjY2NTk5OTYsIm5iZiI6MTc2NjY1OTY5NiwicGF0aCI6Ii8yMzgzNzg0OTIvNTMwMTkyODY5LTRmMDAyMzYyLWI2MjAtNGYyNS1hNjZkLWY3NDY2NWVhMjRmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMjI1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTIyNVQxMDQ4MTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02OGVjYmRhMTU1NDA2ODFmNzVkMDc5MzMxOGJiOTllZGIxNzkyNjgwNjgzNzU2NjcyZmMyMGIwN2Y3NGQ4YjhkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.nUfEZaU4uK1NLfDxmNrDAt6t1_69Ijj2gqThrR26ErU)

## 各ノード・トピック概要
### complementノード
- complementノードはcoordinatesdata.csvに保存されたx-y座標データをスプライン補完により滑らかな軌道に変換し、complementトピックにx-y座標データのメッセージを流します。
### calcurateノード
- calcurateノードはcomplementトピックに流れるメッセージを受け取ります。受け取ったメッセージをもとに逆運動学を解き、ロボットの左右車輪速度を求めて、outputトピックに時刻と左右車輪速度のデータを流します。
### odometoryノード
- odometoryノードはoutputトピックに流れるメッセージを受け取り、データをターミナルに表示します。
```bash
[output-3] [INFO] [1766668105.887554044] [odometory]: time:0.5 VR:108.63478088378906 VL:100.78079986572266
[output-3] [INFO] [1766668106.374411712] [odometory]: time:1.0 VR:112.56177520751953 VL:96.85380554199219
[output-3] [INFO] [1766668106.873757591] [odometory]: time:1.5 VR:112.561767578125 VL:96.85381317138672
[output-3] [INFO] [1766668107.374408491] [odometory]: time:2.0 VR:112.56177520751953 VL:96.85381317138672
[output-3] [INFO] [1766668107.876147103] [odometory]: time:2.5 VR:112.56177520751953 VL:96.85381317138672
```
- また、受け取ったデータをもとに、ロボットの動きをシミュレーションします。
## ライセンス
- このROS2パッケージは、**三条項BSDライセンスの下**、再配布及び使用が許可されます。
- © 2025 Shogo Takizawa