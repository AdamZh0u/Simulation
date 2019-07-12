# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:33:04 2018

@author: zzz
"""
from rtree import index
import numpy as np
import random
import classIndexCoor as indc

def initiate(radius,C,L):
    coordinate = np.ones(2)*L/2.0
    nodelist = {(coordinate[0],coordinate[1]):{5:0.0,7:1}} #5：到心距 7：点数
    index2coor = indc.indexCoor([(coordinate[0],coordinate[1])])
    #index2coor = [(coordinate[0],coordinate[1])]
    idx = index.Index()
    idx.insert(0,list(np.r_[coordinate,coordinate]))
    limitt = np.r_[coordinate - radius,coordinate + radius] 
    return index2coor,nodelist,idx,limitt

def choosenode(index2coor,nodelist,limitt,C):#?
    white = ( (limitt[2]-limitt[0])*(limitt[3]-limitt[1])-len(nodelist) )*C
    #white = ( (list(limitt)[2]-list(limitt)[0])*(list(limitt)[3]-\
    #list(limitt)[1])-len(nodelist) )*C
    exist = len(index2coor)+len(nodelist)*C
    rnd = random.random()*( exist + white )
    if rnd>exist:
        while 1:
            ii = int( random.random()*(limitt[2]-limitt[0]) + limitt[0] )
            jj = int( random.random()*(limitt[3]-limitt[1]) + limitt[1] )
            if (ii,jj) not in nodelist:
                return (ii,jj),0 # 这个结构如果产生不了输出就会死循环，
            #先随机再判断，贝叶斯问题？？
            #用蒙特卡罗验证落到各个空格子概率相等？
    else:
        pos = random.randint(0,len(index2coor)-1)#左闭右闭
        #随机落到落点顺序上  这很重要
        return index2coor[pos],1

def onestep(index2coor,nodelist,idx,limitt,radius,C,h,L):
    two,flag = choosenode(index2coor,nodelist,limitt,C)  
    i,j = two[0],two[1]
#    idx = index.Index()这一步加上的话把idx初始化了
    # intersection只能调用一次就结束了
    if flag == 0:
        intersection = list(idx.intersection([i-radius,j-radius, 
                                              i+radius,j+radius])) 
    #这里的idx在哪里定义的？？？
        if len(intersection) > 0:#新点矩形范围内
            for key in intersection:
                if np.linalg.norm(np.array([index2coor[key]])-np.array([i,j])) <= radius:#?key-1
                    state = 1
                    break
                else:
                    state = 0
            if state == 1:
                index2coor,nodelist,idx,limitt = \
                insert_newpoint(i,j,nodelist,index2coor,idx,limitt,L,radius)
        return index2coor,nodelist,idx,limitt

    elif flag==1: 
        if nodelist[(i,j)][7]+1 <= h:#不溢
            nodelist[(i,j)][7] += 1
            #index2coor[len(index2coor)]=(i,j)
            index2coor.append((i,j))
        else:
            while ((i,j) in nodelist.keys()) and (nodelist[(i,j)][7]+1 > h) :
                (i,j) = sandpile(i,j,h,nodelist)
            if (i,j) in nodelist.keys():#溢出到有点的格子
                nodelist[(i,j)][7] += 1
                #index2coor[len(index2coor)]=(i,j)
                index2coor.append((i,j))
            else:#溢出到空格子
                index2coor,nodelist,idx,limitt = \
                insert_newpoint(i,j,nodelist,index2coor,idx,limitt,L,radius)
        return index2coor,nodelist,idx,limitt

def insert_newpoint(i,j,nodelist,index2coor,idx,limitt,L,radius):
    nodelist[(i,j)] = {5:np.linalg.norm(np.array([i,j])-L/2),7:1}
    #index2coor[len(index2coor)+1]=(i,j)
    index2coor.append((i,j))
    newpoint = [i,j]
    #这里前往小心，index2coor已经新增了点，所以要减1
    idx.insert( len(index2coor)-1, np.r_[newpoint, newpoint] )  ###idx
    for x in range(2):
        limitt[x]   = round(min(limitt[x],newpoint[x]-radius))
        limitt[x+2] = round(max(limitt[x+2],newpoint[x]+radius))
    return index2coor,nodelist,idx,limitt

def sandpile(i,j,h,nodelist):
    r = i
    c = j
    arounddic = {
	1:(r-1,c-1),2:(r -1,c),3:(r -1,c+1),
	4:(r,c-1),5:(r,c),6:(r,c+1),
	7:(r+1,c-1),8:(r+1,c),9:(r+1,c+1)
	}
    deltas = []
    #邻接阵arov
    arov={}
    for m in range(1,10):
        if arounddic[m] in nodelist:
            arov[m] = nodelist[arounddic[m]][7]
        else:
            arov[m] = 0
        delta =nodelist[(r,c)][7] - arov[m] 
        deltas.append(delta)
    B = np.cumsum(deltas)
    if B[-1]!= 0:
        rnd = random.random()*B[-1]
        ind = np.nonzero(B<rnd)
        if len(ind[0])==0:
            pos = 1
        else:
            pos = ind[0][-1]+2
    else:#九格同
        pos = 5 
        while pos == 5:
            pos = random.randint(1,9)
		#pos = 1 #左下
		#pos = 9 #右上
    #得到位置
    return arounddic[pos]


