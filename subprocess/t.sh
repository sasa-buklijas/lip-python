#!/bin/sh

# wait 5 seconds
echo 'Wait from ./t.sh'
sleep 1500;
echo 'Wait DONE'

# make file from first argument
touch $1
