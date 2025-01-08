#!bin/bash

loc=`pwd`
cd `dirname $0`
python3 ../plot/ns2dview.py -c test1.csv -p temp1.pdf --cols 1 2 --header
python3 ../plot/ns2dview.py -c test2.csv -p temp2.pdf --sep \\s+ --legend " APR4, 1.4Ms at 0.001 yr" --cols 0 10 --header --labels r[km] T[K] --log
cd $loc