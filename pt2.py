# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:50:38 2024

@author: YenTrinh
"""
print("Phương trình bậc hai")
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
if a==1:
    print("Phương trình bậc hai có dạng: X^2 + ",b,"X + ",c)
    if b==1:
        print("Phương trình bậc hai có dạng: X^2 + X + ",c)
else:
    print("Phương trình bậc hai có dạng: ",a,"X^2 + ",b,"X + ",c)
if a==0:
    print("Phương trình bậc hai có dạng: X + ",c)
    if b==0:
        print("Phương trình bậc hai có dạng: ",c)
        


