'''
Created on 17-Jul-2017

@author: Sanjana
'''
import collections
from pip._vendor.distlib.compat import raw_input

def getMaxOccuringChar(str):
    a=collections.Counter(str).most_common(3)
    b=[]
    for i in range(len(a)):
        k=a[i][0]
        b.append(k)
    return b

str = raw_input().strip('\'')

print (getMaxOccuringChar(str))