deltat=0.001
deltax=0.01
Time=1 ## simulation time
nt=int((Time)/(deltat)) ## no of timesteps
 ##totalsimulation time

T=1     ##tension in the string
munot=5 ##lineardensity
beta=0.1    ##coefficient of damping
x=[float(i/100) for i in range(0,101)]
m1=1
m2=1/9
unow=[(m1*i) for i in x[0:11]]
u2=[(m2*(1-i))for i in x[11:101]]
unow.extend(u2)
uprevious=unow.copy()
unext=unow[:]

for t in range(0,nt):
   
    for ui in range(1,100):
        
        u=(((((deltat**2)*(T))/(deltax**2)*(munot)))*((unow[ui+1])-(2*unow[ui])+(unow[ui-1]))-(uprevious[ui])+(2*(unow[ui])))
        unext[ui]=u
    print(unext)
        
    uprevious=unow.copy()
    unow=unext.copy()


     
        

