#-*- coding: utf-8 -*-
from array import *
import sys


num = {1:'१',2:'२',3:'३',4:'४',5:'५',6:'६',7:'७',8:'८',9:'९',0:'०'}
num_in = raw_input("Enter mar number")
s = []
p=0

for i in range(0,len(num_in)/3):
    #for j in range(0,len(num_in)/3):
        #for k in range(0,len(num_in)/3):
    v =  num_in[0+i*3] + num_in[1+i*3] + num_in[2+i*3]
    s.append(v)

#sys.stdout.write(s)
number = 0
for k in range(0,len(s)):
    for val in num:
        if s[k] == num[val]:
            number = number*10 + val
            #k=k+3
print number