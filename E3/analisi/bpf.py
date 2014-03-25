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
   -4.6995,
   -4.6170,
   -4.8140,
   -5.0025,
   -5.2589,
   -5.6263,
   -6.0837,
   -6.6560,
   -7.1779,
   -7.8688,
   -8.8207,
   -9.7819,
  -11.1169,
  -12.8545,
  -15.0225,
  -17.9617,
  -23.3450,
  -33.5156,
  -39.5362,
  -47.5041,
  -51.2459,
  -56.0724,
   -4.6626,
   -4.7456,
   -4.8452,
   -5.1862,
   -5.3820,
   -5.7208,
   -6.2023,
   -6.7445,
   -7.4749,
   -8.0545,
   -8.9796,
  -10.0684,
  -11.3312,
  -13.0278,
  -15.2924,
  -18.4746,
  -23.4034,
  -31.2184,
  -37.2298,
  -40.6190)

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
S = 2.41

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Filtro passa banda",
    y=0.97, fontsize=15)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
ax1.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
teo1 = ax1.errorbar(x=[i**2 for i in range(8, 1000)],
y=[20*log10(
			np.absolute(
							(
								(
									(
										L/
										C/
										(2*pi*i**2*L-1/(2*pi*i**2*C))
									)**2
								)**(0.5)
								*
								(
									R*R
									+
									(
										L/
										C/
										(2*pi*i**2*L-1/(2*pi*i**2*C))
									)**2
								)**(-0.5)
							)
						)
			) for i in range(8, 1000)],
    fmt='-.', c='red')

teo1corr = ax1.errorbar(x=[i**2 for i in range(8, 1000)],
	y=[10*log10(((L**2)*((i**2)**2)*4*pi**2+S**2)/((R+S)**2+(((i**2)**2)*4*pi**2)*(L**2+C*(L*(-2+C*L*((i**2)**2)*4*pi**2)+C*S**2)*(R**2))))
	for i in range(8,1000)],
    fmt='-', c='blue')
signal = ax1.errorbar(x=freQ, y=V,
    #yerr=dy, #xerr=,
    fmt='.', c='black')

dbv0 = 10*log10(((L**2)*((1/(2*pi*(C*L)**(0.5)))**2)*4*pi**2+S**2)/((R+S)**2+(((1/(2*pi*(C*L)**(0.5)))**2)*4*pi**2)*(L**2+C*(L*(-2+C*L*((1/(2*pi*(C*L)**(0.5)))**2)*4*pi**2)+C*S**2)*(R**2))))-3
v0 = ax1.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')
db = ax1.axhline(y=dbv0, linewidth=1, color='grey')
ax1.annotate("", (10680, dbv0), xytext=(20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
ax1.annotate("", (9555, dbv0), xytext=(-20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
ax1.text(11400, dbv0+3, r'$\Delta\nu$', size=13, va='center')


    
ax1.set_ylabel(u'Attenuazione segnale [$dB$]', labelpad=2, fontsize=14)

ax1.text(1/(2*pi*(L*C)**(0.5))+500, -60+1.5, r'$\nu_0$', size=15, va='center')

ax1.grid(True)
ax1.set_ylim((-60, 1))
#ax1.get_yaxis().set_ticklabels(("-60", "-40", "-20", "0"))
#ax1.legend((signal, teo1), ("Dati sperimentali", "andamento teorico"), 'upper center', prop={'size': 12})
plt.setp(ax1.get_xticklabels(), visible=False)
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
teo2 = ax2.errorbar(x=[i**2 for i in range(8, 1000)], y=[360/(pi*2)*np.arctan(-R*C/L*(2*pi*i**2*L-1/(2*pi*i**2*C))) for i in range(8, 1000)],
    fmt='-.', c='red')
teo2corr = ax2.errorbar( x=[i**2 for i in range(8, 1000)], y=[360/(2*pi)*np.arctan(((i**2)*2*pi*(L-C*L**2*(i**2)**2*4*pi**2-C*S**2)*R)/(L**2*(i**2)**2*4*pi**2+S*(S+R))) for i in range(8,1000)],
    fmt='-', c='blue')

fase = ax2.errorbar(x=freQ, y=phi,
    #yerr=, #xerr=,
    fmt='.', c='black')

v0 = ax2.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')

ax2.set_ylabel(u'Fase [$^\circ$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$Hz$]', labelpad=2, fontsize=14)

#ax2.set_yticks(np.arange(-18, 18.1, 3))
ax2.set_yticks(np.arange(-90, 90.1, 30))
ax2.set_ylim((-93,93))
ax2.set_xlim((64,100000))
#ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

ax2.grid(True)
ax2.legend((fase, teo2, teo2corr), ("Dati sperimentali", "andamento teorico", r'correzione con resistenza $R_L$ parassita'), 'lower left',
    prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.96,
    top=0.94, bottom=0.08, hspace=0.05, wspace=0.05)
# mostra grafico
plt.show()
