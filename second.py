# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:13:46 2024

@author: YenTrinh
"""

print("Đổi ra giây")
h=int(input("Nhập giờ: "))
m=int(input("Nhập phút: "))
s=int(input("Nhập giây: "))
giay= h*60*60 + m*60 +s
print(h,":",m,":",s," = ",giay,"giây")