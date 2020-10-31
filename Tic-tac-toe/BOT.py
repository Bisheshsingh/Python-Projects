import random

'INFININITE VALUE'
inf=1000000

'MAIN BRAIN OF TIC TAC TOE'
def brain(l,p,d,al,bt):
    if cheakwinner(l)!=0:
        return cheakwinner(l) 
    if moveavl(l):
        return 0
    if p:
        best=-inf
        for i in range(9):
            if l[i]==8:
                l[i]=p
                best=max(best,brain(l,1-p,d+1,al,bt))
                al=max(best,al)
                l[i]=8
                if bt<=al:
                    break
        return best
    else:
        best=inf
        for i in range(9):
            if l[i]==8:
                l[i]=p
                best=min(best,brain(l,1-p,d+1,al,bt))
                bt=min(best,bt)
                l[i]=8  
                if bt<=al:
                    break   
        return best
    
'REFINING ITS DECISION'
def decision(l):
    bv=-inf
    k=-1
    for i in range(9):
        if l[i]==8:
            l[i]=1
            mv=brain(l,0,0,-inf,inf)
            l[i]=8
            if mv>bv:
                k=i+1
                bv=mv
    return k

'BOT2'
def decision1(l):
    a=[]
    for i in range(9):
        if l[i]==8:
            a.append(i)
    return a[random.randint(0,len(a)-1)]+1

'EVALUATES THE BOARD'
def boardevaluation(l,v):
    if l[0]==v and l[3]==v and l[6]==v:
        return True
    if l[1]==v and l[4]==v and l[7]==v:
        return True
    if l[2]==v and l[5]==v and l[8]==v:
        return True
    if l[0]==v and l[1]==v and l[2]==v:
        return True
    if l[3]==v and l[4]==v and l[5]==v:
        return True
    if l[6]==v and l[7]==v and l[8]==v:
        return True
    if l[0]==v and l[4]==v and l[8]==v:
        return True
    if l[6]==v and l[4]==v and l[2]==v:
        return True
    return False

'CHECK WINNER'
def cheakwinner(l):
    if boardevaluation(l,0):
        return -10
    elif boardevaluation(l,1):
        return 10
    else:
        return 0
    
'CHECKS FOR MOVES AVAILABLE OR NOT'
def moveavl(l):
    return 8 not in l
    

    

   
    
        


                
                
    
