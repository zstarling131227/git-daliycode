# !/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import time


iRandom = []
listRandom = []


def main():
    n1 = random.randint(0, 60)
    n2 = random.randint(0, 60)
    n3 = random.randint(0, 60)
    n4 = random.randint(0, 60)
    n5 = random.randint(0, 60)
    n6 = random.randint(0, 60)
    n7 = random.randint(0, 60)
    n8 = random.randint(0, 60)
    n9 = random.randint(0, 60)
    n10 = random.randint(0, 60)
    if (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) == 60:
        listRandom = n1, n2, n3, n4, n5, n6, n7, n8, n9, n10
        iRandom.append(listRandom)
        print(iRandom)
    else:
        print('no')


def do_while():
    while True:
        main()
        time.sleep(0.0000001)


do_while()