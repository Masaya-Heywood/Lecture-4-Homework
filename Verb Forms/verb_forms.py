# -*- coding: utf-8 -*-
import numpy as np 
import re
import pandas as pd

rawData = pd.read_csv("verb_irreg.tsv", sep="\t")

rawData.drop("Unnamed: 4", axis = 1, inplace = True)

workingData = rawData[rawData.PAST.isnull()]

def main(workingData):
    replaceY = True
    normalEnd = True
    
    
    for index, row in workingData.iterrows():
        normalEnd = True
        replaceY = bool(re.findall(r"[bcdfghjklmnpqrstvwxyz]y$", str(row[0])))
        dropE = bool(re.search(r"e\b", str(row[0])))
        #replaceY = bool(row[0].endswith("[aeiou]y"))
        print(replaceY)
        
        
        if dropE == True:
            normalEnd = False
            splitWord = list(row[0])
            splitWord.pop()
            changeWord = "".join(splitWord)
            
            row[1] = str(changeWord + "ed")
            row[2] = str(changeWord + "ed")
            row[3] = str(changeWord + "ing")
        
        if replaceY == True:
            normalEnd = False
            splitWord = list(row[0])
            splitWord[-1] = "i"
            changeWord = "".join(splitWord)
            
            row[1] = str(changeWord + "ed")
            row[2] = str(changeWord + "ed")
            row[3] = str(changeWord + "ng")
        
        
        
        if normalEnd == True:
            row[1] = str(row[0] + "ed")
            row[2] = str(row[0] + "ed")
            row[3] = str(row[0] + "ing")
            #print(row)
        #row[0] + 
        
    return()


main(workingData)