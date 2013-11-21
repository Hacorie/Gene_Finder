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
	genes = []	#hold all potential genes found
	for frameNo in range(0,3):
		#num = 0 #number of genes found on this strand

		#loop over every contig in the strand
		for key,value in strand.items():
			#start posisition of current strand data in correct reading frame
			startPos = frameNo;

			#loop over entire contig data
			while(startPos < len(value)-3):

				#pull out individual codon
				codon = value[startPos:startPos+3]

				#only accept atg as start codon for a gene
				if(codon == "atg"):
					gene = []	#holds potential gene

					#record where potential gene starts
					geneStart = nextCodon = startPos 

					#make sure not to exceed length of contig data
					while geneStart < len(value)-2:
						#update the current Codon
						currCodon = value[nextCodon:nextCodon+3]

						#accept "taa" "tag" and "tga" as the only possible gene stop codons
						if(currCodon == "taa") or currCodon == "tag" or currCodon == "tga":
							gene.append(currCodon)
							break; #potential gene found!
						else: #keep going if currCodon is not one of above
							gene.append(currCodon)
							nextCodon += 3

					#set some "bounds" on the possible length of a gene
					if(len(gene)*3 >= 99 and len(gene)*3 <= 1500):
						genes.append(GeneInfo(len(gene)*3, key, geneStart))
						#num += 1
						startPos += length #assume one gene is not inside another gene
						continue
				#update position of next codon
				startPos += 3

		return genes


temp = read_fasta_file("text.txt")
revTemp = reverseFasta(temp)
findPotentialGenes(temp, revTemp)