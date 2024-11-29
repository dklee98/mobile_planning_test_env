# Dynamic object environment setting
## Examples
<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/user-attachments/assets/6b98cb17-9711-40b3-9588-d31ec25dcbdd" alt="map_1" width="45%" />
    <img src="https://github.com/user-attachments/assets/76c15e1d-d06e-46f0-97df-3d1639edd8b7" alt="map_2" width="45%" />
</div>

## Setup

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

1. ``animated_box.cc`` is for generating plugin. We can generates several ``*.cc``, and modify each waypoints.

2. ```Important```: we have to change every class name.

3. Add ```CMakeLists.txt```
   ```
    add_library(animated_box_map1_1 SHARED dynamic_obstacles/animated_box_map1_1.cc)
    target_link_libraries(animated_box_map1_1 ${GAZEBO_LIBRARIES})
   ```

4. "drc_practice_blue_cyclinder" is dynamic obstacles.

5. Add following tag to the ``model.sdf``.

    ```
        ...
        <static>1</static>
        <allow_auto_disable>1</allow_auto_disable>
        <plugin name='push_animate' filename='libanimated_box.so'/>
    </model>
    </sdf>
    ```

6. Can load dynamic models in ``map.world``
    ```
        <include>
            <uri>model://drc_practice_blue_cylinder</uri>      
            <name>blue_cylinder</name>
        </include>
    ```
7. If you want multiple models, please rename every model to avoid duplication error.

## Turtle bot
reference: turtlebot3 tutorial
```
# in ~/.bashrc
export TURTLEBOT3_MODEL=waffle # burger, waffle, waffle_pi
```

## Usage
```roslaunch mobile_planning_test_env world_setup.launch```
parameters
- map_name [map1, map2, map3] # map3 is static map
- world [map, map_dyn] # map_dyn is dynamic map

## Teleop
```rosrun mobile_planning_test_env teleop.py```

