#!/usr/bin/env mytrader
# -*- coding: utf-8 -*-
# Created by ZIJIA on 2021/10/15
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = np.arange(1, 7).reshape((3,2))
a_view = a[:2]
a_copy = a[:2].copy()

a_copy[1,1] = 0
print(a)
"""
[[1 2]
 [3 4]
 [5 6]]
"""

a_view[1,1] = 0
print(a)
"""
[[1 2]
 [3 0]
 [5 6]]
"""
a = np.zeros((1000, 1000))
b = np.zeros((1000, 1000))
N = 9999

def f1(a):
    for _ in range(N):
        a *= 2           # same as a[:] *= 2

def f2(b):
    for _ in range(N):
        b = 2*b
t0 = time.time()
f1(a)
t1 = time.time()
f2(b)
t2 = time.time()
print('%f' % ((t1-t0)/N))     # f1: 0.000837
print('%f' % ((t2-t1)/N))     # f2: 0.001346
def f1(a):
    for _ in range(N):
        a.flatten()

def f2(b):
    for _ in range(N):
        b.ravel()
t0 = time.time()
f1(a)
t1 = time.time()
f2(b)
t2 = time.time()
print('%f' % ((t1-t0)/N))    # 0.001059
print('%f' % ((t2-t1)/N))    # 0.000000