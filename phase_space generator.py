import numpy as np
import matplotlib.pyplot as plt


m=1                     #mass
l=1                     #length
g=9.8                   #gravititional acc.
to=0                    #initial time
t=[to]                  #time_list
tf=3                    #final time
lo=10000 
h=(tf-to)/lo            #time step

mu=5                    #angle_devider 1 (for the final angle limit)
ji=2                    #angle_devider 2 (for the additive angle term)

theta_int=[-mu*np.pi]   #list of all initial thetas 
theta=[]                #actual angle change for every theta_int 
vo=-4                   #initial velocity
v_int=[vo]              #list of all initial velocities
v=[]                    #actual velocity change for every v_int

delta_v=0.25            #the separation between velocities
kkl=0                   #counter 1
counter=0               #counter 2

print('total number of plots=',(mu)*4*(-vo/delta_v)*ji)


#================================================================
#================Auto-generating the initial conditions==========
#================and solving them using Euler's method===========
#================================================================


while round(v_int[kkl],2) < -vo:
    
    j=0
    while round(theta_int[j],2)!= round(np.pi*mu,2):
        theta=[]
        theta.append(theta_int[j])
        v=[]
        v.append(v_int[kkl])
        i=0
        while round(t[i],2) != tf:
            v.append(-h*(g/l)*np.sin(theta[i])+v[i])
            theta.append(theta[i]+h*v[i])
            t.append(t[i]+h)
            i+=1
        k=0
        w=[]
        while k != len(v):
            w.append((m*l**2)*v[k])
            k+=1
        counter+=1
        i=0
        print(counter,'plots have been done')
        plt.plot(theta,w,'k')   
        theta_int.append(theta_int[j]+np.pi/ji)
        j+=1
        v=[]
    v_int.append(v_int[kkl]+delta_v)
    kkl+=1
#=================================================================
#===============plotting the results==============================
#=================================================================

plt.grid()
plt.xlabel('theta')
plt.ylabel('p_theta')
plt.show()

