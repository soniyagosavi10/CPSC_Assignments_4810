#! /usr/bin/env bash
awk -F',' 'BEGIN{OFS=",";print "ArrDelay,Origin"} $17=="SFO" {print $15,$17}' 2007.csv | head -4 > firstsfo3.csv


