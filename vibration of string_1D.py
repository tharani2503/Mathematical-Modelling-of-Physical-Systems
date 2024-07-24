delt=0.001 ## timestep
delx=0.01 ##element size
x=[i/100 for i in range(0,101)] ## grid points or nodes
##print(x)
ynow=[]
m1=1
m2=(1/8)
ynow=[(m1*i) for i in x[0:10]]
g=[m2*(1-i) for i in x[10:101]]
ynow.extend(g)
##print(ynow)
yprevious=ynow[:]
ynext=ynow[:]

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

for index in range(1,10):
    #s=(((delt**2)*(ynow[index+1]-2*ynow[index]+ynow[index-1]))/(delx**2))+(2*(ynow[index]))-(ynow[index])
##    ynext[index]=s
##    if len(ynext)==100:
##        ynext.append(0)
##        yprevious=ynow.copy()
##        ynow=ynext.copy()
##        #print(ynext)
##        ynext=[0]
    for i in range(1,100):
        y=(((delt**2)*(ynow[i+1]-2*ynow[i]+ynow[i-1]))/(delx**2))+(2*(ynow[i]))-(yprevious[i])
        ynext[i]= y
        
    yprevious=ynow[:]
    ynow=ynext[:]
##    print(ynext)
    ax.plot(x, ynext,index,linewidth=2.0)
    
plt.show()
#print(ynext)
