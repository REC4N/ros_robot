# ECE 5730 - Robotics
## Authors: Edgar A. Recancoj and Colten Eden
## Date: December 15, 2021

---

This repository contains all the code necessary to make a robot follow an apriltag using Ros 1 and Python. When downloading the repo (when using git clone), be sure to source the distribution of Ros 1 in your computer (this code was tested on Ros melodic) and source the devel/setup.bash file before executing.
To execute the program, type on the `ros_ws` the following: `roslaunch ros_robot robot.launch`. This command automates the launch of all the modules required for the robot to work.

The `src` folder of this repo contains all the source code necessary to compile the project. If changes are made to this folder, always make sure to compile using `catkin_make`.
The `rviz_images` folder contains images demonstrating how the robot is simulated using rviz. The `devel` folder contains things necessary for the robot to execute. Always make sure to execute `. devel/setup.bash` before running the robot for the first time.

Additionally, the schematics pdf shows the wiring diagram of the robot, in case modifications or additions need to be made. Lastly, see the `frames.pdf` file to visualize the transform tree.
