#!/usr/bin/python
# -*- coding: utf-8 -*-

fin=open("test.py","r")
lines=fin.readlines()
fin.close()

#it works only with #...
for line in lines:
	if "#" in line:
		#Starts with "#";
		l=line.strip()
		if l[0]!="#": #If yes we ignore it
			#Split the line with #
			tmp=line.split("#")
			#Count ', ''
			a1=tmp[0].count("'")
			a2=tmp[0].count('"')
			#if the number is odd
			# # is in alphanumeric
			if a1%2==1 or a2%2==1:
				print line
			else:
				print line.split("#")[0]
	else:
		print line
