import os

# use following command to kill the bash process
#  kill `ps -ef | grep bash Test.sh | awk '{ print $2 }'`

os.system('nohup bash Test.sh &')

