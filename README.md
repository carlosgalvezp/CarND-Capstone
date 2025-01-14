Self-Driving Car Nanodegree Capstone Project [![Build Status](https://travis-ci.org/CarND-EuroBots/CarND-Capstone.svg?branch=master)](https://travis-ci.org/CarND-EuroBots/CarND-Capstone)
============================================
This is the project repo for the final project of the Udacity Self-Driving Car Nanodegree: Programming a Real Self-Driving Car. For more information about the project, see the project introduction [here](https://classroom.udacity.com/nanodegrees/nd013/parts/6047fe34-d93c-4f50-8336-b70ef10cb4b2/modules/e1a23b06-329a-4684-a717-ad476f0d8dff/lessons/462c933d-9f24-42d3-8bdc-a08a5fc866e4/concepts/5ab4b122-83e6-436d-850f-9f4d26627fd9).

### Team Members

|   Name                        |   Udacity account email            |
|-------------------------------|------------------------------------|
| Carlos Galvez (**Team Lead**) | carlosgalvezp (at) gmail.com       |
| Marko Sarkanj                 | marko.sarkanj (at) gmail.com       |
| Oren Meiri                    | oren.meiri (at) gmail.com          |
| Ivan Danov                    | ivan.geo.danov (at) gmail.com      |

### In-car video

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/RJEDSU22D3Y/0.jpg)](https://www.youtube.com/watch?v=RJEDSU22D3Y)

### Simulator Video

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/QFi0pbq8Zkc/0.jpg)](http://www.youtube.com/watch?v=QFi0pbq8Zkc)

### Quick setup using Docker

Follow these steps to setup the development/runtime environment
without having to install any dependencies, except for Docker.
NOTE: currently supported only on Linux and OSX.

* Install dependencies:

  - [docker](https://docs.docker.com/engine/installation).
  - [nvidia-docker](https://github.com/NVIDIA/nvidia-docker#ubuntu-distributions).
    Only supported on Ubuntu, to get GPU acceleration.

* Build and run code on simulator (CPU only):

      $ ./run.py

* Build and run code on simulator, with GPU acceleration (Ubuntu only):

      $ ./run.py --gpu

* Build and run code using a `rosbag`:

      $ ./run.py --rosbag <path_to_rosbag>

* Build and run code on Carla (GPU always enabled, Ubuntu only):

      $ ./run.py --carla


### Native installation

Follow these steps to have a native installation (only supported on Ubuntu).

* Be sure that your workstation is running Ubuntu 16.04 Xenial Xerus or Ubuntu 14.04 Trusty Tahir. [Ubuntu downloads can be found here](https://www.ubuntu.com/download/desktop). 
* If using a Virtual Machine to install Ubuntu, use the following configuration as minimum:
  * 2 CPU
  * 2 GB system memory
  * 25 GB of free hard drive space
  
  The Udacity provided virtual machine has ROS and Dataspeed DBW already installed, so you can skip the next two steps if you are using this.

* Follow these instructions to install ROS
  * [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) if you have Ubuntu 16.04.
  * [ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu) if you have Ubuntu 14.04.
* [Dataspeed DBW](https://bitbucket.org/DataspeedInc/dbw_mkz_ros)
  * Use this option to install the SDK on a workstation that already has ROS installed: [One Line SDK Install (binary)](https://bitbucket.org/DataspeedInc/dbw_mkz_ros/src/81e63fcc335d7b64139d7482017d6a97b405e250/ROS_SETUP.md?fileviewer=file-view-default)
* Download the [Udacity Simulator](https://github.com/udacity/CarND-Capstone/releases/tag/v1.2).

### Usage

1. Clone the project repository
```bash
git clone https://github.com/udacity/CarND-Capstone.git
```

2. Install python dependencies
```bash
cd CarND-Capstone
pip install -r requirements.txt
```
3. Make and run styx
```bash
cd ros
catkin_make
source devel/setup.sh
roslaunch launch/styx.launch
```
4. Run the simulator

### Real world testing
1. Download [training bag](https://drive.google.com/file/d/0B2_h37bMVw3iYkdJTlRSUlJIamM/view?usp=sharing) that was recorded on the Udacity self-driving car (a bag demonstraing the correct predictions in autonomous mode can be found [here](https://drive.google.com/open?id=0B2_h37bMVw3iT0ZEdlF4N01QbHc)) 
2. Unzip the file
```bash
unzip traffic_light_bag_files.zip
```
3. Play the bag file
```bash
rosbag play -l traffic_light_bag_files/loop_with_traffic_light.bag
```
4. Launch your project in site mode
```bash
cd CarND-Capstone/ros
roslaunch launch/site.launch
```
5. Confirm that traffic light detection works on real life images
