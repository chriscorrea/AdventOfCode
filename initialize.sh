#/bin/bash

year=`date | awk '{print $6}'`
day=1

echo "Initializing $year Advent of Code directories"

mkdir -p $year;
mkdir -p $year/inputs

while [ $day -le 25 ]
do
    mkdir -p $year/$day
    ((day++))

done
