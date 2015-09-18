import matplotlib as plt
import pylab
import numpy


A_path = '/home/harrisonh/Code/GFW1/LetsFixThisCode/SAWorECHELLE'
ND1 = '/SLAC_1.5_ECHELLE/'
ND2 = '/SLAC_1.5_SAW/'

TEXTFILE = 'pol.txt'
xcol = 0
ycol = 8
n = 0
m = 0
k =0

beta = 0.99999
l1 = 0.5
l2 = 1
l3 = 1.5 #all gratings here are 1.5mm
x_1= [0 for i in range(142)]
x_2= [0 for i in range(142)]
#x_3= [0 for i in range(142)]


#print ND_path

dataset1=numpy.genfromtxt(fname=A_path+ ND1 +TEXTFILE, skip_header=1)
dataset2=numpy.genfromtxt(fname=A_path+ ND2 +TEXTFILE, skip_header=1)


#print dataset

x1=dataset1[:, xcol]
x2=dataset2[:, xcol]
#x3=dataset3[:, xcol]

#Convert angles to wavelength (mm)

for k in range(0, 142):
  x_1[k]= l3*((1/beta)-numpy.cos(numpy.radians(x1[k])))

y1=dataset1[:, ycol]
y2=dataset2[:, ycol] 


fig = pylab.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x_1, y1, label =  '$ECHELLE$', linewidth = 1.5)
ax.plot(x_1, y2, label = '$SAW$', linewidth = 0.5)

ax.set_xlim([0, 2])

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
#ax.spines['left'].set_smart_bounds(True)
#ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

xticks = ax.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)

ax.set_title('Degree of Polarisation of SPR for \n Different Grating Periodicities', fontname='Times New Roman', weight='bold', fontsize = '16' )
ax.set_xlabel('Wavelength (mm)', fontname='Times New Roman', fontsize = '14')
ax.set_ylabel('Degree of polarisation', fontname='Times New Roman', fontsize = '14')
ax.legend(loc = 4)

pylab.show()




