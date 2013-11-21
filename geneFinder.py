#!/usr/bin/pypy

#Author: Nathan Perry
#Description:

from readFastaFile import *
from collections import namedtuple

GeneInfo = namedtuple("GeneStruct", "startPos length contigId")
def findPotentialGenes(pos, neg):
	"""Searches all three reading frames for items that 'look like' genes.
	Records the data in seperate structures depending on if found on positive
	or negative strand."""
	return geneSearch(pos), geneSearch(neg)

def geneSearch(strand):
	"""Takes a positive or negative strand and return potential genes"""
	genes = []
	for frameNo in range(0,3):
		num = 0 #number of genes found on this strand

		#loop over every contig in the strand
		for key,value in strand.items():
			#record the starting pos of the strand
			startPos = frameNo; #starting position of potential gene

			while(startPos < len(value)-3):
				codon = value[startPos:startPos+3]
				if(codon == "atg"):
					gene = []
					geneStart = nextCodon = startPos

					while geneStart < len(value)-2:
						currCodon = value[nextCodon:nextCodon+3]

						if(currCodon == "taa") or currCodon == "tag" or currCodon == "tga":
							gene.append(currCodon)
							break;
						else:
							gene.append(currCodon)
							nextCodon += 3

					if(len(gene)*3 >= 99 and len(gene)*3 <= 1500):
						contigid = key
						length = len(gene)*3
						genes.append(GeneInfo(length, contigid, geneStart))
						num += 1
						startPos += length
						continue
				startPos += 3

		return genes


temp = read_fasta_file("text.txt")
revTemp = reverseFasta(temp)
findPotentialGenes(temp, revTemp)