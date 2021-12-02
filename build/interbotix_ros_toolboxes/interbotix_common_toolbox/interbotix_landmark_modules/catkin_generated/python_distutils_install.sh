#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/robotics/ros_ws/src/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_landmark_modules"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/robotics/ros_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/robotics/ros_ws/install/lib/python2.7/dist-packages:/home/robotics/ros_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/robotics/ros_ws/build" \
    "/usr/bin/python2" \
    "/home/robotics/ros_ws/src/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_landmark_modules/setup.py" \
     \
    build --build-base "/home/robotics/ros_ws/build/interbotix_ros_toolboxes/interbotix_common_toolbox/interbotix_landmark_modules" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/robotics/ros_ws/install" --install-scripts="/home/robotics/ros_ws/install/bin"
