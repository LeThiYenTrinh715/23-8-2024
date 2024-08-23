# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:15:23 2024

@author: YenTrinh
"""
print("Tinh tong cac chu so ")
a=int(input("Nhap a: "))
if a>=10 and a<=100:
    t=(a%10) + (a//10)
    print("Tong cac chu so cua ",a, "la: ",t)
