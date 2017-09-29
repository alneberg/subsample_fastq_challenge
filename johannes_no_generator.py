#!/usr/bin/env python
import random
import gzip
import argparse
import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def main(args):
    logging.info("Start parsing input file")
    with gzip.open(args.fastq_R1) as f:
        for i,l in enumerate(f):
            pass
    input_length = (i+1)/4
    logging.info("Input file length is {}".format(input_length))
    
    readNumbers2out = {}
    while len(readNumbers2out) < args.nr_reads:
        readNumbers2out[random.randint(0,input_length-1)] = True
    logging.info("Generated dictionary with random selection.")

    with gzip.open(args.fastq_R1) as f1, gzip.open(args.fastq_R2) as f2, \
            open(args.output_R1, 'w') as o1, open(args.output_R2, 'w') as o2:
        go = True
        while go:
            r1l1 = f1.readline()
            r1l2 = f1.readline()
            r1l3 = f1.readline()
            r1l4 = f1.readline()

            r2l1 = f2.readline()
            r2l2 = f2.readline()
            r2l3 = f2.readline()
            r2l4 = f2.readline()

            if r1l1 == "":
                go = False
                break

            output_pair(((r1l1,r1l2,r1l3,r1l4),(r2l1,r2l2,r2l3,r2l4)), o1, o2)
    logging.info("Printed all reads. Done!")
    
def fastq_iterator(file_handle):
    go = True
    while go:
        l1 = file_handle.readline()
        l2 = file_handle.readline()
        l3 = file_handle.readline()
        l4 = file_handle.readline()

        if l1 == "":
            go = False
            break
        yield l1,l2,l3,l4

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
