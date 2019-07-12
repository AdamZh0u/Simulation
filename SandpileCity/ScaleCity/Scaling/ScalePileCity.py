# -*- coding: utf-8 -*-
'''
Created on 29 Apr 2018
python 3.6
@author: zzz
'''
from rtree import index
import numpy as np
import random
import math

#源代码中index2coor记录的是有人存活的格子，用ksequence记录每个格子人数
#将index2coor变为记录存活的人的序号，len（index2coor）为总人数
def initiate(radius,C,L = 10**5): 
    coordinate = np.ones(2)*L/2.0
    nodelist = {(coordinate[0],coordinate[1]):{1:1, 3:1, 5:0.0, 6:0, 7:1}} 
    index2coor = {1:(coordinate[0],coordinate[1])}
    idx = index.Index()
    for key in nodelist:
        idx.insert(  nodelist[key][1],list(np.r_[coordinate,coordinate])  )                     
    limitt = np.r_[coordinate - radius,coordinate + radius] 
    return nodelist,idx,limitt,index2coor

def choosenode(nodelist,limitt,C,index2coor):#?
    white = ( (limitt[2]-limitt[0])*(limitt[3]-limitt[1])-len(nodelist) )*C
    rnd = random.random()*( len(index2coor)+len(nodelist)*C + white ) 
    if rnd>len(index2coor)+len(nodelist)*C:
        while 1:
            ii = int( random.random()*(limitt[2]-limitt[0])   + limitt[0] )
            jj = int( random.random()*(limitt[3]-limitt[1])   + limitt[1] )
            if (ii,jj) not in nodelist:
                return (ii,jj),0
    else:
        pos = random.randint(1,len(index2coor))
        return index2coor[pos],1  
        
def onestep(nodelist,index2coor,idx,radius,C,h,limitt,L=10**5):
    two,flag = choosenode(nodelist,limitt,C,index2coor)  
    i = two[0]; j = two[1]
    if flag == 0:
        intersection = list(  idx.intersection( [i-radius,j-radius, i+radius,j+radius] )  ) 
        if len(intersection) > 0: 
            for key in intersection:
                if np.linalg.norm(np.array(index2coor[key]) - np.array([i,j])) <= radius:  
                    nodelist[(i,j)] = {1:0,3:1,5:np.linalg.norm(np.array([i,j])-L/2),6:0,7:1}
                    index2coor[max(index2coor.keys())+1]=(i,j)
                    newpoint = [i,j]
                    idx.insert( len(nodelist), np.r_[newpoint, newpoint] )  
                    for i in range(2):  
                        limitt[i]   = round(min(limitt[i],newpoint[i]-radius))
                        limitt[i+2] = round(max(limitt[i+2],newpoint[i]+radius)) 
    return nodelist,index2coor,idx,limitt
                
    if flag==1: 
        if nodelist[(i,j)][7] <= h:#不溢出
            nodelist[(i,j)][7] += 1
            nodelist[(i,j)][3] += 1
            index2coor[max(index2coor.keys())+1]=(i,j)
        else:
            while ((i.j) in nodelist.keys()) and nodelist[i,j][7] > h :
                (i,j) = sandpile[i,j,h,nodelist]
            if (i,j) in nodelist.keys():
                nodelist[(i,j)][7] += 1
                nodelist[(i,j)][3] += 1
                index2coor[max(index2coor.keys())+1]=(i,j)
            else:
                nodelist[(i,j)] = {1:0,3:1,5:np.linalg.norm(np.array([i,j])-L/2),6:0,7:1}
                index2coor[max(index2coor.keys())+1]=(i,j)
    return nodelist,index2coor,idx,limitt

def sandpile(i,j,h,nodelist):
    r = i
    c = j
    arounddic = {1:(r -1,c-1),2:(r -1,c),3:(r -1,c+1),
                         4:(r,c-1),5:(r,c),6:(r,c+1),
                         7:(r+1,c-1),8:(r+1,c),9:(r+1,c+1)}
    deltas = []
    #生成邻接阵arov
    arov={}
    for i in range(1,10):
        if arounddic[i] in nodelist:
            arov[i] = nodelist[arounddic[i]][7]
        else:
            arov[i] = 0
        delta =nodelist[(i,j)][7] - arov[i] 
        deltas.append(delta)
    B = np.cumsum(deltas)
    rnd = random.random()*B[-1]
    ind = np.nonzero(B<rnd)
    if len(ind[0])==0:
        pos = 1
    else:
        pos = ind[0][-1]+2
    #得到位置
    return arov[pos]        

def caculate(nodelist,radius):
    w = []
    delta  = radius
    for key in nodelist:
        w.append([nodelist[key][5],nodelist[key][7]])
    w.sort()
    w = np.array(w)
    R = np.arange(0,np.max(w[:,0]),delta)
    RL = np.zeros((len(R),2)) 
    RL[:,0] = R
    for i in range(len(RL)):
        RL[i,1] = np.sum(w[w[:,0]<RL[i,0],1])
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
if __name__=='__main__':
    L=10**10;times=10**8
    radius  = 10  #radius就是r0
    delta = radius #做统计时取的小间隔r0
    #maxnode = 10000000
    maxnode = 100000
    C = 0.01
    sequence = []; 
    nodelist = {}
    
radius = 10
C = 0.01
maxnode = 100
h = 3
nodelist,idx,limitt,index2coor= initiate(radius,C)
while len(index2coor) < maxnode:
    nodelist,index2coor,idx,limitt = onestep(nodelist,index2coor,idx,radius,C,h,limitt)
    if len(index2coor)%5000 == 0:
        print ('PPP',  len(index2coor), len(nodelist))
        Rrhox = caculate(nodelist,radius)
        print(Rrhox)
    