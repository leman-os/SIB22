#!/bin/bash -
list=$(ls -A)
cnt=0
for i in $list
	do
		let "(cnt++)"
	done
echo $list
echo "Total:"$cnt
