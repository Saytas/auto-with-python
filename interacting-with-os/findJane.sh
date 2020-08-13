#!/bin/bash


> oldFiles.txt

list=$(ls oldFiles.txt)

files=$(grep ' jane ' /home/student-02-46e2e5bdc29a/data/list.txt | cut -d' ' -f3)

for file in $files; do
	if test -e ..$file; then
		echo  ..$file >> oldFiles.txt
        fi
done



#!/bin/bash
#> oldFiles.txt
#files=$(grep " jane " ../data/list.txt | cut -d' ' -f3)
#for f in $files; do	
#  if [ -e $HOME$f ]; then
#    echo $HOME$f >> oldFiles.txt;
#  fi
#done



#echo $files

#for files in /home/student-02-46e2e5bdc29a/data; do
	#echo $files
#done
