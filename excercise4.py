#!/bin/python


def percentageGC(dnasequence):
    realbase = "ATCG"
    def validitycheck(dnasequence):   
        for base in dnasequence:
            if base not in realbase:
                return ("This is an invalid dna")
        for data in dnasequence:
            validitycheck(dnasequence)
            Gs=(dnasequence.count("G"))
            Cs=(dnasequence.count("C"))
            length=len(dnasequence)
            GC_content =((Gs + Cs) / length *100)
        return GC_content
    
percentageGC(input ("paste DNA sequence:"))

print("The GC content of your DNA is %.2f" %(GC_content))


