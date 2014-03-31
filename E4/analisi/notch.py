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

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Filtro a reiezione di banda", y=0.97, fontsize=15)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
ax1.set_xscale('log')

R=0.980E3
C=0.099E-6
A = (R*C*2*pi*np.logspace(2,5,500))**2

teo1 = ax1.errorbar(x=np.logspace(2,5,500),
y=20*np.log10(( (A)**4 + 6*(A)**3 - 5*(A)**2 + 6*(A) + 1 )**(0.5) * ( 2*(A)**2 + 14*(A) + 2)**(-1)),
 fmt='-', c='blue')
gain = ax1.errorbar(x=FREQ, y=20*np.log10(VM/(V2*2)),
    #yerr=dy, #xerr=,
    fmt='.', c='black')
#boja = ax1.errorbar(x=np.logspace(2,5,500), y=20*np.log10(1/2 *(1 - (8 *A)/(1 + 7 *A + A**2))**(0.5)),
#    fmt='--', c='red')

#v0 = ax1.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')
#db = ax1.axhline(y=-3, linewidth=1, color='grey')
    
ax1.set_ylabel(u'Attenuazione segnale [$dB$]', labelpad=2, fontsize=14)

#ax1.text(1/(2*pi*(L*C)**(0.5))+1000, -50+1.5, r'$\nu_0$', size=15, va='center')

ax1.grid(True)
ax1.set_ylim((-16, -5))
plt.setp(ax1.get_xticklabels(), visible=False)
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
fase = ax2.errorbar(x=FREQ, y=-PHI,
    #yerr=, #xerr=,
    fmt='.', c='black')

wrc = R*C*2*pi*np.logspace(2,5,500)
teo2 = ax2.errorbar(x=np.logspace(2,5,500),
y=180/pi*np.arctan(1/(3*wrc)-wrc/3),
 fmt='-', c='blue')
#varphi=ax2.errorbar(x=np.logspace(2,5,500),
#y=180/pi*np.arctan(2*wrc*(wrc**2-1)/(wrc**4+wrc**2+1)),
# fmt='-.', c='red')

#v0 = ax2.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')
#db = ax1.axhline(y=-3, linewidth=1, color='grey')

#ax1.annotate("", (650, -3), xytext=(20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
#ax1.annotate("", (141000, -3), xytext=(-20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
#ax1.text(1/(2*pi*(C*L)**(0.5))+500, -4.5, r'$\Delta\nu$', size=13, va='center')

ax2.set_ylabel(u'Fase $CH_{1}|CH_{2}$ [$^\circ$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$Hz$]', labelpad=2, fontsize=14)

ax2.set_ylim((-91, 91))
#ax2.set_xlim((10,20000000))
ax2.set_yticks(np.arange(-90, 91, 30))

ax2.grid(True)
ax2.legend((fase,teo2), ("Dati sperimentali", "Andamento teorico"), 'upper right', prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.96, top=0.94, bottom=0.08, hspace=0.05, wspace=0.05)
# mostra grafico
plt.show()
