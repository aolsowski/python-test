#!/usr/bin/python
import sys

import os
#print os.listdir('./')

#a = os.popen('ls').read()
files = os.popen('ls -la').read().split('\n')
#print files
for elem in files[:-1]:
	print elem

#from __future__ import print_function
#
#a = [1, 2, 3]
#b = a
#c = a[:]
#for elem in a:
#	print (elem,end='')
#
#print ('')
#
#print str(a)
#print ''.join(map(str,a))
