#!/usr/bin/pypy

#filename should be a .fasta file.
#fasta file should contents should look like
# >Description_of_sequence (recommended less than 80 characters)
# GenomicSequence(of A C T G's)
def read_fasta_file(filename):
    """Read fasta file into memory for faster access"""

    #local variable declarations
    key = ""
    desc2seq = {}

    #Open Fasta file for reading
    fastaFile = open(filename, 'r')

    #Read and store all genomic data in the Fasta file
    for line in fastaFile.readlines():
        if line[0:1] == '>':
            key = line[1:-1]
            desc2seq[key] = ""
        elif line[0:1] == '#':
            continue
        else:
            desc2seq[key] = line.strip()
    #Close the Fasta file
    fastaFile.close()

    return desc2seq

def reverseFasta(desc2seq):
    """Negate  a strand of genomic data"""

    #local variables
    reverse = ""
    rev_desc2seq = {}

    #pull out all genome data, reverse the strand data
    for key, value in desc2seq.items():
        reverse = list(value[::-1])
        #convert genomic data to negative
        for i, char in enumerate(reverse):
            if char == 'a':
                reverse[i] = 't'
            elif char == 't':
                reverse[i] = 'a'
            elif char == 'c':
                reverse[i] = 'g'
            elif char == 'g':
                reverse[i] = 'c'

        rev_desc2seq[key] = ''.join(reverse)

    return rev_desc2seq

#test code to make sure functions work
#temp = read_fasta_file("text.txt")
#revTemp = reverseFasta(temp)
#print temp
#print revTemp
