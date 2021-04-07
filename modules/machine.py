#!/usr/env/python3
#coding:utf-8

def IdentityOfMachine(qct):
        if(qct[3] == 1):
                qct = 1
        if(qct[3] == 2):
                qct = 2
        if(qct[3] == 3):
                qct = 3

        return int(qct[3])
