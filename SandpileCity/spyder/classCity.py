# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:34:26 2018

@author: zzz
"""
import main;

class city(object):
    def __init__(self,H,C,maxP,radius=10,L=10**5):
        # H 沙堆阈值 C 引力 maxP 最大人口 radius 引力范围 L 背景范围 
        # deltaP 间隔人口 delta 密度采样间隔
        self.C,self.H,self.maxP = C,H,maxP
        self.radius,self.L = radius,L

    def step(self):
        index2coor,nodelist,idx,limitt = main.initiate(self.radius,
                                                       self.C,self.L)#初始化
        while len(index2coor) < self.maxP:
            index2coor,nodelist,idx,limitt = main.onestep\
            (index2coor,nodelist,idx,limitt,self.radius,self.C,self.H,self.L)
        return index2coor
