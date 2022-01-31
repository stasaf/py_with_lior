#!/bin/bash

for j in `seq 1 3`
do
	ssss="{
	  \"externalUsers\": ["
	  
	for ((i=1; i<=10; i++))
	do
		if(($i == 10))
		then
			ssss+="\"psruser${i}\""
		else
			ssss+="\"psruser${i}\","
		fi
	done
	ssss+="],
	  \"ldapGroups\": [
		\"string\"
	  ],
	  \"name\": \"group${j}\"
	}"
	echo $ssss > file4
	curl -X POST "http://localhost:28080/groups?dataArrivedFromZookeeperServer=false" -H "accept: application/json" -H "Content-Type: application/json" -d @file4
done
