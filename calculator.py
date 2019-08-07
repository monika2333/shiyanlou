#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import sys

class Args:
    self.c = sys.argv[sys.argv.index('-c')+1]
    self.d = sys.argv[sys.argv.index('-d')+1]
    self.o = sys.argv[sys.argv.index('-o')+1]

class Config:
    def __init__(self, configfile):
        d = {}
        d['bili'] = 0
        with open(configfile) as f:
            for i in f:
                name,value = i.split(' = ')
            if float(value)<1:
                d['bili'] += float(value)
            else:
                d[name] = float(value)

    def get_config(self):
        return d[self]

class UserData:
    def __init__(self, userdatafile):
        userlist = {}
        with open(userdatafile) as f:
            data = list(csv.reader(f))
            for i in data:
                num,income_string = data.split(',')
            income = float(income_string)
            userlist.append((num,income))

class Calculator:
    def cal(self):
        for i in u:
            
        return 







if __name__ == '__main__':   #打印Args类的实例的属性值
    args = Args()
    print(args.c)
    print(args.d)
    print(args.o)
