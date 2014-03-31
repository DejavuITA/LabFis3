# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Qui vanno i dati
dati = np.genfromtxt("../dati/dati_notch.csv", delimiter=',')

V1 = dati[:,0]
V2 = dati[:,1]
VM = dati[:,2]
PHI = dati[:,3]
FREQ = dati[:,4]

dati2 = np.genfromtxt("../dati/phi.csv", delimiter=',')
phaser = dati2[:]

R=0.980E3
C=0.099E-6

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 4))
# Titolo del grafico
f1.suptitle("Sfasamento tra segnali di input e output del filtro", y=0.97, fontsize=15)

######
# GRAFICO 1
ax2 = f1.add_subplot(1, 1, 1)
ax2.set_xscale('log')
fase = ax2.errorbar(x=FREQ, y=phaser,
    #yerr=, #xerr=,
    fmt='.', c='black')

wrc = R*C*2*pi*np.logspace(2,5,500)
teo2 = ax2.errorbar(x=np.logspace(2,5,500),
y=180/pi*np.arctan(2*wrc*(wrc**2-1)/(wrc**4+wrc**2+1)),
 fmt='--', c='blue')

#v0 = ax2.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')
#db = ax1.axhline(y=-3, linewidth=1, color='grey')

#ax1.annotate("", (650, -3), xytext=(20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
#ax1.annotate("", (141000, -3), xytext=(-20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
#ax1.text(1/(2*pi*(C*L)**(0.5))+500, -4.5, r'$\Delta\nu$', size=13, va='center')

ax2.set_ylabel(u'Fase [$^\circ$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$Hz$]', labelpad=-10, fontsize=14)

ax2.set_ylim((-46, 46))
#ax2.set_xlim((10,20000000))
ax2.set_yticks(np.arange(-45, 46, 15))

ax2.grid(True)
ax2.legend((fase,teo2), ("Dati sperimentali", "Andamento teorico"), 'lower right', prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.96, top=0.91, bottom=0.12, hspace=0.05, wspace=0.05)
# mostra grafico
plt.show()
