#!/bin/bash

cd ~/all/python/projects/dobble/images/
i=0
for filename in ~/all/python/projects/dobble/images/*; do
	new_name="img_$i"
	let i=$i+1 
	mv $filename $new_name
done

