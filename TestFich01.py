# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:47:55 2024

@author: Sensei
"""
print("f(x) = x2 + y")

print("saisir ")

x = int(input(" x : "))
y = int(input(" y : "))

result = lambda x, y: x**2 +y

#result = f(x)
print("f(x) = " + str(result(x, y)))
#print("f(x) = ")
 
