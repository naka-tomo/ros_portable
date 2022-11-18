DIR=`dirname "$0"`
export PYTHONPATH="$DIR:$DIR/../:$PYTHONPATH"

alias rosservice="python $DIR/rosservice.py"
alias rosnode="python $DIR/rosnode.py"
alias rostopic="python $DIR/rostopic.py"
alias rosparam="python $DIR/rosparam.py"
