import matplotlib.pyplot as plt
import numpy as np
import math

A_path = '/home/harrisonh/Code/GFW1/DoitEXPERIMENT/SLAC'
ND1 = '/1_35_small/'
ND2 = '/1_35_mid/'
ND3 = '/1_35_big/'
ND4 = '/1_35_huge/'

TEXTFILE = 'dE.txt'

l=1
beta = 0.99999
x_1= [0 for i in range(137)]
#print ND_path

dataset1=np.genfromtxt(fname=A_path+ ND1 +TEXTFILE, skip_header=1)
dataset2=np.genfromtxt(fname=A_path+ ND2 +TEXTFILE, skip_header=1)
dataset3=np.genfromtxt(fname=A_path+ ND3 +TEXTFILE, skip_header=1)
dataset4=np.genfromtxt(fname=A_path+ ND4 +TEXTFILE, skip_header=1)

#print datase

#Convert angles to wavelength (mm)
#for n in range(137):
  #x[n]= l*((1/beta)-math.cos(math.radians(x1[n])))

x1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] 
x2 = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4] 
x3 = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5] 
x4 =  [0, 1, 2, 3, 4, 5, 6, 7]
x = np.concatenate((x1, x2, x3, x4), axis=0)
indexs = x.argsort()
x_order = x[indexs]

y1 =dataset1[8, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[8, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[8, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[8, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y40 = np.concatenate((y1, y2, y3, y4), axis=0)
y40_order = y40[indexs]
y40_norm = (y40_order - np.min(y40_order))/(np.max(y40_order)-np.min(y40_order))

y1 =dataset1[18, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[18, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[18, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[18, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y50 = np.concatenate((y1, y2, y3, y4), axis=0)
y50_order = y50[indexs]
y50_norm = (y50_order - np.min(y50_order))/(np.max(y50_order)-np.min(y50_order))

y1 =dataset1[28, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[28, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[28, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[28, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y60 = np.concatenate((y1, y2, y3, y4), axis=0)
y60_order = y60[indexs]
y60_norm = (y60_order - np.min(y60_order))/(np.max(y60_order)-np.min(y60_order))

y1 =dataset1[38, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[38, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[38, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[38, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y70 = np.concatenate((y1, y2, y3, y4), axis=0)
y70_order = y70[indexs] 
y70_norm = (y70_order - np.min(y70_order))/(np.max(y70_order)-np.min(y70_order))

y1 =dataset1[48, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[48, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[48, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[48, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y80 = np.concatenate((y1, y2, y3, y4), axis=0)
y80_order = y80[indexs] 
y80_norm = (y80_order - np.min(y80_order))/(np.max(y80_order)-np.min(y80_order))

y1 =dataset1[58, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[58, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[58, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[58, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y90 = np.concatenate((y1, y2, y3, y4), axis=0)
y90_order = y90[indexs] 
y90_norm = (y90_order - np.min(y90_order))/(np.max(y90_order)-np.min(y90_order))

y1 =dataset1[68, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[68, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[68, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[68, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y100 = np.concatenate((y1, y2, y3, y4), axis=0)
y100_order = y100[indexs] 
y100_norm = (y100_order - np.min(y100_order))/(np.max(y100_order)-np.min(y100_order))
y1 =dataset1[78, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[78, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[78, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[78, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y110_order = np.concatenate((y1, y2, y3, y4), axis=0)
y110_norm = (y110_order - np.min(y110_order))/(np.max(y110_order)-np.min(y110_order))

y1 =dataset1[88, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[88, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[88, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[88, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y120 = np.concatenate((y1, y2, y3, y4), axis=0)
y120_order = y120[indexs]
y120_norm = (y120_order - np.min(y120_order))/(np.max(y120_order)-np.min(y120_order))

y1 =dataset1[98, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[98, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[98, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[98, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y130 = np.concatenate((y1, y2, y3, y4), axis=0)
y130_order = y130[indexs]
y130_norm = (y130_order - np.min(y130_order))/(np.max(y130_order)-np.min(y130_order))

y1 =dataset1[108, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[108, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[108, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[108, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y140 = np.concatenate((y1, y2, y3, y4), axis=0)
y140_order = y140[indexs]
y140_norm = (y140_order - np.min(y140_order))/(np.max(y140_order)-np.min(y140_order))

y1 =dataset1[118, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[118, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[118, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[118, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y150 = np.concatenate((y1, y2, y3, y4), axis=0)
y150_order = y150[indexs]

y1 =dataset1[128, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[128, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[128, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[128, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y160 = np.concatenate((y1, y2, y3, y4), axis=0)
y160_order = y160[indexs]

y1 =dataset1[136, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y2 = dataset2[136, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y3 = dataset3[136, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y4 = dataset4[136, [ 1, 2, 3, 4, 5, 6, 7, 8]]
y170 = np.concatenate((y1, y2, y3, y4), axis=0)
y170_order = y170[indexs]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#ax.scatter(x,10E300*y, label = '$42^{\circ}$', linewidths=scalar)
#ax.plot(x_order, y40_order, label = r'$\theta = 40^{\circ}$')
#ax.plot(x_order, y50_order, label = r'$\theta = 50^{\circ}$')
#ax.plot(x_order, y60_order, label = r'$\theta = 60^{\circ}$')
#ax.plot(x_order, y70_order, label = r'$\theta = 70^{\circ}$')
#ax.plot(x_order, y80_order, label = r'$\theta = 80^{\circ}$')
ax.plot(x_order, y90_order, label = r'$\theta = 90^{\circ}$')
ax.plot(x_order, y100_order, label = r'$\theta = 100^{\circ}$')
ax.plot(x_order, y110_order, label = r'$\theta = 110^{\circ}$')
ax.plot(x_order, y120_order, label = r'$\theta = 120^{\circ}$')
ax.plot(x_order, y130_order, label = r'$\theta = 130^{\circ}$')
ax.plot(x_order, y140_order, label = r'$\theta = 140^{\circ}$')
ax.plot(x_order, y150_order, label = r'$\theta = 150^{\circ}$')
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




