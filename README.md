# publisher_tutorial
--- ---

publisherの基本的な使い方について学ぶ。

## セットアップ
- rosのインストール → [install_ros_kinetic.sh](https://gitlab.com/TeamSOBITS/sobits-setup/blob/master/install_sh/install_ros_kinetic.sh)
- workspaceの作成の方法 → [install_catkin_ws.sh](https://gitlab.com/TeamSOBITS/sobits-setup/blob/master/install_sh/install_catkin_ws.sh)

## パッケージのクローン

```
cd catkin_ws/src

git clone https://github.com/KoutaOhishi/ros_publisher_tutorial.git

cd ros_publisher_tutorial/src

chmod 755 *

cd ~/catkin_ws/

catkin_make
```

## Dummy_LEDの起動
すべての端末をすべて切った後、
```
roslaunch publisher_tutorial dummy_led.launch
```
を実行する。


![](/img/dummy_led.png) ←これが出てくればOK  


## topicの確認
別の端末を起動させ、  
```
rostopic list
```
と打つと、  
``` .termial
/publisher_tutorial/led_color
/publisher_tutorial/led_on
/rosout
/rosout_agg
```
が表示される。

それぞれのトピックの型は、
- /publisher_tutorial/led_on : [std_msgs/Bool]
- /publisher_tutorial/led_color : [std_msgs/String]




## 端末からtopicをpublishする
- /publisher_tutorial/led_on (LEDのON/OFFを制御)
  ```
  rostopic pub /publisher_tutorial/led_on std_msgs/Bool "data: false" #LEDが消える

  rostopic pub /publisher_tutorial/led_on std_msgs/Bool "data: true" #LEDが付く
  ```

- /publisher_tutorial/led_color (LEDの色を制御)
  ```
  rostopic pub /publisher_tutorial/led_color std_msgs/String "data: 'Blue'"

  rostopic pub /publisher_tutorial/led_color std_msgs/String "data: 'Yellow'"
  ```

## 課題
pythonやc++でtopicをpublishできるようになろう！  
ただpublishするだけだと面白くないので、ちょっとした処理を加えてください。  
publisher_tutorial/src/の中にサンプルプログラムがあるので参考にしてください。

- Lチカさせてみよう  
  ![](/img/flashing.gif)  

- キー入力で色を変えれるようにしよう  
  ![](/img/color_change.gif)

### C++を使う際の注意点

c++のファイルを追加する場合は、CMakeList.txtの末尾に以下を加える  
```
# 名前は適宜変更してください。
add_executable({node_name} src/{file_name}.cpp)
target_link_libraries({node_name} ${catkin_LIBRARIES})
```
