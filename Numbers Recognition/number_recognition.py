# -*- coding: utf-8 -*-
import numpy as np 
import re


input_file = "all-OANC.txt"

list_of_number_names = ['one',' two',' three',' four',' five',' six',' seven',' eight',' nine',' ten',' eleven',' twelve',
                        ' thirteen',' fourteen',' fifteen',' sixteen',' seventeen',' eighteen',' nineteen',' twenty',' thirty',
                        ' forty',' fifty',' sixty',' seventy',' eighty',' ninety',' hundred',' thousand',' million',' billion',' trillion']


single_number_names = ['one',' two',' three',' four',' five',' six',' seven',' eight',' nine']
double_number_names = [' ten',' eleven','twelve',
                       ' thirteen',' fourteen',' fifteen',' sixteen',' seventeen',' eighteen',' nineteen',' twenty',' thirty',
                        ' forty',' fifty',' sixty',' seventy',' eighty',' ninety']
large_number_names = [' hundred',' thousand',' million',' billion',' trillion']


def word_find(line,words):
    return list(set(line.strip().split()) & set(words))


finding = []
def main():
    with open("all-OANC.txt", "r", encoding="UTF-8") as instream:
        
        
        # for each in list_of_number_names:
        #     finding = re.findall("million", str(instream))
        #     print(finding)
        
        
        
        #for count, line in enumerate(instream):
            
        
        for line in instream:
            finding = re.findall("[0-9]+", str(line))
            if len(finding) != 0:
                print(finding)
            
            for each in single_number_names:     
                for count, name in enumerate(large_number_names):
                    finding = re.findall(name + each, str(line))
                    if len(finding) != 0:
                        print(finding)
                    
            for each in double_number_names:
                finding = re.findall(each, str(line))
                if len(finding) != 0:
                    print(finding)
                for count, name in enumerate(single_number_names):
                    finding = re.findall(each + name, str(line))
                    if len(finding) != 0:
                        print(finding)
            
            for each in large_number_names:
                finding = re.findall("[0-9]+" + each, str(line))
                if len(finding) != 0:
                    print(finding)
            
            
        #    for word in line.split():
         #       if word == "million":
          #          print(word) 
                
        
        
        
    return()


main()