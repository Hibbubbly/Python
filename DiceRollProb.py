# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Calculates the probability of rolling multiple die
https://digitalscholarship.unlv.edu/cgi/viewcontent.cgi?article=1025&context=grrj
https://www.geeksforgeeks.org/multiply-two-polynomials-2/
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# Inputs

def Roll(RollInput,Score=0,FullResults=False):
    """
    Roll inputs and caller function
    """  
    ListInput=RollInput.rsplit(",")
    NumDie=0
    TotalMod=0
    DiceArray=[]
    for i in ListInput:
        j=i.split("d")
        k=j[1].split("+")
        NumDie+=int(j[0])
        try:
            TotalMod+=int(k[1])
        except:
            pass
        DiceArray.extend([int(k[0])]*int(j[0]))

    # Constants
    SingProb=1/DiceArray[0]
    for m in range(1,NumDie):
        SingProb*=1/(DiceArray[m])
    
    """
    Polynomial Mutliplication
    """
    # Initialise dice coefficient polynomials
    DieXArr=[]
    index=0
    for die in DiceArray:
        DieYArr=[]
        for x in range(1,DiceArray[index]+1):
            DieYArr.append(1)
        DieXArr.append(DieYArr)
        index+=1        
    
    # Create multiplication polynomials
    # Die1
    prod1=[0]*(DiceArray[0])
    for i in range(DiceArray[0]):
        prod1[i]+=DieXArr[0][i]
    
    # Iterate other die
    prodX=prod1
    for x in range(1,NumDie):
        if DiceArray[x]>0:
            prodY=[0]*(len(prodX)+DiceArray[x]-1)
            for i in range(len(prodX)):
                for j in range(DiceArray[x]):
                    prodY[i+j]+=prodX[i]*DieXArr[x][j]
            prodX=prodY 
    
    """
    Probability Distribution
    """
    # Generate Roll Index
    DieSum=0
    for i in DiceArray:
        DieSum+=i
    Offset=NumDie+TotalMod-1
    DiceRoll=[0]*(DieSum+TotalMod)
    for k in range(DieSum+TotalMod):
        DiceRoll[k]=k+1
    
    # Generate Probability Distribution   
    ProbDis=[]
    CumProbDis=[]
    InvCumProbDis=[]
    CumProb=0
    InvCumProb=1
    ProbDis2=[0]*Offset   
    ProbDis2.extend(prodX)
    for k in range(len(ProbDis2)):
        y=SingProb*ProbDis2[k]
        CumProb+=y
        InvCumProb-=y
        ProbDis.append(y)
        CumProbDis.append(CumProb)
        InvCumProbDis.append(InvCumProb)
    
    # Plot Probability Distribution
    plt.figure()
    ax1=plt.subplot(211)
    line1,=ax1.plot(DiceRoll,ProbDis)
    ax2=plt.subplot(212,sharex=ax1)
    ax1.xaxis.set_visible(False)
    line2,=ax2.plot(DiceRoll,InvCumProbDis)
    ax1.set_ylabel('Probability of Roll\n')
    ax2.set_ylabel('Cumulative Probability\nof Exceedance')
    ax2.set_xlabel('Sum of Dice Scores')
    ax2.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.subplots_adjust(hspace=.0)

    if Score>0:
        print(InvCumProbDis[Score-1])
        
    if FullResults==True:
        Results=np.zeros((len(DiceRoll),2))
        for i in range(0,len(DiceRoll)):
            Results[i][0]=DiceRoll[i]
            Results[i][1]=InvCumProbDis[i]
        np.set_printoptions(formatter={'float':'{:0.3f}'.format})
        #np.set_printoptions(precision=5,floatmode='maxprec')
        #np.set_printoptions(formatter={'float_kind':'{:f}'.format})
        print(Results)
