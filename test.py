import matplotlib.pyplot as plt
import numpy as np
import math

A_path = '/home/harrisonh/Code/GFW1/LetsFixThisCode/TESTRESULTS'
ND1 = '/AP_SMALL/'
ND2 = '/AP_MID/'
ND3 = '/AP_BIG/'


TEXTFILE = 'dE.txt'

l=1
beta = 0.99999
x_1= [0 for i in range(142)]
#print ND_path

dataset1=np.genfromtxt(fname=A_path+ ND1 +TEXTFILE, skip_header=1)
dataset2=np.genfromtxt(fname=A_path+ ND2 +TEXTFILE, skip_header=1)
dataset3=np.genfromtxt(fname=A_path+ ND3 +TEXTFILE, skip_header=1)


#print datase

#Convert angles to wavelength (mm)
#for n in range(142):
  #x[n]= l*((1/beta)-math.cos(math.radians(x1[n])))

x1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] 
x2 = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4] 
x3 =  [0, 1, 2, 3, 4, 5, 6, 7]
x = np.concatenate((x1, x2, x3),  axis=0)
indexs = x.argsort()
x_order = x[indexs]

y1 =dataset1[8, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[8, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[8, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y40 = np.concatenate((y1, y2, y3), axis=0)
y40_order = y40[indexs]
y40_norm = (y40_order - np.min(y40_order))/(np.max(y40_order)-np.min(y40_order))




#y1 =dataset1[58, [ 1, 2, 3, 4, 5, 6, 7, 8]]
#y2 = dataset2[58, [ 1, 2, 3, 4, 5, 6, 7, 8]]
#y3 = dataset3[58, [ 1, 2, 3, 4, 5, 6, 7, 8]]

#y90 = np.concatenate((y1, y2, y3), axis=0)
#y90_order = y90[indexs] 
#y90_norm = (y90_order - np.min(y90_order))/(np.max(y90_order)-np.min(y90_order))



fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#ax.scatter(x,10E300*y, label = '$42^{\circ}$', linewidths=scalar)
ax.plot(x_order, y40_order, label = r'$\theta = 40^{\circ}$')

ax.plot(x1, y1, label = r'$y1$')
ax.plot(x2, y2, label = r'$y2$')
ax.plot(x3, y3, label = r'$y3$')
#ax.plot(x_order, y80_order, label = r'$\theta = 80^{\circ}$')
#ax.plot(x_order, y90_order, label = r'$\theta = 90^{\circ}$')
#ax.plot(x_order, y100_order, label = r'$\theta = 100^{\circ}$')
#ax.plot(x_order, y110_order, label = r'$\theta = 110^{\circ}$')
#ax.plot(x_order, y120_order, label = r'$\theta = 120^{\circ}$')
#ax.plot(x_order, y130_order, label = r'$\theta = 130^{\circ}$')
#ax.plot(x_order, y140_order, label = r'$\theta = 140^{\circ}$')
#ax.plot(x_order, y150_order, label = r'$\theta = 150^{\circ}$')
#ax.plot(x_order, y160_order, label = r'$\theta = 160^{\circ}$')
#ax.plot(x_order, y170_order, label = r'$\theta = 170^{\circ}$')
#ax.set_xlim([0, 3])
#ax.set_ylim([0, 1.1])
#ax.set_yscale('log')
ax.set_title('Azimuthal Distribution of Energy of SPR \n for Several Different Detectors', fontname='Times New Roman', weight='bold', fontsize = '16' )
ax.set_xlabel('Azimuthal Angle $\phi$ (degrees)', fontname='Times New Roman', fontsize = '14')
ax.set_ylabel(r'Differential (Total) Energy (Joules)', fontname='Times New Roman', fontsize = '14')
ax.legend(loc = 1)
plt.show()




