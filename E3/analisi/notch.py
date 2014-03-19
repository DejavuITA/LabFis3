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
6.9E3,
3.6E3,
2.35E3,
1.8E3,
1.4E3,
1.1E3,
900,
760,
640,
530,
450,
370,
300,
230,
170,
110,
50,
25,
14E3,
30E3,
42E3,
56E3,
72E3,
88E3,
105E3,
125E3,
140E3,
160E3,
190E3,
210E3,
240E3,
270E3,
300E3,
330E3,
370E3,
415E3,
530E3,
666E3,
900E3,
1.2E6,
1.6E6,
2.7E6,
7.0E6,
15.0E6)

# Vout./Vin
V = (
   0.0063291,
   0.0506329,
   0.1526316,
   0.2492114,
   0.3242392,
   0.4058577,
   0.4968750,
   0.5757261,
   0.6404959,
   0.7037037,
   0.7676561,
   0.8154944,
   0.8629442,
   0.9028340,
   0.9385081,
   0.9647887,
   0.9839196,
   0.9949799,
   0.9979920,
   0.0432489,
   0.1643836,
   0.2473684,
   0.3273872,
   0.4104712,
   0.4958246,
   0.5677083,
   0.6446281,
   0.6969072,
   0.7589744,
   0.8333333,
   0.8737271,
   0.9026369,
   0.9433198,
   0.9656912,
   0.9818548,
   0.9929648,
   0.9969758,
   0.9757576,
   0.9238579,
   0.8221994,
   0.7016632,
   0.5756303,
   0.3758099,
   0.1750000,
   0.1186441)

#V20 = ()

# phi
phi = (
-90,	
-84,	
-80,	
-75,	
-70.5,	
-65.5,	
-59.8,	
-54.7,	
-50.0,	
-45.2,	
-40.0,	
-35.2,	
-30.5,	
-24.5,	
-19.9,	
-15.0,	
-9.9,	
-4.8,	
-1.9,	
82,	
79,	
75.2,	
70.5,	
65.0,	
60.0,	
55.0,	
50.0,	
46.0,	
40.0,	
34.0,	
29.5,	
25.3,	
20.0,	
15.5,	
10.5,	
5.3,	
0.0,	
-10.0,	
-20.0,	
-31.0,	
-41.0,	
-50.0,	
-60.0,	
-60.0,	
-60.0)

# dati
R = 997.81
C = 250.4E-9
L = 1E-3

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Filtro a reiezione di banda",
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
teo1 = ax1.errorbar(x=[10*i for i in range(1, 10000000)], y=[((((2*pi*i*10*L-1/(2*pi*i*10*C)))**2)**(0.5)*(R*R + ((2*pi*i*10*L-1/(2*pi*i*10*C)))**2)**(-0.5)) for i in range(1, 10000000)],
    fmt='-', c='red')
    
ax1.set_ylabel(u'Attenuazione segnale [$db$]',
    labelpad=2, fontsize=14)
ax1.set_xlabel(u'Frequenza [$\omega$]',
    labelpad=2, fontsize=14)
#ax1.yaxis.labelpad = 0

ax1.grid(True)
ax1.set_ylim((0.005, 1.5))
ax1.get_yaxis().set_ticklabels(("-60", "-40", "-20", "0"))
# questo produce una legenda
ax1.legend((signal, teo1), ("Dati sperimentali", "andamento teorico"), 'lower right',
    prop={'size': 12})
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
fase = ax2.errorbar(x=freQ, y=phi,
    #yerr=, #xerr=,
    fmt='.', c='black')
teo2 = ax2.errorbar(x=[i*10 for i in range(1, 10000000)], y=[360/(pi*2)*np.arctan(R/(2*pi*i*10*L-1/(2*pi*i*10*C))) for i in range(1, 10000000)],
    fmt='-', c='red')


ax2.set_ylabel(u'Fase [$\mu s$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$\omega$ ]', labelpad=2, fontsize=14)

ax2.set_ylim((-91, 91))
#ax2.yaxis.set_label_position("right") # posiziona il label sulla destra
#ax2.yaxis.tick_right() # posiziona i ticks sulla destra
#ax2.set_yticks(np.arange(-18, 18.1, 3))
ax2.set_yticks(np.arange(-90, 91, 30))
#ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

ax2.grid(True)
ax2.legend((fase, teo2), ("Dati sperimentali", "andamento teorico"), 'upper right',
    prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.94,
    top=0.92, bottom=0.10, hspace=0.25, wspace=0.05)
# mostra grafico
plt.show()
