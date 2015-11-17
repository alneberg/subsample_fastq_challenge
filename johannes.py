#!/usr/bin/env python
from numpy.random import choice
import gzip
import argparse
from Bio import SeqIO

def main(args):
    with gzip.open(args.fastq_R1) as f:
        for i,l in enumerate(f):
            pass
    input_length = (i+1)/4
    indices = choice(xrange(input_length), args.nr_reads, replace=False)
    indices.sort()

    j = 0
    max_j = len(indices)-1
    with gzip.open(args.fastq_R1) as f1, gzip.open(args.fastq_R2) as f2:
        with open(args.output_R1, 'w') as o1, open(args.output_R2, 'w') as o2:
            item = indices[j]
            for i, read_pair in enumerate(zip(fastq_iterator(f1), fastq_iterator(f2))):
                if i == item:
                    output_pair(read_pair, o1, o2)
                    if j == max_j:
                        return
                    j += 1
                    item = indices[j] 

def fastq_iterator(file_handle):
    rows = []
    for i, row in enumerate(file_handle):
        rows.append(row)
        if i % 4 == 3:
            yield rows
            rows = []

def output_pair(read_pair, o1, o2):
    r1, r2 = read_pair

    for r1_row in r1:
        o1.write(r1_row)
   
    for r2_row in r2:
        o2.write(r2_row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fastq_R1")
    parser.add_argument("fastq_R2")
    parser.add_argument("output_R1")
    parser.add_argument("output_R2")
    parser.add_argument("nr_reads", type=int)

    args = parser.parse_args()
    main(args)
