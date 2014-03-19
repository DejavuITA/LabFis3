# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Qui vanno i dati
# freQ
freQ = (
10E3,	
10.06E3,
9.97E3,
9.92E3,
9.87E3,
9.81E3,
9.75E3,
9.68E3,
9.62E3,
9.54E3,
9.43E3,
9.31E3,
9.14E3,
8.89E3,
8.53E3,
7.93E3,
6.47E3,
4E3,
2E3,
1E3,
500,
100,
10.1E3,
10.16E3,
10.20E3,
10.27E3,
10.32E3,
10.38E3,
10.45E3,
10.53E3,
10.63E3,
10.71E3,
10.85E3,
11.01E3,
11.22E3,
11.54E3,
12.07E3,
13.11E3,
15.94E3,
23E3,
39E3,
50E3)

# Vout./Vin
V = (
   0.5821355,
   0.5876923,
   0.5745118,
   0.5621788,
   0.5458290,
   0.5232198,
   0.4963806,
   0.4647300,
   #0.6455331,
   0.4376299,
   0.4041667,
   0.3622129,
   0.3242678,
   0.2780693,
   0.2276551,
   0.1773684,
   0.1264489,
   0.0680380,
   0.0210970,
   0.0105485,
   0.0042150,
   0.0027397,
   0.0015717,
   0.5846154,
   0.5790554,
   0.5724563,
   0.5504115,
   0.5381443,
   0.5175620,
   0.4896480,
   0.4600208,
   0.4229167,
   0.3956159,
   0.3556485,
   0.3137461,
   0.2712934,
   0.2231579,
   0.1719409,
   0.1191983,
   0.0675818,
   0.0274841,
   0.0137566,
   0.0093122)

V20 = (
   1.9975e-05,
   2.4155e-05,
   1.5345e-05,
   9.9424e-06,
   5.5098e-06,
   2.3642e-06,
   8.2470e-07,
   2.2081e-07,
   6.6396e-08,
   1.3527e-08,
   1.5111e-09,
   1.6523e-10,
   7.6394e-12,
   1.3981e-13,
   9.4957e-16,
   1.0922e-18,
   4.5188e-24,
   3.0509e-34,
   2.9096e-40,
   3.1324e-48,
   5.6773e-52,
   8.4637e-57,
   2.1747e-05,
   1.7964e-05,
   1.4284e-05,
   6.5125e-06,
   4.1493e-06,
   1.9022e-06,
   6.2760e-07,
   1.8011e-07,
   3.3504e-08,
   8.8201e-09,
   1.0481e-09,
   8.5421e-11,
   4.6643e-12,
   9.3809e-14,
   5.1002e-16,
   3.3528e-19,
   3.9500e-24,
   6.0485e-32,
   5.8916e-38,
   2.4045e-41)

# phi
phi = (
7,	
0,	
10,	
15,	
20,	
25.5,	
30,	
35.5,	
40,	
44.4,	
50,	
55,	
60,	
65,	
70,	
75,	
80,	
82,	
77,	
67,	
51,	
13,	
-4.5,	
-10.5,	
-14.5,	
-20,	
-25,	
-30.5,	
-35.2,	
-40.4,	
-45.7,	
-49.7,	
-55.1,	
-60,	
-65,	
-70.3,	
-75,	
-80,	
-85.2,	
-88,	
-89,	
-89)

# dati
R = 997.81
C = 250.4E-9
L = 1E-3

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Filtro passa banda",
    y=0.97, fontsize=15)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
ax1.set_xscale('log')
ax1.set_yscale('log')
# crea plot con le barre d'errore (o anche senza)
signal = ax1.errorbar(x=freQ, y=V,#V20,
    #yerr=dy, #xerr=,
    fmt='.', c='black')
teo1 = ax1.errorbar(x=[i for i in range(10, 100000)], y=[(((L/C/(2*pi*i*L-1/(2*pi*i*C)))**2)**(0.5)*(R*R + (L/C/(2*pi*i*L-1/(2*pi*i*C)))**2)**(-0.5)) for i in range(10, 100000)],
    fmt='-', c='red')
    
ax1.set_ylabel(u'Attenuazione segnale [$db$]',
    labelpad=2, fontsize=14)
ax1.set_xlabel(u'Frequenza [$\omega$]',
    labelpad=2, fontsize=14)
#ax1.yaxis.labelpad = 0

ax1.grid(True)
ax1.set_ylim((0.001, 1.5))
ax1.get_yaxis().set_ticklabels(("-60", "-40", "-20", "0"))
# questo produce una legenda
ax1.legend((signal, teo1), ("Dati sperimentali", "andamento teorico"), 'upper center',
    prop={'size': 12})
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
fase = ax2.errorbar(x=freQ, y=phi,
    #yerr=, #xerr=,
    fmt='.', c='black')
teo2 = ax2.errorbar(x=[i for i in range(10, 100000)], y=[360/(pi*2)*np.arctan(-R*C/L*(2*pi*i*L-1/(2*pi*i*C))) for i in range(10, 100000)],
    fmt='-', c='red')


ax2.set_ylabel(u'Fase [$\mu s$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$\omega$ ]', labelpad=2, fontsize=14)

#ax2.yaxis.set_label_position("right") # posiziona il label sulla destra
#ax2.yaxis.tick_right() # posiziona i ticks sulla destra
#ax2.set_yticks(np.arange(-18, 18.1, 3))
#ax2.set_yticks(np.arange(-70, 70.1, 10))
#ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

ax2.grid(True)
ax2.legend((fase, teo2), ("Dati sperimentali", "andamento teorico"), 'lower center',
    prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.94,
    top=0.92, bottom=0.10, hspace=0.25, wspace=0.05)
# mostra grafico
plt.show()
