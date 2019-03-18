#!/bin/python

#Question1
dna = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
nucleotides = list (dna)
D1 = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
complement = [D1[i] for i in nucleotides]
complement.reverse()
reverseComp = '' .join(complement)
print(reverseComp)