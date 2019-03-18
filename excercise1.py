#!/bin/python

#Question-1
trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

#Counting the different nucleotides and storing them to variables
As=(trna.count("A"))
Ts=(trna.count("T"))
Gs=(trna.count("G"))
Cs=(trna.count("C"))
length=len(trna)

#Calculating the AT and GC content in the trna
AT_content = (As + Ts) / length *100
GC_content = (Gs + Cs) / length *100

#Printing the results
print("The senquence is %i" % len(trna),"nucleotides long")
print("The AT content %.2f and the GC content is %.2f" %(AT_content, GC_content))


#Question-2
aa = "MNKMDLVADVAEKTDLSKAKATEVIDAVFA"
print("The first amino acid is", aa[0], ","  "the last is", aa[len(aa)-1], "and the fifth", aa[4], "in the sequence")


#Question-3
seq = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
print(seq)
seq.find("TCCGGA")
print("The first restriction site for the enzyme is from position", seq.find("TCCGGA"), "to position",\
     (seq.find("TCCGGA")) +(len("TCCGGA")))







