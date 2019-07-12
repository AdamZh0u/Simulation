# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 09:58:36 2018

@author: zzz
"""
import numpy as np
from collections import Counter
import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

class indexCoor(list):
    def __init__(self,ls):
        self.extend(ls)

    def __getitem__(self, item):   # 实现切片
        #cls = type(self)    # 相当于cls=Group()  但软编程可维护性好
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            L = indexCoor([])
            for x in range(stop):
                if x>=start:
                    L.append(self[x])
            return L
        if isinstance(item,int):
            return list(self)[item]

    def nodeList(self):
        nodelist = {}
        for i in self:
            if i in nodelist:
                nodelist[i][7] +=1
            else:
                nodelist[i]={5:np.linalg.norm(np.array(i)-
                        np.array(self[0])),7:1}
        return nodelist

    def sideView(self):
        h = []
        nodelist = indexCoor.nodeList(self)
        for k in nodelist:
            h.append(nodelist[k][7])
        a = Counter(h)
        return a 

    def caculate(self,deltaR):
        #根据nodelist计算s曲线
        nodelist = indexCoor.nodeList(self)
        w = []
        delta = deltaR
    	#delta = radius/2#qqq
        for key in nodelist:
            w.append([nodelist[key][5],nodelist[key][7]])
        w.sort()
        w = np.array(w)
        R = np.arange(0,np.max(w[:,0]),delta)
        RL = np.zeros((len(R),2)) 
        RL[:,0] = R
        for i in range(len(RL)):
            RL[i,1] = np.sum(w[w[:,0]<RL[i,0],1])
            #RL delta*n 列是sum
        Rrho = np.zeros((len(R),2))
        Rrho[:,0] = R + delta/2
        for i in range(len(Rrho)-1):
            Rrho[i,1] = (RL[i+1,1] - RL[i,1])/(math.pi*(delta**2+2*delta*RL[i,0]))
        a = Rrho
        xx = np.nonzero(a[:,1]==0) 
        if len(xx[0])==0:
            x = 0 
        else:
            x = xx[0][0]
        Rrhox = Rrho[:x,:x]
        return Rrhox

#    def Rx(self,city):
#        Rrhox = caculate(self,city)
#        return Rrhox

    def save(self,city,deltaR):#i 预留次数参数
        Rx = indexCoor.caculate(self,deltaR)
        C,radius,maxnode,h=city.C,city.radius,city.maxP,city.H
        se = {}
        for i in range(1,len(Rx)+1):
            se[i] = pd.Series(Rx[i])
        df = pd.concat([se[i] for i in range(1,len(Rx)+1) ],axis = 1)
        name = "C"+str(C)+"--r"+str(radius)+"--maxnode"+str(maxnode)+"--h"+\
        str(h)+"--delataR"+str(deltaR)+"--i"+str(i)
        df.to_csv(name+".csv")
        print("saved")

    def spatial_range(self):
        nodelist = indexCoor.nodeList(self)
        x = []
        y = []
        for k in nodelist.keys():
            x.append(k[0])
            y.append(k[1])
        return max(x),min(x),max(y),min(y)

    def paint(self,size = 0.1):
        nodelist = indexCoor.nodeList(self)
        x = nodelist
        a = []
        c = []
        xmax,xmin,ymax,ymin = indexCoor.spatial_range(self)
        for k,v in x.items():
            a.append(k)
            c.append(1/(v[7]))
        m = []
        n = []
        for i in a:
            m.append(i[0])
            n.append(i[1])
        plt.figure(figsize=(10,10),dpi=100)
        plt.scatter(m,n,size,c = c)
        plt.xlim((xmin,xmax))
        plt.ylim((ymin,ymax))
        plt.show()

    def fun(x, a, n):
        b = 1-x**(-a)
        return 1-np.sign(b)*np.abs(b)**n#numpy 不支持负值的指数

    def curveFit(self,H,deltaR):
        H = H
        delta = deltaR
        x,y=[],[]
        for a in self.caculate(delta):
            x.append(a[0])
            y.append(a[1]/H)
        popt,pcov = curve_fit(indexCoor.fun,x,y)
        a = popt[0]
        n = popt[1]
        yvals = indexCoor.fun(x,a,n)
        plt.plot(x, yvals, 'r',label='polyfit values')
        plt.legend()
        plt.plot(x,y,"b",label = "line")
        return [a,n]
