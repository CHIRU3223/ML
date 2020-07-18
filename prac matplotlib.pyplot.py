# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:05:18 2020

@author: chiru
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(['sin','cosindqawde'])
plt.show


plt.subplot(2,1,1)
plt.plot(x,y1)
plt.title('sine')
plt.subplot(2,1,2)
plt.plot(x,y2)
plt.title('cosine')
plt.show