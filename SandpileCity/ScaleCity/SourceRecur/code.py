# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:42:08 2014
@author: Ricky Lee
@Description: 它是在FinalCbeta的基础上，把所有的图之类都画出来
最终版：：一旦落点，每个格子的度等于其内 点数+C， r0这个参数只是用来进行匹配。
"""

from rtree import index
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
import math
from scipy.optimize import leastsq
import matplotlib
import sys

"""
#node: 每一个加入的节点，即是一个小方格
#nodelist: 将所有加入的节点构造一个字典，
#每个节点存五个数组：1坐标, （2(相邻点ID,距离)<暂时不用>）  ,3每个节点的度,   （4每个节点对应的连边长度合<暂时先不要之>）
                   ,5离中心半径，6该点落下的时间步 (changed as described below)，7the number of people in this unit
                       在最终版里3、7这两个定义只差了个C，但在存储的过程中二者一样，因为C的影响都放到外面去处理了
#idx: 所有node的空间索引（rtree）
"""


def initiate(L,radius,C): #k is not used
    coordinate = np.ones(2)*L/2.0
    nodelist = {(coordinate[0],coordinate[1]):{1:1, 3:1, 5:0.0, 6:0, 7:1}}  ####!!!这里虽然仍叫Nodelist，但实际上是LatticeList，所以在后面的计算时须要小心！！~~
    #坐标(i,j)作为Index，  1序号(第几个成功落点的点), 3degree, 5distance2center, 6timestamp for survival， 7the number of people in this unit
    index2coor = {1:(coordinate[0],coordinate[1])}  
    # Create 2D index
    idx = index.Index() 
    for key in nodelist:   #
        idx.insert(  nodelist[key][1],list(np.r_[coordinate,coordinate])  )                     
    limitt = np.r_[coordinate - radius,coordinate + radius] #also one dimension array
    # nodelist: a list of nodes~~  idxnd: Rtree indices~~  limitt: Rectangle boundary：xmin,ymin,  xmax,ymax
    ksequence = []
    ksequence.append(1) #这里只记录每个格点上的人数，所以在这里面C没有必要引入，后面C的影响 都放在choosenode里来处理
    return (nodelist,idx,limitt,index2coor,ksequence)

"""
  Choose one node by degree（C+\rho） distribution
