# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Qui vanno i dati
# freQ
freQ = (
100,
200,
300,
400,
500,
600,
700,
900,
1E3,
1.2E3,
1.4E3,
1.7E3,
2.1E3,
2.8E3,
3.6E3,
5.7E3,
12.2E3)

# Vout./Vin
V = (
   0.992979,
   0.978916,
   0.955734,
   0.926337,
   0.890688,
   0.854675,
   0.816514,
   0.740513,
   0.704733,
   0.637397,
   0.578838,
   0.504167,
   0.426332,
   0.333683,
   0.265756,
   0.170168,
   0.082192)

# phi
phi = (
-5.5,
-11.1,
-16.9,
-21.9,
-26.9,
-31.3,
-35.9,
-42.8,
-45,
-50.1,
-54.5,
-60,
-64.6,
-70.3,
-75,
-80,
-85)

# dati
R = 997.81
C = 162E-9

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Grafico di casa gay",
    y=0.97, fontsize=15)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
ax1.set_xscale('log')
ax1.set_yscale('log')
# crea plot con le barre d'errore (o anche senza)
signal = ax1.errorbar(x=freQ, y=V,#**20,
    #yerr=dy, #xerr=,
    fmt='o', c='black')
teo1 = ax1.errorbar(x=[i for i in range(10, 100000)], y=[(1+(R*C*2*pi*i)**2)**(-0.5) for i in range(10, 100000)],
    fmt='-', c='red')
    
ax1.set_ylabel(u'Attenuazione segnale [$db$]',
    labelpad=2, fontsize=14)
ax1.set_xlabel(u'Frequenza [$\omega$]',
    labelpad=2, fontsize=14)
#ax1.yaxis.labelpad = 0

ax1.grid(True)
ax1.set_ylim((0.01, 2))
# questo produce una legenda
ax1.legend((signal, teo1), ("Dati sperimentali", "andamento teorico"), 'lower left',
    prop={'size': 12})
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
fase = ax2.errorbar(x=freQ, y=phi,
    #yerr=, #xerr=,
    fmt='o', c='black')
teo2 = ax2.errorbar(x=[i for i in range(10, 100000)], y=[360/pi/2*np.arctan(-2*pi*i*R*C) for i in range(10, 100000)],
    fmt='-', c='red')


ax2.set_ylabel(u'Fase [$\mu s$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$\omega$ ]', labelpad=2, fontsize=14)

#ax2.yaxis.set_label_position("right") # posiziona il label sulla destra
#ax2.yaxis.tick_right() # posiziona i ticks sulla destra
#ax2.set_yticks(np.arange(-18, 18.1, 3))
#ax2.set_yticks(np.arange(-70, 70.1, 10))
#ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

ax2.grid(True)
ax2.legend((fase, teo2), ("Dati sperimentali", "andamento teorico"), 'lower left',
    prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.94,
    top=0.92, bottom=0.10, hspace=0.25, wspace=0.05)
# mostra grafico
plt.show()
