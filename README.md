# dynamic object environment setting

```
$ cd ~/simulation_setup
$ mkdir build && cd build
$ cmake ..
$ make

$ cd ~/simulation_setup/dynamic_obstacles
$ echo "export GAZEBO_MODEL_PATH=$(pwd):$GAZEBO_MODEL_PATH" >> ~/.bashrc
$ source ~/.bashrc

$ cd ~/simulation_setup/build
$ echo "export GAZEBO_PLUGIN_PATH=$(pwd):$GAZEBO_PLUGIN_PATH" >> ~/.bashrc
$ source ~/.bashrc
```

## How to use dynamic world

animated_box.cc 는 플러그인 생성용! 여러개 생성하고, 각 waypoint 설정하면 됨.

class 이름은 매번 바꿔줘야함!

CMakeLists.txt에 적절히 추가할 것.

"drc_practice_blue_cyclinder" 는 동적 장애물로 가져온 모델.

model.sdf 안에 다음 tag 추가할 것.

```
        ...
        <static>1</static>
        <allow_auto_disable>1</allow_auto_disable>
        <plugin name='push_animate' filename='libanimated_box.so'/>
    </model>
</sdf>
```

원하는 map.world 들어가서, 아래처럼 모델 불러오면 됨
```
        <include>
            <uri>model://drc_practice_blue_cylinder</uri>      
            <name>blue_cylinder</name>
        </include>
```
여러개 불러올거면, 각 모델 복붙한 다음에 이름 안꼬이게 자알 설정하기.

## Turtle bot
turtlebot3 기본 예제 참고해서 필요한 패키지 설치해놓기
```
# in ~/.bashrc
export TURTLEBOT3_MODEL=waffle # burger, waffle, waffle_pi
```

## Simulation
```roslaunch mobile_planning_test_env world_setup.launch```
잘 모르겠는데 가제보 로딩 시간이 오래걸림.
모델 경로 확인해야할수도

## Teleop
```rosrun mobile_planning_test_env teleop.py```
기본코드라서 코드 수정이 필요할지도 모름.

