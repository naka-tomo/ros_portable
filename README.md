# roslib

Python環境（Ubuntu, Mac, Windows）で，ROSで通信するための最低限のファイル

## インストール
- リポジトリのclone
  ```
  git clone https://github.com/naka-tomo/roslib.git
  ```
- 依存モジュールのインストール
  ```
  pip install defusedxml
  pip install pyyaml
  pip install pyparsing
  ```

## 設定方法
- cloneしたフォルダへパスを通す
  - Macの場合
  ```
  export PYTHONPATH="$HOME/roslib:$PYTHONPATH"
  ```
  - Windowsの場合
  ```
  set PYTHONPATH=%PYTHONPATH%;C:¥***¥roslib
  ```
  - またはスクリプトの上部でroslibへのパスを通す（Mac, Windows共通）
  ```
  import sys
  sys.path.append("../roslib")
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
  - またはPythonファイルのはじめに宣言（Mac, Windows共通）
    ```
    import os
    os.environ["ROS_MASTER_URI"] = "http://192.168.1.10:11311"
    os.environ["ROS_IP"] = "192.168.1.11"
    ```

## 使い方
### 通信機能
- ROS master (roscore)の起動
  ```
  cd roslib
  python python run_master.py
  ```
  
- message, service, action, rosparamが使用可能．使い方の詳細は[example](example)を参照．

### コマンド
- rosnode, rosparam, rosservice, rostopicの一部機能は，setupスクリプトを実行することでWindows, Macでも動作可能
  - Macの場合
    ```
    source (リポジトリのあるディレクトリ)/roslib/ros_command/setup.sh
    ```
  - Windowsの場合
    ```
    (リポジトリのあるディレクトリ)/roslib/ros_command/setup.bat
    ```
- IPの設定
  - Ros masterのIPは`(リポジトリのあるディレクトリ)/roslib/ros_command/set_ip.py`で指定する
    ```
    os.environ["ROS_MASTER_URI"] = "http://(ros masterのIP):11311"
    os.environ["ROS_IP"] = "(このPCのIP)"
    ```
  - 環境変数の値を参照する場合は，設定をコメントアウトする．
    ```
    # os.environ["ROS_MASTER_URI"] = "http://127.0.0.1:11311"
    # os.environ["ROS_IP"] = "127.0.0.1"
    ```
