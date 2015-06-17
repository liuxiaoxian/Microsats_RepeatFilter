#!/usr/bin/env python

## Pick unique SSR loci##

Usage="""RepeatFilter_step1.py INPUT FILE_INDEX"""

import sys

if len(sys.argv) < 2:
	print Usage

else:
  InFileName = sys.argv[1] #MISA output
	file_index = sys.argv[2] #e.g. species name
	OutFileName1 = file_index + ".repeat.txt"
	OutFileName2 = file_index + ".uniq.txt"  #output

	WriteOutFile = True
	InFile =open(InFileName, 'r')
	
	if WriteOutFile:
	  OutFile1 = open(OutFileName1, 'w')
	  OutFile2 = open(OutFileName2, 'w')

	
	lociDict = dict()
	LineNumber = 0
	
	primerList=[]
	
	for Line in InFile:
	  if LineNumber ==0:
	    OutFile2.write(Line)
	    OutFile1.write(Line)
	 else:
	    Line=Line.strip('\n')
			ElementList = Line.split('\t')
			
			scaffoldID = str(ElementList[0])
			SSRnr = str(ElementList[1])
			
			THE_SSR= str(ElementList[3])
		
			primerF1=str(ElementList[7])
			primerR1=str(ElementList[10])
			
			if (primerF1 in primerList) or (primerR1 in primerList):
				OutFile1.write(Line+"\n")
			else:
				primerList.append(primerF1)
				primerList.append(primerR1)
				OutFile2.write(Line+"\n")
				
		LineNumber += 1
	
