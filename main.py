#!/usr/bin/python3

# This program generates N virtual rolls upon starting. Each roll will spin for N times  and 'play' a random mantra 
# from mantras.txt
import os
import random as r
import tkinter as tk

# rolls
rolls = r.randint(1,10)
spins = r.randint(50,200)

# mantras
my_file = open ("mantras.txt","r")
content = my_file.read()
mantras_list = content.split(";")
my_file.close()


class ManiWheel:
    """ A simple class to generate wheels """
    def __init__(self):
        self.rolls = rolls
        self.spins = spins
        self.mantra = r.choice(mantras_list)

test = ManiWheel()

for i in range (1,test.rolls):
    for e in range (1,test.spins):
        print(test.mantra)


print ("Chanted" ) 
print (rolls*spins)
print ("times")

