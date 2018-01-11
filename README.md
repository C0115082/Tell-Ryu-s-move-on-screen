

# Tell-Ryu-s-move-on-screen
ストリートファイターVにおける画像内のリュウの技を画像ポーズ認識を使い判断する

# Requirements
* Python 3.0+
* Chainer 2.0+
* NumPy
* Matplotlib
* OpenCV

# Preparation
このアプリケーションは[DeNA](https://github.com/DeNA)さん開発の
[Chainer_Realtime_Multi-Person_Pose_Estimation](https://github.com/DeNA/Chainer_Realtime_Multi-Person_Pose_Estimation)
を使用するのでまずこちらの導入をお願いします。

導入が完了したら 
  
Tell-Ryu-s-move-on-screen  
  |  
  |--Chainer_Realtime_Multi-Person_Pose_Estimation  
  |--move-ungle-dates  
  |--pose-detecterKai.py  
  |--ungleGetter.py  
のようにファイルを配置

次に**pose-detecterKai.py**をChainer_Realtime_Multi-Person_Pose_Estimation内にコピー。
これで下準備は完了です。

# Test
認識したい画像を用意し以下のように実行  
`python ungleGetter.py sample.jpg`  
実行結果がsmall kickとなっていれば成功。

# Condition
当プログラムで使用できる対象は題目通りストリートファイターVにおけるリュウの通常技18種類のみであり、使用できる画像は映っている人物がリュウのみの場合です。  
ただしRyuMoveAngles.csvのような技の角度データを作成し、Chainer_Realtime_Multi-Person_Pose_Estimationが認識可能なものであればどんなものにも応用は可能です。  
ただ普通に精度良くないです。  
