#!/usr/bin/env mytrader
# -*- coding: utf-8 -*-
# Created by ZIJIA on 2021/10/15


d=float(input('Please enter what is your initial balance: \n'))
p=float(input('Please input what is the interest rate (as a number): \n'))
d=float(d+d*(p/100))
year=1
while year<=5:
    d=float(d+d*p/100)
    print('Your new balance after year:',year,'is',d)
    year=year+1
print('your final year is',d)