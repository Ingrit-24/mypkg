# お絵かきロボット軌道計画＆シミュレーション
![test](https://github.com/Ingrit-24/mypkg/actions/workflows/test.yml/badge.svg)
##　デモの動かし方
```bash
$ cd ~/ros2_ws
$ colcon bulid
$ ros2 launch mypkg drowing_robot.launch.py
```
# complementノード
- calcurateノードはcoordinatesdata.csvに保存されたx-y座標データをスプライン補完し、complementというトピックにx-y座標データのメッセージを流します。
## ライセンス
- このROS2パッケージは、**三条項BSDライセンスの下**、再配布及び使用が許可されます。