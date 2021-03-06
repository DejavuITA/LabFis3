# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt

# Qui vanno i dati
# Voltaggio e corrente a monte
Vm = (   
	1.88,
	2.8,
	3.9,
	4.8,
	5.8,
	6.8,
	7.8,
	8.6,
	9.6,
	11,
	11.5,
)

Im = (
	19,
	22,
	26.5,
	30.5,
	34,
	37,
	40,
	43,
	45.5,
	48,
	50,
)

dVm = (
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.500000,
	0.500000,
	0.500000,
)

dI = (
	0.500000,
	0.500000,
	0.500000,
	0.500000,
	0.500000,
	0.500000,
	0.500000,
	0.500000,
	0.500000,
	0.500000,
	0.500000,
)

# Voltaggio e corrente a valle
Vv = (
	2,
	3,
	4,
	5,
	6,
	7,
	8,
	9,
	10,
	11,
	12,
)

Iv = (
	19,
	22,
	26.5,
	30.5,
	34,
	37,
	40,
	43,
	45.5,
	48,
	50,
)

dVv = (
	0.020000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.100000,
	0.500000,
	0.500000,
)

# errori dI + dV
dyM = (
   0.50043,
   0.50902,
   0.50781,
   0.50714,
   0.50658,
   0.50614,
   0.50578,
   0.50554,
   0.50528,
   0.61241,
   0.61241)
dyV = (
   0.51072,
   0.50907,
   0.50805,
   0.50734,
   0.50681,
   0.50639,
   0.50604,
   0.50575,
   0.62328,
   0.61894,
   0.61894)


# plot teorico
a = 12.679670971
b = 0.56232
a2 = 11.931715227
b2 = 0.58327

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(11, 6))
# Titolo del grafico
f1.suptitle("Caratteristica volt-amperometrica di una lampadina",
    y=0.96, fontsize=15)


# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)
# crea plot con le barre d'errore (o anche senza)
monte = ax1.errorbar(x=Vm, y=Im,
    yerr=dyM, #xerr=dVm,
    fmt='s:', c='black')
valle = ax1.errorbar(x=Vv, y=Iv,
    yerr=dyV, #xerr=dVv,
    fmt='o:', c='grey')
teo1   = ax1.errorbar(x=[i/1000 for i in range(1000, 14000)], y=[a*(i/1000)**(b) for i in range(1000, 14000)],
        fmt='-', c='#666666')
#teo2   = ax1.errorbar(x=[i/1000 for i in range(1000, 14000)], y=[a2*(i/1000)**(b2) for i in range(1000, 14000)],
#        fmt='-', c='#CC6600')
    
ax1.set_xlabel(u'Differenza di potenziale [V]',
    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Intensità di corrente [mA]',
    labelpad=6, fontsize=14)

ax1.grid(True)
ax1.set_ylim((0, 55))
ax1.set_xlim((1.2, 12.8))
# questo produce una legenda
ax1.legend((valle, monte, teo1), ("configurazione amperomentro a valle", "configurazione amperomentro a monte", "fit configurazione a monte:\n$I=aV^{\,b}$ con $a=12.7$ e $b=0.56$"), 'lower right',
    prop={'size': 12})

ax1.annotate('cambio fondoscala', ((9.65, 43)), xytext=(25, -60), 
    textcoords='offset points', arrowprops=dict(facecolor='black',arrowstyle='-|>', connectionstyle="arc3,rad=-0.4"))
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.07, right=0.97,
    top=0.90, bottom=0.12, hspace=0, wspace=0.1)
# mostra grafico
plt.show()  