"""
def choosenode(nodelist,limitt,C,ksequence,totpop):  #ksequence只是传进来用了下，没有作改变
    white = ( (limitt[2]-limitt[0])*(limitt[3]-limitt[1])-len(nodelist) )*C#未落点的Limit框中空白格点的吸引力
    rnd = random.random()*( sum(ksequence)+len(nodelist)*C + white ) 
#    print 'sum,totpop', sum(ksequence),totpop #they two are the same prove the process is correct
    if rnd> sum(ksequence)+len(nodelist)*C:  #说明选到了空白区域，然后就随机落点，直到它落到一个空白点上（是否存活在主程序中判断）
        while 1:
            ii = int( random.random()*(limitt[2]-limitt[0])   + limitt[0] )
            jj = int( random.random()*(limitt[3]-limitt[1])   + limitt[1] )
            if (ii,jj) not in nodelist:
                return (ii,jj),0,ksequence  #flag=0,表示落了个新的空白位置
    else:  #落到了非空格子上
#        print white,rnd,len(sequence)+len(nodelist)*k,'###'    
        A = np.array(ksequence)+C
        B = np.cumsum(A)
#        rand = rand*B[-1]
        ind = np.nonzero(B<rnd)  
#        print rnd, B, ind
        if len(ind[0])==0:  #比第一个节点都小就会返回空，所以用长度来判，然后位置是第1个节点（1）
            pos = 1
        else:
            pos = ind[0][-1]+1  #因从0开始返回，故须+1， 其序始同于模型设定
        return index2coor[pos],1,ksequence    #flag=1,表示落到了从前的位置上     

        
def onestep(nodelist,index2coor,idx,time,L,radius,C,limitt,totpop,ksequence):
    #calculate degree distribution and choose node j to match
    ss = 1
    for i in range(2):
        ss = ss*(limitt[i+2]-limitt[i])
    ss *= C
#    ss = (ss-len(nodelist))*C
    ss += totpop
    locallambda = ss/(L**2*C + totpop)  #;print locallambda
    time += random.expovariate(locallambda)  #time就是所谓的落点的时间R_t~t^xxx中的t~~   make the time real....

    two,flag,ksequence = choosenode(nodelist,limitt,C,ksequence,totpop)  
    i = two[0]; j = two[1]  #这是它们的坐标

    intersection = list(  idx.intersection( [i-radius,j-radius, i+radius,j+radius] )  )  #用框和之前的点来进行Intersect
    withincircle = 0    
    if len(intersection) > 0:  #this node (i,j) can survive ##为什么Intersection时会出现3L？明明只有两个点

        for key in intersection:  
#            print i,j,key,idx,list(intersection),index2coor[key],nodelist,'\n\n\n'
            if np.linalg.norm(np.array(index2coor[key]) - np.array([i,j])) <= radius:  #intersection是个方形,还是看圆形区域内
                withincircle += 1
                continue
                
        if flag==1: #落到了已有格子上
            nodelist[(i,j)][7] += 1
            nodelist[(i,j)][3] += 1
            ksequence[ nodelist[(i,j)][1]-1 ] += 1
            totpop += 1   
            
        elif  withincircle > 0  and  flag==0: #落到了空白格子上
            totpop += 1  ##        
            nodelist[(i,j)] = {1:len(nodelist)+1,3:1,5:np.linalg.norm(np.array([i,j])-L/2),6:time,7:1} #最终版

            index2coor[len(nodelist)] = (i,j)

            newpoint = [i,j]
            idx.insert( len(nodelist), np.r_[newpoint, newpoint] )  
#==============================================================================
            ksequence.append( nodelist[(i,j)][3] )
#==============================================================================
            
            for i in range(2):  #2 is the dimension 'd'
                limitt[i]   = round(min(limitt[i],newpoint[i]-radius))
                limitt[i+2] = round(max(limitt[i+2],newpoint[i]+radius)) #相应维另一点之x,y,z...(共d个)坐标矣
    return nodelist,index2coor,idx,time,limitt,totpop,ksequence

def residuals2(p,xx,yy,zz):
    A,a,b=p
    return np.log(zz)- (a*np.log(xx)+b*np.log(yy)+A)

def residuals(p,xx,yy):
    k,b=p
    return np.log(yy) - (k*np.log(xx)+b)

def LinearRegress(xx,yy):
    r1 = leastsq(residuals,[1,1],args=(xx,yy))  #return  k,b
    fit= r1[0][0]*np.log(xx)+r1[0][1]  #y尖
    residualss = (fit-np.log(yy))**2   
    totalres = np.sum(residualss)  #SSR
    stot = np.sum((fit-np.mean(np.log(yy)))**2)   #SST
    rsquare = 1-totalres/stot
    return r1,rsquare,residualss

def LinearRegressOutlier(xx,yy,fit):
    r1,rsquare,residualss = LinearRegress(xx,yy)
    while rsquare<fit and np.size(xx)>3:
        maxx = np.amax(residualss)
        bools= residualss==maxx
        bools=~bools  #??
        xx = xx[bools]
        yy = yy[bools]
        r1,rsquare,residualss = LinearRegress(xx,yy)
    return r1,rsquare

def circumcircle2(T):
    P1,P2,P3 = T[:,0], T[:,1], T[:,2] #所有三角形 第0，1，2个点的坐标(x,y)之数组之数组##P1乃一个数对数组##
    b = P2 - P1
    c = P3 - P1
    d = 2*(b[:,0]*c[:,1]-b[:,1]*c[:,0])
    center_x=(c[:,1]*(np.square(b[:,0])+np.square(b[:,1]))- b[:,1]*(np.square(c[:,0])+np.square(c[:,1])))/d + P1[:,0]
    center_y=(b[:,0]*(np.square(c[:,0])+np.square(c[:,1]))- c[:,0]*(np.square(b[:,0])+np.square(b[:,1])))/d + P1[:,1]
    #print 'center = ',np.array((center_x, center_y)),'\n\n\n',np.array((center_x, center_y)).T ##.T就可以把两个大数据按序号对应生成数对的大数组，太神奇了
    return np.array((center_x, center_y)).T ##将两个大数组按顺序各种组好组成一坨2变量数组

def check_outside(point, bbox):
    point = np.round(point, 4) #任意位置出了框就True
    return point[0]<bbox[0] or point[0]>bbox[2] or point[1]< bbox[1] or point[1]>bbox[3]

def move_point(start, end, bbox):
    vector = end-start
    c = calc_shift(start, vector, bbox)
    if c>0 and c<1:
        start = start+c*vector
        return start

def calc_shift(point, vector, bbox):
    c = sys.float_info.max  ## 1.79769313486e+308
    #print 'point = ',point, vector
    for l,m in enumerate(bbox):
        #print 'enume = ',l,m
        a = ( float(m)-point[l%2] )/vector[l%2]
        if  a>0 and  not check_outside(point+a*vector, bbox):
            if abs(a)<abs(c):
                c = a
    return c if c<sys.float_info.max else None

def voronoi2(P,outlines, bbox=None):
    if not isinstance(P, np.ndarray): ## if not~~
        P = np.array(P)
    if not bbox:
        xmin=P[:,0].min()
        xmax=P[:,0].max()
        ymin=P[:,1].min()
        ymax=P[:,1].max()
        
        xrange=(xmax-xmin)/100.0# * 0.3333333
        yrange=(ymax-ymin)/100.0# * 0.3333333
        bbox=(xmin-xrange, ymin-yrange, xmax+xrange, ymax+yrange)
        Axisbox=(xmin-xrange, xmax+xrange, ymin-yrange, ymax+yrange)
    bbox=np.round(bbox,4) ##why 999.. or 0001? wrong in this function?

    #print 'Axis = ',np.array(Axisbox),'\n\n\n'
    D = matplotlib.tri.Triangulation(P[:,0],P[:,1]) ##不知这种画三角形是不是严格的Delaunay，但样子是~~Lawson算法似乎可演化~~###
    T = D.triangles ##get all the triangles..three numbers in an arrary, each is an index for node
                    ##其节点的序号对应于Points中节点的顺序，T中序号的排列是按逆时针排列的##
    ntri = T.shape[0] ##get the number of rows, shape[1]~~column
#    print 'T = ',T, '\n', ntri
    #print 'P[T] = ',P[T]
    C = circumcircle2(P[T]) 
    #P乃数组，T乃序号在数组中，P[T]则会将T中所有序号对应行的P值取出，若T中有3个元素，则将3者所得结果再取作一个稍大的数组
        #the three lines below are unnecessary~~it can be obtained from variables above 
    #CC = matplotlib.tri.Triangulation(C[:,0],C[:,1]) ##
    #CT = CC.triangles ##get all the triangles..three numbers in an arrary, each is an index for nodes
    #n = CT.shape[0] ##get the number of rows, 1~column
    #print CT[200:365:1],n, '\n\n\n', 6<5 or 4<3
    pos = {}
    segments = []  
    for i in range(ntri):
        if i!=-1 and i not in pos:        
            pos[i] = C[i]
        for j in range(3):
            k = D.neighbors[i][j]
                    ##neighbors中的序号对应于D中各个三角形的外接圆的次序，其1234分别表示T中第1234行的三角形
                    ##其中-1者 对应的是那些在bbox外面的节点，所以只有去掉-1者就可得到路网的拓扑
            if k != -1:
                #cut segment to part in bbox
                start,end = C[i], C[k]
                if check_outside(start, bbox):  #应该是如果圆心出了框，就把它再往里拉至bbox~~~
                    start = move_point(start,end, bbox)
                    if  start is None:
                        continue
                if check_outside(end, bbox):
                    end = move_point(end,start, bbox)
                    if  end is None:
                        continue
                segments.append( [start, end] )
            else:
                #ignore center outside of bbox
                if check_outside(C[i], bbox):
                    continue
                first, second, third = P[T[i,j]], P[T[i,(j+1)%3]], P[T[i,(j+2)%3]]
                edge = np.array([first, second])
                vector = np.array([[0,1], [-1,0]]).dot(edge[1]-edge[0]) ##矩阵 点乘 一个向量
                line = lambda p: (p[0]-first[0])*(second[1]-first[1])/(second[0]-first[0]) - p[1] + first[1]
                    ##内联函数
                orientation = np.sign( line(third) )*np.sign( line(first+vector) )
                if orientation>0:
                    vector = -orientation*vector
                c = calc_shift(C[i], vector, bbox)
                if c is not None:
                    segments.append( [C[i],C[i]+c*vector] )
                
    linetopo = []
    weights = []
    for i in range(ntri):
        for j in range(3):
            k = D.neighbors[i][j]
#            print k, C[k]
#            weights.append([(C[i]+C[k])/2, np.sqrt(np.sum(np.square(C[i]-C[k])))])#good~~~
            if outlines == 1:            
                if k != -1 and [k,i] not in linetopo:##须去重..若有向可不去
                    linetopo.append([i, k])
            elif outlines == 0:
                if k != -1 and not check_outside(C[k],bbox) and not check_outside(C[i],bbox) and [k,i] not in linetopo:##中间两个Check就把外面的边给去掉了
                    linetopo.append([i, k])  ##兹乃NETWORK也
#                weights.append([(C[i]+C[k])/2, np.sqrt(np.sum(np.square(C[i]-C[k])))])#good~~~
#                if i != -1:
#                    weights.append([(C[i]+C[k])/2, np.sqrt(np.sum(np.square(C[i]-C[k])))])#good~~~
    for i in range(len(segments)):
        weights.append([(segments[i][0]+segments[i][1])/2, np.sqrt(np.sum(np.square(segments[i][0]-segments[i][1])))])#good~~~
        ####weights记录的是每段路的  中心，及其 长度值
#    print linetopo,'\n\n',weights          

    return segments, Axisbox, linetopo, weights, pos #pos中是每段路其端点的位置

#----------------------experiment-----------------------
if __name__=='__main__':
    L=10**10;times=10**8
    radius  = 100  #radius就是r0
    delta = radius #做统计时取的小间隔r0
    #maxnode = 10000000
    maxnode = 100000
    C = 0.001
    sequence = []; 
    nodelist = {}
for C in np.logspace(-5,3,100):
    print 'C = ', C,',--N = ',maxnode
#    if C>4329 and C<6579:
#    radius += 20
    delta = radius
#    delta = 2*radius
    if 1==1:
        for repeat in range(10):
            namep = 'N'+str(maxnode)+'PttRtdenpro'+'C'+str(C)+'re'+str(repeat)+'.csv'
        #==============================================================================
#            fpp = open(namep,'w')
        #==============================================================================
        #======================最后在拟合时用的Rt也是maxRt，亦即限定个最远范围拟合即可================================================
#            print >>fpp, 'Pt',',','maxRt',',','minRt',',','aveRt',',','t',',','tstep',',',  'rho5',',','rho15',',','rho105',',',  'pro5',',','pro15',',','pro105'
        #==============================================================================
        #    print >>fpp, 'Pt',',','80Rt',',','w10Rt',',','t',',','tstep',',',  'rho5',',','rho15',',','rho105',',',  'pro5',',','pro15',',','pro105',  'JDpro5',',','JDpro15',',','JDpro105'
            sequence = [];nodelist = {}
            nodelist,idx,limitt,index2coor,sequence = initiate(L,radius,C)
            
            totpop = 1  #这种情况下一定得注意总人数不是len(nodelist)~~那个是总‘建成面积’
            tstep = 1
            time = 1  #R_t~t^中的t
            tempP = 1; tempT = 1;T = 2
            while tstep < times  and  totpop < maxnode:
                nodelist,index2coor,idx,time,limitt,totpop,sequence = onestep(nodelist,index2coor,idx,time,L,radius,C,limitt,totpop,sequence)
        #=================================以Population为横轴的统计============================================#
                if totpop%5000 == 0:
                    if tempP!=totpop and tempT!=time:
                        print 'PPP',tstep,time, totpop, len(nodelist), len(sequence)
                        
                        w = []    
                        for key in nodelist:
                    #        w.append([nodelist[key][5],1])
                            w.append([nodelist[key][5],nodelist[key][7]])
                        w.sort()
                        w = np.array(w)
                        
                        R = np.arange(0,np.max(w[:,0]),delta)
                        RL = np.zeros((len(R),2))  #RL~~R,Pop~~懒的改变量名了，RP就用RL代了
                        RL[:,0] = R
                        for i in range(len(RL)):
                            RL[i,1] = np.sum(w[w[:,0]<RL[i,0],1])
                    #==================rho(P)_R================================================    
                        Rrho = np.zeros((len(R),2))
                        Rrho[:,0] = R + delta/2
                        
                        for i in range(len(Rrho)-1):
                            Rrho[i,1] = (RL[i+1,1] - RL[i,1])/(math.pi*(delta**2+2*delta*RL[i,0]))
                    #==================probability_R================================================
                        w = []    
                        for key in nodelist:
                            w.append([nodelist[key][5],nodelist[key][3]])
                        w.sort()
                        w = np.array(w)
                        totDegree = np.sum(w[:,1])
                        Rrhoo = np.zeros((len(R),2))
                        Rp = np.zeros((len(R),2))
                        Rp[:,0] = R
                        for i in range(len(Rp)):
                            RL[i,1] = np.sum(w[w[:,0]<Rp[i,0],1])
                            
                        Rpp = np.zeros((len(R),2))
                        Rpp[:,0] = R + delta/2
                        RpJD = np.zeros((len(R),2))
                        RpJD[:,0] = R + delta/2
        #                print 'total degree = ', totDegree
                        for i in range(len(Rp)-1):
                            Rpp[i,1] = (RL[i+1,1] - RL[i,1])/(math.pi*(delta**2+2*delta*RL[i,0]))/totDegree
                            RpJD[i,1] = (RL[i+1,1] - RL[i,1])/(math.pi*(delta**2+2*delta*RL[i,0]))/(len(sequence)+C*L**2)
    
        #                Rrhoo[:,0] = np.arange(0,np.max(w[:,0]),delta)
        #                Rp[:,0] = np.arange(0,np.max(w[:,0]),delta)+delta/2  #这是把那个区间的概率用其中心的值表示出来~~
        #                RpJD[:,0] = np.arange(0,np.max(w[:,0]),delta)+delta/2  #这是把那个区间的概率用其中心的值表示出来~~
        #                for i in range(len(Rrhoo)-1):
        #                    Rp[i,1] = (np.sum(w[w[:,0]<(Rrhoo[i,0]+delta),1]) - np.sum(w[w[:,0]<Rrhoo[i,0],1]))/(totDegree * math.pi*(delta**2+2*delta*Rrho[i,0]))
        #                    RpJD[i,1] = (np.sum(w[w[:,0]<(Rrhoo[i,0]+delta),1]) - np.sum(w[w[:,0]<Rrhoo[i,0],1]))/(( len(sequence)+L**2*k ) * math.pi*(delta**2+2*delta*Rrho[i,0]))
        #                print >>fpp, totpop,',',max(abs(limitt-L/2)),',',min(abs(limitt-L/2)),',',(max(abs(limitt-L/2))+min(abs(limitt-L/2)))/2,',',time,',',tstep,',',  Rrho[0,1],',', Rrho[1,1],',', Rrho[10,1],',',  Rpp[0,1],',', Rpp[1,1],',', Rpp[10,1],',',RpJD[0,1],',', RpJD[1,1],',', RpJD[10,1]
        #                print >>fpp, totpop,',',(max(abs(limitt-L/2))+min(abs(limitt-L/2)))/2,',',time,',',tstep,',',  Rrho[0,1],',', Rrho[1,1],',', Rrho[10,1],',',  Rp[0,1],',', Rp[1,1],',', Rp[10,1],',',RpJD[0,1],',', RpJD[1,1],',', RpJD[10,1]
        #                print >>fpp, totpop,',',max(abs(limitt-L/2)),',',min(abs(limitt-L/2)),',',(max(abs(limitt-L/2))+min(abs(limitt-L/2)))/2,',',time,',',tstep,',',  Rrho[0,1],',', Rrho[1,1],',', Rrho[10,1],',',  Rp[0,1],',', Rp[1,1],',', Rp[10,1]
                        tempP = totpop; tempT = time
                        
                        if totpop == maxnode:
#                            print totpop
        #                    namet = 'JD_prob--'+'N='+str(maxnode)+'k'+str(k)+'.csv'
        #                    np.savetxt(namet, RpJD, delimiter=',')#,fmt='%1.15f')
        #                    namep = 'prob--'+'N='+str(maxnode)+'k'+str(k)+'.csv'
        #                    np.savetxt(namep, Rpp, delimiter=',')#,fmt='%1.15f')
    #                        namerho = 'originalC-withinR-density--'+'N='+str(maxnode)+'C'+str(C)+'re'+str(repeat)+'.csv'
                            dcC = str(C)
                            if len(dcC)<6:
                                if C>=1:
#                                    dcC += '.'
                                    for i in range(6-len(dcC)):
                                        dcC += '0'
                                elif C<1 and C>0:
                                    for i in range(6-len(dcC)):
                                        dcC += '0'
                            rr = str(radius)
                            if len(rr)<3:
                                rr += '.0'
                            namerho = 'N='+str(maxnode)+'--C'+str(dcC)+'--R'+str(rr)+'--v'+str(repeat)+'.csv'
    #                        namerho = 'originalC-withinR-density--'+'N='+str(maxnode)+'C'+str(C)+'Radius'+str(radius)+'.csv'
    #====================================一旦Rho有等于0都就停下，认为这是Rt==========================
                            a = Rrho
                            xx = np.nonzero(a[:,1]==0)  #会返回类似“(array([41]),)”这样的结果
    #                        print xx,xx[0], len(xx[0])
                            if len(xx[0])==0:
                                x = 0 
                            else:
                                x = xx[0][0]
                            Rrhox = Rrho[:x,:x]
                            np.savetxt(namerho, Rrhox, delimiter=',')#,fmt='%1.15f')##这是最后的输出，下面的是另外情况的
    #                       np.savetxt(namerho, Rrho, delimiter=',')#,fmt='%1.15f')
    
    ##=================================验证Zipf，将所有节点的密度输出来，然后将之按降序排列=============================================                        
    #                        estimatedRT = (x+1)*delta/2
    #                        rholattice = 'nowC+edgeMutation---'+'N'+str(maxnode)+'C'+str(C)+'.csv'
    #                        fprl = open(rholattice,'w')         
    ##                        print>>fprl,'Rho',',','Pt_when_mutate',',','sequence_of_thislattice'
    #                        rho = []
    #                        for key in nodelist:
    #                            if nodelist[key][5] <= estimatedRT:     
    #                                rho.append([nodelist[key][1],nodelist[key][3],nodelist[key][7]])
    ##==============================================================================
    ##                         rho = np.array(rho)
    ##                         rho.sort(0)  #按密度0 或者序号2 排个序，然后看情况
    ##                         ##怎么降序排来着？
    ##==============================================================================
    #                        for i in range(len(rho)):
    #                            print>>fprl, rho[i][0],',',rho[i][1],',',rho[i][2]
    ##==============================================================================
    ##                         for key in nodelist:
    ##                             print>>fprl, nodelist[key][7],',',nodelist[key][8],',',nodelist[key][1]
    ##==============================================================================
    #                        fprl.close()
        
                tstep += 1    
#====================================下面的部分只是为了画图，与生成密度分布无关================================
##    C = 10*C0
#    #==============================================================================
#    #     fpp.close()
#    #==============================================================================
#    WIDTH = max(limitt[2]-limitt[0], limitt[3]-limitt[1])
##    GDPdelta = 0.6*radius  #这个是最后统计时那个经济的方格的大小
##    GDPdelta = WIDTH/10  #这个是最后统计时那个经济的方格的大小
##    print WIDTH, GDPdelta
##    print 'limit is ',limit  ##limit=[4., 4., 6., 6.]
#    timee=1; t=1;#edges=[0];
#    newareas=[0]; newlengths=[0];
#    #roadlength=np.ndarray([0])
#    #roadlength1=np.ndarray([0])
#    dimensions=0
#    sizes=np.ndarray(1)
#    ##------draw voronoi--------##
#    nds = []
#
#    results = []  #存储L与N的数据
#    results2 = [] #存储rou_l与rou_n的数据
#    already = []    
#
#    for key in index2coor:
#        nds.append( np.array(index2coor[key])-0.5+np.array([np.random.rand(),np.random.rand()]) ) 
#    #把相应的点在其中间的方格内重新确定下位置
#
##    print len(nds), 'N = ',len(index2coor), '\n\n\n', index2coor#,'\n\n\n',ndlist,'\n\n\n',nds
##====================须要Voronoi的时序时~~VoronoiEvolve~~~================================
##         if np.remainder(len(ndlist),maxnode/10)==0 and len(ndlist) not in already:
##             lines, axisbox, network, weights, pos = voronoi2(nds)
##             ww = np.array(weights)
##             results.append([len(ndlist), np.sum(ww[:,1])])
##             results2.append([float(len(ndlist))/float(L**2), np.sum(ww[:,1])/len(ndlist)])#density
##             already.append(len(ndlist))
##             print len(ndlist),',',t,',',already
#    #        results2.append([t/area, np.sum(np.array(weights[:,1]))/area])#density?
##            print 'length = ', type(len(ndlist)),np.sum(ww[:,1])
#    
#    #ndss = [ndlist[i][1] for i in ndlist.keys()] #upper is the same with this #ndss = np.array(ndss)
##==============================================================================
#
##===================粘过来之前画示意图的程序 继续来画图=========================
#    GDPdelta = 100
#    nds = np.array(nds)
##    print 'nds = ',nds  #点的位置信息，（x,y）即为一组
#    pos = {}
#    lines, axisbox, network, weights, pos = voronoi2(nds,1) 
##==============================================================================
##    print 'test lines, networks  ',lines,'\n\n\n', network,'\n\n\n'
##    print 'test weigths, pos  ',weights,'\n\n\n', pos,'\n\n\n'
##    print pos
#    print 'OOOKKK',np.array(results),'\n\n',np.array(results2)#,'\n\n',network
##===============================从Limit框中来算每个位置的
#    gdp = {}
#    x=[];y=[];g=[]
#    for i in np.arange(limitt[0]+GDPdelta/2,limitt[2]-GDPdelta/2,GDPdelta):
#        for j in np.arange(limitt[1]+GDPdelta/2,limitt[3]-GDPdelta/2,GDPdelta):
#            dpop = 0; droad = 0;  #一个小区域（现在最初是方形）内  节点数 和 路长
#            x.append(i);y.append(j)
#            hits=list(idx.intersection(tuple(np.r_[i,j ,i,j])))
#            dpop = len(hits)
##===============如果为了加速这一段，完全可以把 每条路 也建在一个Rtree中，然后还是按顺序存一个 数组 放置其长度
#            #====这样只要一Intersecion就知道哪些是在某个区域内，然后把对应序号对应的长度取出来即可。。。现在1500点差不多算小1分钟，也还将就
#            if dpop!=0:
#                for m in range(len(weights)):
#                    if np.linalg.norm(weights[m][0] - np.array([i,j]))<=0.56418958315174811722429804605635:
#                        #                if np.linalg.norm(weights[m][0] - np.array([i,j]))<=0.5642:
#                        droad += weights[m][1] 
#            gdp[(i,j)] = dpop*droad
#            g.append(gdp[(i,j)])
##    print 'GDP every lattice   ',gdp
#    fp = open('gdp.csv','w')
#    print>>fp, 'x', ',',  'y',',', 'gdp'
#    for key in gdp:
#        print>>fp, key[0], ',',key[1],',', gdp[key]
#    fp.close()
#    
#    
#    plt.close('all') ######close all也#########
##=================像处理介数一样把GDP按颜色画出来===================
#    plt.figure(figsize=(L,L))
##    plt.figure()
#    #可能要存个字典之类。。。。
##    vmin = min(g)   #若normalized=True则介数均为小数，这样取作0也还能保证那些不那么小，只要能拉开梯度、又不至最小值为最小就行   #vmin = -min(ee.values())#vmin = -0.1*max(ee.values())
##    vmax = max(g)
#    g = np.array(g)
#    g = g/max(g)
##    colorvec = plt.cm.hot((max(g)-g)*128)
##    colorvec = plt.cm.hot(g*256)
#    colorvec = plt.cm.Reds(g) ###其实这样把数据归一化一下就可以了~~这样效果才更好，才能拉开梯度，上面两种都不对，结果就是只有两种值（可能本来须要输入的值就是0-1之间的吧）
##    G = 
#
##    print '\n\n\ng is', colorvec
#    plt.scatter(x,y, s=10000,marker='s', linewidths=0, color=colorvec, alpha = 1)
##    plt.axis('off')   #把透明度调为1，这样的情况下它就只会根据两个XY数据点间的距离来平均的分配了，就不会有重叠的问题啦，哈哈~~ 
##    name = 'gdp_illustrationN='+str(maxnode)+'.pdf'
##    name = 'gdp_illustrationN='+str(maxnode)+'-'+str(1000*random.random()%1000)+'.pdf'
#    name = 'gdp_illustrationN='+str(maxnode)+'-'+str(random.random())+'.pdf'
#    plt.savefig(name)
#
##    plt.scatter(x,y, s=1000,marker='s', linewidths=0, color=colorvec, norm = None, vmin=vmin, vmax=vmax, alpha = 0.3)
#                   #s是node_size之意
##==============路网按 介数 来画示意图==========================================================
#    netx = nx.Graph(network)
##     netx.add_edges_from(network) #从一个邻接数组中添加边
#    for u,d in netx.edges():
#        netx[u][d]['weight'] = np.linalg.norm(pos[u]-pos[d]) #算两点之间的距离 来赋权
#    edges = nx.edge_betweenness_centrality(netx, normalized=True,weight='weight')  #这里的weight是 是否有计算有权网的介数，所以那个Weight就必须算出相应的值来
# #    print 'edges = ', edges   #edges返回的是一个字典，键值是（1，2）这样的边tuple，值是相应的介数
#    for u,d in netx.edges():
#        netx[u][d]['color'] = edges[u,d] #直接用Color就行，在下面draw时给Edge_color赋值即可
#     #colors = range(len(edges))
#           #####     nx.draw(netx,pos,node_size=0,node_color='#A0CBE2',edge_color='#A0CBE2',   width=[float(d['weight']*0.2) for (u,v,d) in netx.edges(data=True)],   edge_cmap=plt.cm.Blues,with_labels=False)
#                      #width也和其它颜色之类的属性一样，可以给每个单独赋值，只要和ndlist一样就行    
#    print 'OOOKKK2'
##    plt.figure(figsize=(1,1))
#    plt.figure()
# #   plt.xlim(4985,5015)
# #   plt.ylim(4985,5015)
#

##    print netx.edges(data=True)
#    ee = dict( ((u,v),d['color']) for u,v,d in netx.edges(data=True) )
#    vmin = -0.081   #若normalized=True则介数均为小数，这样取作0也还能保证那些不那么小，只要能拉开梯度、又不至最小值为最小就行   #vmin = -min(ee.values())#vmin = -0.1*max(ee.values())
#    vmax = max(ee.values())
##    edge_colorvec = [plt.cm.Blues(ee[key]/vmax) for key in ee] #这样其实也可以，但对比度会有点太大，太深太浅都会有
##    nx.draw(netx,pos,node_size=0,node_color='b',width=1.2,edge_color=edge_colorvec, with_labels=False)
#    nx.draw(netx,pos,node_size=0,node_color='b',width=1.2,edge_color=[float(d['color']) for (u,v,d) in netx.edges(data=True)],edge_cmap=plt.cm.Blues,edge_vmin=vmin,edge_vmax=vmax,with_labels=False)
#
##    nx.draw(netx,pos,node_size=0,node_color='b',width=1.2,edge_color='gray',with_labels=False)#这个是画不按介数的
#    fp = open('roads.csv','w')
#    print>>fp, 'x1', ',',  'y1',',', 'x2', ',',  'y2',',', 'betweenness'
#    for key in ee:
#        print>>fp, pos[key[0]][0], ',', pos[key[0]][1], ',',pos[key[1]][0],',', pos[key[1]][1], ',', ee[key]
#    fp.close()
#
#    plt.gca()
#    plt.axis(axisbox) ##axisbox is (..,..,..,..)
#    plt.scatter(nds[:,0], nds[:,1], color='b',alpha=0.3)##draw nodes  #有alpha时"blues"居然报错了；是因为那个本来就是梯度之故？
##    name1 = 'roadVoronoi'+str(1000*random.random()%1000)+'.pdf'
#    name1 = 'roadVoronoiN='+str(maxnode)+'.pdf'
#    plt.savefig(name1)
#    plt.show()
#    
#    fp = open('nodes.csv','w')
#    print>>fp, 'x', ',',  'y'
#    for key in nds:
#        print>>fp, key[0], ',',key[1]
#    fp.close()
#    
##    pos = {}
##    lines, axisbox, network, weights, pos = voronoi2(nds,0) #这是啥啊？1，0
##    netx = nx.Graph(network)
#    
##    plt.figure(figsize=(L,L))
##    nx.draw(netx,pos,node_size=0,node_color='b',width=1.2,edge_color='gray',with_labels=False)
###    nx.draw(netx,pos,node_size=0,node_color='b',width=1.2,edge_color='gray',edge_cmap=plt.cm.gray,edge_vmin=vmin,edge_vmax=vmax,with_labels=False)
##    plt.axis(axisbox) ##axisbox is (..,..,..,..)
##    plt.scatter(nds[:,0], nds[:,1], color='b',alpha=0.4)##draw nodes
##    name2 = 'roadVoronoiNoOutline'+str(1000*random.random()%1000)+'.pdf' 
##    plt.savefig(name2)
##    plt.show()
#
##==============VornoiEvolve的统计性质============================================
##     results = np.array(results)
##     plt.figure() 
##     plt.scatter(results[:,0], results[:,1], color="red") 
##     ott, oaa = results[:,0], results[:,1]
##     plt.loglog(ott,oaa,'bo')
##     plt.hold(True)
##     bools=(ott>0)&(oaa>0)
##     xx=ott[bools]
##     yy=oaa[bools]
##     rr = leastsq(residuals,[1,1],args=(xx,yy))
##     print 'rr = ',rr
##     k,b=rr[0]
##     xplt=xx
##     yplt=xplt**k*np.exp(b)
##     plt.loglog(xplt,yplt)
##     name = 'MATCHING_L_n'+str(rr[0][0])+'n'+str(maxnode/10)+'_'+str(maxnode)+'.pdf'
## #    plt.savefig(name)
## #    plt.show
## 
##     results2 = np.array(results2)
##     plt.figure() 
##     plt.scatter(results2[:,0], results2[:,1], color="red") 
##     ott, oaa = results2[:,0], results2[:,1]
##     plt.loglog(ott,oaa,'bo')
##     plt.hold(True)
##     bools=(ott>0)&(oaa>0)
##     xx=ott[bools]
##     yy=oaa[bools]
##     rr = leastsq(residuals,[1,1],args=(xx,yy))
##     print 'rr = ',rr
##     k,b=rr[0]
##     xplt=xx
##     yplt=xplt**k*np.exp(b)
##     plt.loglog(xplt,yplt)
##     name = 'MATCHING_l_rou'+str(rr[0][0])+'n'+str(maxnode/10)+'_'+str(maxnode)+'.pdf'
##     plt.savefig(name)
## #    plt.show()
## 
##     #name1 = time.time()
##     name1 = 'MATCHING_n'+str(maxnode/10)+'_'+str(maxnode)+'.txt'
##     fp = open(name1,'w')
##     for i in range(np.size(results)/2):
##         print >>fp, results[i,0],'\t',results[i,1],'\t',results2[i,0],'\t',results2[i,1]
##    fp.close()
##==============================================================================
