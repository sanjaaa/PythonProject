'''
Created on 17-Jul-2017

@author: Sanjana
'''
import ast
import sys
from pip._vendor.distlib.compat import raw_input

k=ast.literal_eval(raw_input())
l=[]
for i in range(len(k)):
    
    i=k[i][1]
    l.append(i)
    

def print2Smallest(arr):
 
    # There should be atleast two elements
    arr_size = len(arr)
    first = second = 10000
    for i in range(0, arr_size):
 
        # If current element is smaller than first then
        # update both first and second
        if arr[i] <= first:
            second = first
            first = arr[i]
        # If arr[i] is in between first and second then
        # update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]
    if (second == 10000):
        print ("No second smallest element")
    else:
        return second
 
def printans(r,k):
    o=[]
    for i in range(len(k)):
        if k[i][1]==r:
            o.append(k[i][0])
    return o
r=print2Smallest(l)
o=printans(r,k)
print('[' + ', '.join(o) + ']')


