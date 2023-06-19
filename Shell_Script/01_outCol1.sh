#! /bin/bash
inFile="./input/01_input.txt"
outFile="./output/01_output.txt"

awk '{print $1}' ${inFile} |
sed '/^[[:space:]]*$/d' > ${outFile}
cat ${outFile}