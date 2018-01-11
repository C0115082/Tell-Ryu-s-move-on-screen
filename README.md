

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
  |--pose-detecter.py  
  |--ungleGetter.py  
のようにファイルを配置

次に**pose-detecter.py**をChainer_Realtime_Multi-Person_Pose_Estimation内にコピー、上書き。
これで下準備は完了です。

# Test
認識したい画像を用意し以下のように実行  
`python ungleGetter.py 画像のパス`  
これにより用意した画像の比較用要素が取得できたので以下のように比較
