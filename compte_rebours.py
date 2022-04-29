# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:51:48 2022

@author: Barbera TSOKATI
"""

import time

def countdown(t):
    while t:
        mins, secs=divmod(t, 60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t-=1
        print('Timer completed')

t=input('entrer le temps en seconde')
countdown(int(t))


ligne = ["A","B","C"]
colonne = ["0","1","2"]
c=input("entrer un caractère")
while len(c) >2 :
    c=input("entrer un caractère")

while c[0] not in ligne or c[1] not in colonne:
    c=input("entrer un caractère")