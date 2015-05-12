import sys
import csv

filename = sys.argv[1]

raw = open(filename,'r')

for line in raw:
    record = line.split('\t')
    key = record[0]
    authors = record[3]
    for author in authors.split('; '):
    	print key, author

raw.close()
