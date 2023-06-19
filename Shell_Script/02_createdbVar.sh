#! /bin/bash
inFile="./output/01_output.txt"
outFile="./output/02_output.txt"

awk '{print "self."$1" = @"$1"@"}' ${inFile} | 
sed "s/@/\"/g" > ${outFile}