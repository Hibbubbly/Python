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
# Inputs

# Dice scores from 1 to:
NumDie=3

Die1=6
Die2=6
Die3=6
Die4=0
Die5=0
Die6=0
Die7=0
Die8=0
Die9=0
Die10=0

# Constants
DiceArray=[Die1,Die2,Die3,Die4,Die5,Die6,Die7,Die8,Die9,Die10]
SingProb=1/Die1
for m in range(1,NumDie):
    SingProb*=1/(DiceArray[m])
"""
Polynomial Mutliplication
"""
# Initialise dice coefficient polynomials
Die1Arr=[]
for x in range(1,Die1+1):
    Die1Arr.append(1)
Die2Arr=[]   
for x in range(1,Die2+1):
    Die2Arr.append(1)
Die3Arr=[]    
for x in range(1,Die3+1):
    Die3Arr.append(1)
Die4Arr=[] 
for x in range(1,Die4+1):
    Die4Arr.append(1)  
Die5Arr=[] 
for x in range(1,Die5+1):
    Die5Arr.append(1)
Die6Arr=[] 
for x in range(1,Die6+1):
    Die6Arr.append(1)
Die7Arr=[] 
for x in range(1,Die7+1):
    Die7Arr.append(1)
Die8Arr=[] 
for x in range(1,Die8+1):
    Die8Arr.append(1)    
Die9Arr=[] 
for x in range(1,Die9+1):
    Die9Arr.append(1)    
Die10Arr=[] 
for x in range(1,Die10+1):
    Die10Arr.append(1)   

# Create multiplication polynomials
# Die1*Die2
prod2 = [0]*(Die1+Die2-1)
for i in range(Die1):
    for j in range (Die2):
        prod2[i+j]+=Die1Arr[i]*Die2Arr[j]
# prod2*Die3
if Die3>0:   
    prod3 = [0]*(len(prod2)+Die3-1)
    for i in range(len(prod2)):
        for j in range (Die3):
            prod3[i+j]+=prod2[i]*Die3Arr[j]
else:
    prod3=[1]
# prod3*Die4
if Die4>0:
    prod4 = [0]*(len(prod3)+Die4-1)
    for i in range(len(prod3)):
        for j in range (Die4):
            prod4[i+j]+=prod3[i]*Die4Arr[j]
else:
    prod4=prod3
# prod4*Die5
if Die5>0:
    prod5 = [0]*(len(prod4)+Die5-1)
    for i in range(len(prod4)):
        for j in range (Die5):
            prod5[i+j]+=prod4[i]*Die5Arr[j]
else:
    prod5=prod4
# prod5*Die6
if Die6>0:
    prod6 = [0]*(len(prod5)+Die6-1)
    for i in range(len(prod5)):
        for j in range (Die6):
            prod6[i+j]+=prod5[i]*Die6Arr[j]
else:
    prod6=prod5
# prod6*Die7
if Die7>0:
    prod7 = [0]*(len(prod6)+Die7-1)
    for i in range(len(prod6)):
        for j in range (Die7):
            prod7[i+j]+=prod6[i]*Die7Arr[j]
else:
    prod7=prod6
# prod7*Die8
if Die8>0:
    prod8 = [0]*(len(prod7)+Die8-1)
    for i in range(len(prod7)):
        for j in range (Die8):
            prod8[i+j]+=prod7[i]*Die8Arr[j]
else:
    prod8=prod7
# prod8*Die9
if Die9>0:
    prod9 = [0]*(len(prod8)+Die9-1)
    for i in range(len(prod8)):
        for j in range (Die9):
            prod9[i+j]+=prod8[i]*Die9Arr[j]
else:
    prod9=prod8
# prod9*Die10
if Die10>0:
    prod10 = [0]*(len(prod9)+Die10-1)
    for i in range(len(prod9)):
        for j in range (Die10):
            prod10[i+j]+=prod9[i]*Die10Arr[j]
else:
    prod10=prod9


"""
Probability Distribution
"""
# Generate Roll Index
DieSum=Die1+Die2+Die3+Die4+Die5+Die6+Die7+Die8+Die9+Die10
Offset=NumDie-1

DiceRoll=[0]*DieSum
for k in range(DieSum):
    DiceRoll[k]=k+1

# Generate Probability Distribution   
ProbDis=[]
CumProbDis=[]
InvCumProbDis=[]
CumProb=0
InvCumProb=1
ProbDis2=[0]*Offset   
ProbDis2.extend(prod10)
for k in range(len(ProbDis2)):
    y=SingProb*ProbDis2[k]
    CumProb+=y
    InvCumProb-=y
    ProbDis.append(y)
    CumProbDis.append(CumProb)
    InvCumProbDis.append(InvCumProb)

# Plot Probability Distribution
fig=plt.figure()
ax1=plt.subplot(211)
line1,=ax1.plot(DiceRoll,ProbDis)
ax2=plt.subplot(212,sharex=ax1)
line2,=ax2.plot(DiceRoll,InvCumProbDis)
ax1.set_ylabel('Probability of Roll\n')
ax2.set_ylabel('Cumulative Probability\nof Exceedance')
ax2.set_xlabel('Sum of Dice Scores')
plt.subplots_adjust(hspace=.0)
