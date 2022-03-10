"""infile and outfile Read and Write"""
import argparse
import re
import csv
import sys

parser = argparse.ArgumentParser()
parser.add_argument('infile', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('outfile', type=argparse.FileType('w'),
                    default=sys.stdout)

args = parser.parse_args()
csv_writer = csv.writer(args.outfile)
for row in csv.reader(args.infile):
    row[2] = re.sub(r'[a-zA-Z0-9]+','*****', row[2])
    csv_writer.writerow(row)
