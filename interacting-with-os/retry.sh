#!/bin/bash

n=0
# To access the first command line argument
# similar to sys.argv[1]
command=$1

while ! $command && [ $n -le 5 ]; do
	sleep $n
	((n+=1))
	echo "Retry #$n"
done;
