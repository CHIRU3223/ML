# import numpy as np
# aa=np.array([[1,2,3],[4,5,6]])
# bb=np.array([[3,2],[4,5],[6,7]])

# cc=np.empty([3,3])
# # cc[0,1]=10
# for i in range(bb.shape[0]):
#     cc[i,:]=00
# print(cc)
# dd=np.arange(10,22).reshape((3,4))
# print(dd.shape[0])
# dd=np.tile(bb,(10,10))
# c=0
# for i in range(dd.shape[0]):
#     for j in range(dd.shape[1]):
#         if(dd[i,j]==3):
#             c+=1;
# print(c)
# # print(dd)
# v=np.array([10,10,10])
# vv=aa+v
# print(vv)
# v1=np.tile(v,(2,1))
# vv1=aa+v1
# print(vv1)
from scipy.special import exp10,cbrt
from scipy import linalg
import numpy as np
from matplotlib import pyplot as plt
# a=cbrt([27,64]);
# print(a)
# b=exp10([2,3])
# print(b)
# a=np.array([[2,3],[4,5]]);
# print((linalg.inv(a)))
n=5
n_samp=50
t=np.linspace(0,1,1000)
aa=np.sin(2*n*np.pi*t)
figure, axis=plt.subplots()
axis.plot(t,aa)
axis.set_xlabel("chchc")
axis.set_ylabel("y y ydsd")

from scipy import fftpack
f=fftpack.fftfreq(2)
print(f)



# n=10
# ns=100
# t=np.linspace(0, n,ns*1000,endpoint=False)
# aaa=np.tan(n*np.pi*t)
# figure,axis=plt.subplots()
# axis.plot(t,aaa)
# axis.set_xlabel("chiru")
# print(aaa)