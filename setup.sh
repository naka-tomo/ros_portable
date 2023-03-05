DIR=`dirname "$0"`
export PYTHONPATH="$DIR/commands:$DIR/python_package:$PYTHONPATH"
export PATH=$DIR/commands:$PATH

alias rosservice="python $DIR/commands/rosservice.py"
alias rosnode="python $DIR/commands/rosnode.py"
alias rostopic="python $DIR/commands/rostopic.py"
alias rosparam="python $DIR/commands/rosparam.py"
alias roscore="python $DIR/commands/run_master.py"

export ROS_MASTER_URI=http://127.0.0.1:11311
export ROS_HOSTNAME=127.0.0.1