# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:30:52 2024

@author: YenTrinh
"""
print("Thực hiện phép tính")
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
import math
A=(math.sqrt(a)-math.sqrt(b))/(math.pow(a,0.25)-math.pow(b,0.25)) - (math.sqrt(a)+math.pow((a*b),0.25))/(math.pow(a,0.25)+math.pow(b,0.25))
print("Kết quả phép tính là", A)
