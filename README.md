# slam_demo
Tested under *noetic*.


Needs https://github.com/tu-darmstadt-ros-pkg/hector_slam built from source in same workspace


# notes on using SICK microScan3
`sudo apt install ros-noetic-sick-safetyscanners`
set own ip to `192.168.0.50`
start driver with .. `roslaunch sick_safetyscanners sick_safetyscanners.launch sensor_ip:=192.168.0.220 host_ip:=192.168.0.50 port:=9990`