#!/bin/python


def percentageGC(dnasequence):
    realbase = "ATCG"
    def validitycheck(dnasequence):   
        for base in dnasequence: ## A function inside a nother function, though 
            #allowed is not correct in this case -1, seoarate them
            if base not in realbase:
                return ("This is an invalid dna") #CK: this should return true or false so that you can reuse
        for data in dnasequence: #CK This loop here is useless, not required -1
            validitycheck(dnasequence)
            Gs=(dnasequence.count("G"))
            Cs=(dnasequence.count("C"))
            length=len(dnasequence)
            GC_content =((Gs + Cs) / length *100)
            return GC_content ## CK: 
 #CK: You need a return value here   
percentageGC(input ("paste DNA sequence:"))

print("The GC content of your DNA is %.2f" %(GC_content)) ##CK GC_content is local to your function, you have to assign
# the output to a new variable -2


