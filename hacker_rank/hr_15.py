#!/bin/python3

import math
import os
import random
import re
import sys


def task(value):
    n=value
    if n>=1 and n<=100:
        if (n%2 == 0 ):
            if (n>=2 or n<=5):
                print("Not Weird")
            elif (n >=6 or n<=20):
                # NOTE, when n=20, expected Weird
                print("Weird")
            elif (n>20):
                print("Not Weird")
        else:
            print("Weird")  
             
if __name__ == '__main__':
    n = abs(int(input()))
    #task(n)
    if n % 2 == 0:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")
