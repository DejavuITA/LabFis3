# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Qui vanno i dati
# Valori teorici delle resistenze
Rt = (
   983000,
   99820,
   9937.0,
   999.00,
   98.880,
   9.9700,
   1.0410)

# Valori sperimentali delle resistenze - NON CORRETTI
Rm_rough = (
   975610,
   100000,
   10000,
   1052.6,
   105.26,
   17.391,
   7.5676)
Rv_rough = (
   166670,
   90909,
   9756.1,
   1026.3,
   101.05,
   9.3617,
   0.86957)

Rm = (
   973610,
   99411,
   9936.5,
   989.14,
   98.868,
   10.996,
   1.1726)
Rv = (
   1000000,
   100000,
   9852.2,
   1031.6,
   101.10,
   9.3639,
   0.86994)

# Errore sui valori delle resistenze
dRm = (
   17037,
   1767.8,
   176.78,
   29.738,
   2.3790,
   0.47410,
   0.55013)
dRv = (  
   111570,
   1858.3,
   173.75,
   29.884,
   2.3611,
   0.43724,
   0.21779)

# scarti
scar_Rm = ( #(R_teo .- R_corr_monte)./R_teo * 100
   0.95526,
   0.40954,
   0.0049109,
   0.98663,
   0.011976,
  -10.294,
  -12.639)
dscar_Rm = ( # dR_corr_monte.*100./R_teo;
    1.7332,
    1.7710,
    1.7790,
    2.9768,
    2.4060,
    4.7553,
   52.8462)
scar_Rv = ( #(R_teo .- R_corr_valle)./R_teo * 100
   -1.72940,
   -0.18032,
    0.85321,
   -3.26422,
   -2.24890,
    6.07930,
   16.43194)
dscar_Rv = ( # dR_corr_valle.*100./R_teo;
   11.3505,
    1.8616,
    1.7485,
    2.9914,
    2.3879,
    4.3855,
   20.9208)

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 6))
# Titolo del grafico
f1.suptitle("Valori di resistenza teorici e sperimentali",
    y=0.97, fontsize=15)

######
# GRAFICO 1 - grafico R-R
ax1 = f1.add_subplot(1, 2, 1)
ax1.set_xscale('log')
ax1.set_yscale('log')
# crea plot con le barre d'errore (o anche senza)
rough_monte = ax1.errorbar(x=Rt, y=Rm_rough,
    #yerr=dy, #xerr=,
    fmt='.:', c='red')
rough_valle = ax1.errorbar(x=Rt, y=Rv_rough,
    #yerr=dy, #xerr=,
    fmt='.:', c='green')
monte = ax1.errorbar(x=Rt, y=Rm,
    yerr=dRm, #xerr=,
    fmt='s:', c='black')
valle = ax1.errorbar(x=Rt, y=Rv,
    yerr=dRv, #xerr=,
    fmt='o:', c='grey')
    
ax1.set_xlabel(u'Resistenza teorica [$\Omega$]',
    labelpad=2, fontsize=14)
ax1.set_ylabel(u'Resistenza misurata [$\Omega$]',
    labelpad=2, fontsize=14)
#ax1.yaxis.labelpad = 0

ax1.grid(True)
ax1.set_ylim((0.6, 1800000))
ax1.set_xlim((0.6, 1800000))
# questo produce una legenda
ax1.legend((valle, monte, rough_valle, rough_monte), ("amperometro a valle", "amperometro a monte", "'a valle' non corretto", "'a monte' non corretto"), 'lower right',
    prop={'size': 12})
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(1, 2, 2)
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
scar_monte = ax2.errorbar(x=Rt, y=scar_Rm,
    yerr=dscar_Rm, #xerr=,
    fmt='o-', c='black')
scar_valle = ax2.errorbar(x=Rt, y=scar_Rv,
    yerr=dscar_Rv, #xerr=,
    fmt='.-', c='grey')

ax2.set_xlabel(u'Resistenza teorica [$\Omega$]',
    labelpad=2, fontsize=14)
ax2.set_ylabel(u'Scarto percentuale [%]',
    labelpad=2, fontsize=14)
ax2.yaxis.set_label_position("right") # posiziona il label sulla destra
ax2.yaxis.tick_right() # posiziona i ticks sulla destra
ax2.set_yticks(np.arange(-18, 18.1, 3))
#ax2.set_yticks(np.arange(-70, 70.1, 10))
#ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

ax2.grid(True)
ax2.set_ylim((-18, 18))
#ax2.set_ylim((-70, 70))
ax2.set_xlim((0.6, 1800000))
# questo produce una legenda
ax2.legend(( scar_valle, scar_monte), ("amperometro a valle", "amperometro a monte"), 'lower center',
    prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.07, right=0.94,
    top=0.92, bottom=0.10, hspace=5, wspace=0.05)
# mostra grafico
plt.show()
