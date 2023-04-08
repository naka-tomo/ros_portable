# ROS for Windows and Mac

Mac, Windowsでの，ROSの最小限の実行環境

## インストール
- リポジトリのclone
  ```
  git clone https://github.com/naka-tomo/ros_portable.git
  ```
- 依存モジュールのインストール
  ```
  pip install defusedxml
  pip install pyyaml
  pip install pyparsing
  ```

## 設定方法
- IPの設定  
  `setup.sh`または`setup.bat`の`ROS_MASTER_URI`と`ROS_HOSTNAME`を書き換える

- 設定の反映
  - Macの場合: ターミナルで以下を実行，または設定ファイル（`.bashrc`や`.zshrc`）に追加する（追加した場合は，ターミナル起動時に自動的に実行されるので，手動で実行する必要はない）
  ```
  source (cloneしたパス)/setup.sh
  ```
  - Windowsの場合: コマンドプロンプトで以下を実行
  ```
  (cloneしたパス)/setup.bat
  ```

## 使い方
`setup.sh`または`setup.bat`を実行したターミナル・コマンドプロンプトでROSの通信機能とコマンドが利用可能
### 通信機能
- roscoreの起動: `roscore`  
- message, service, action, rosparamが使用可能．使い方の詳細は[example](example)を参照．

### コマンド
- rosnode, rosparam, rosservice, rostopicの一部機能を実行可能
