# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:33:23 2020

@author: chiru
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
panda=misc.face()
plt.imshow(panda)
plt.show
# fd=np.flipud(panda)
# plt.imshow(fd)
# plt.show
fr=np.flip(panda)
plt.imshow(fr)
plt.show
