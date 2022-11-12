# roslib

Python環境（Ubuntu, Mac, Windows）で，ROSで通信するための最低限のファイル

# インストール
- 依存モジュールのインストールと，リポジトリのclone
```
pip install rospkg
pip install catkin_pkg

cd
git clone https://github.com/naka-tomo/roslib.git
```

- cloneしたフォルダへパスを通す
  - Macの場合
  ```
  export PYTHONPATH="$HOME/roslib:$PYTHONPATH"
  ```
  - Windowsの場合
  ```
  set PYTHONPATH=%PYTHONPATH%;C:¥***¥roslib
  ```

- IPの設定
  - 環境変数を追加  
    - Macの場合
    ```
    export ROS_MASTER_URI=http://192.168.1.10:11311
    export ROS_HOSTNAME=192.168.1.11
    ```
    - Windowsの場合
    ```
    set ROS_MASTER_URI=http://192.168.1.10:11311
    set ROS_HOSTNAME=192.168.1.11
    ```
- またはPythonファイルのはじめに宣言  
  ```
  import os
  os.environ["ROS_MASTER_URI"] = "http://192.168.1.10:11311"
  os.environ["ROS_IP"] = "192.168.1.11"
  ```
