#!/usr/bin/env python
from __future__ import print_function
from sys import platform
import os
import subprocess
import argparse
import psutil

ROOT = os.path.dirname(os.path.abspath(__file__))

def build_code():
    """ Builds the code """
    print('Building the code...')
    subprocess.check_call([os.path.join(ROOT, 'build.sh')])

def is_simulator_running():
    """ Checks whether the simulator is running or not.
        Currently supported on Linux and OSX only """
    # Get simulator process name
    if platform.startswith('linux'):  # Linux
        simulator_p_name = 'system_integrat'
    elif platform.startswith('darwin'):  # OSX
        simulator_p_name = 'mac_sys_int'
    else:
        raise Exception('Unsupported platform: {}'.format(platform))

    # Loop over processes and see if they match
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name().startswith(simulator_p_name):
            return True

    return False

def maybe_launch_simulator():
    """ Launches the simulator, if it is not already running """
    if is_simulator_running():
        print('Great, the simulator is already running!')
    else:
        print('Starting the simulator...')
        subprocess.call([os.path.join(ROOT, 'ros', 'src', 'styx',
                                            'unity_simulator_launcher.sh')])

def docker_network_configuration():
    if platform.startswith('linux'):
        return '--network=host'
    else:
        return '--publish=4567:4567'

def run(launch_file, gpu_enabled):
    """ Runs the ROS nodes
        Input: launch_file (string) launch file to run, to be found
               in the ros/launch folder. Additional arguments to the launch
               file are accepted.
               Example:
                   launch_file = site_bag.launch bag_file:=data/log.bag

               gpu_enabled (boolean) True if GPU support activated
    """
    if gpu_enabled:
        docker_cmd = 'nvidia-docker'
        docker_img = 'eurobots/carnd_capstone_gpu:latest'
    else:
        docker_cmd = 'docker'
        docker_img = 'eurobots/carnd_capstone:latest'

    subprocess.check_call(['docker', 'pull', docker_img])
    cmd = [docker_cmd, 'run', '--rm=true', '--tty=true', '--interactive=true',
           '--user={}:{}'.format(os.getuid(), os.getgid()),
           '--volume=/tmp:/.ros',
           '--volume={}:{}'.format(ROOT, ROOT),
           '--workdir={}'.format(ROOT),
           docker_network_configuration(),
           '--env=DISPLAY',
           '--volume=/tmp/.X11-unix:/tmp/.X11-unix',
           docker_img,
           '/bin/bash',
           '-c',
           'source /opt/ros/kinetic/setup.bash;'
           'source ros/devel/setup.bash;'
           'roslaunch ros/launch/{}'.format(launch_file)]

    try:
        subprocess.check_call(cmd)
    except Exception as e:
        print('Error executing:\n{}'.format(' '.join(cmd)))
        print(str(e))

def parse_arguments():
    """ Parses the arguments sent from command line
        Returns: a struct with the value of the arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--bag', dest='rosbag')
    parser.add_argument('-g', '--gpu', dest='gpu', action='store_true',
                        default=False)
    parser.add_argument('-c', '--carla', dest='carla', action='store_true',
                        default=False)

    return parser.parse_args()

def main():
    """ Main function """
    # Parse arguments
    args = parse_arguments()

    # Build code
    build_code()

    # Select launch file
    if args.rosbag:
        rosbag_full_path = os.path.abspath(args.rosbag)
        launch_file = 'site_bag.launch bag_file:={}'.format(rosbag_full_path)
    elif args.carla:
        launch_file = 'site.launch'
        args.gpu = True  # GPU available in Carla
    else:
        launch_file = 'styx.launch'
        maybe_launch_simulator()

    # Run the code
    run(launch_file, args.gpu)
    return 0

if __name__ == "__main__":
    exit(main())
