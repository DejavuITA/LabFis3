# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Qui vanno i dati
# freQ
freQ = (
#10E3,
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
#-43.973142,
  -25.911342,
  -16.327112,
  -12.068643,
   -9.782688,
   -7.832523,
   -6.075057,
   -4.795681,
   -3.869673,
   -3.052203,
   -2.296666,
   -1.771580,
   -1.280346,
   -0.887842,
   -0.551240,
   -0.311356,
   -0.140808,
   -0.043714,
   -0.017459,
  -27.280490,
  -15.682832,
  -12.133115,
   -9.698766,
   -7.734346,
   -6.093438,
   -4.917495,
   -3.813815,
   -3.136501,
   -2.395458,
   -1.583625,
   -1.172484,
   -0.889738,
   -0.506821,
   -0.303234,
   -0.159054,
   -0.061323,
   -0.026308,
   -0.213161,
   -0.687897,
   -1.700457,
   -3.077426,
   -4.797128,
   -8.500635,
  -15.139239,
  -18.515079)

# phi
phi = (
#-90,	
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
S = 2.41
D = 1.4E-10

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Filtro a reiezione di banda",
    y=0.97, fontsize=15)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
ax1.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
teo1 = ax1.errorbar(x=[i**2 for i in range(1, 4500)], y=[20*log10(np.absolute(((((2*pi*i**2*L-1/(2*pi*i**2*C)))**2)**(0.5)*(R*R + ((2*pi*i**2*L-1/(2*pi*i**2*C)))**2)**(-0.5)))) for i in range(1, 4500)],
     fmt=':', c='red')
teo1corr = ax1.errorbar(x=[i**2 for i in range(1, 4500)],
	y=[20*log10(np.absolute(( (S*(S+R) + ( 2*pi*i**2*L - 1/(2*pi*i**2*C) )**2 )**2 + ( R * (2*pi*i**2*L - 1/(2*pi*i**2*C) ) )**2 )**(0.5) * 1/(  ( 2*pi*i**2*L - 1/(2*pi*i**2*C) )**2 + (R+S)**2  ))) for i in range(1, 4500)],
    fmt='-.', c='blue')
teo1corr2 = ax1.errorbar(x=[i**2 for i in range(1, 4500)],
		y=[20*log10(np.absolute(
					sqrt((1 + (C + D)*(2*pi*i**2)**2*((C + D)*S**2 + L*(-2 + (C + D)*L*(2*pi*i**2)**2)))/
					(1 + (2*pi*i**2)**2*(D*(D*S**2 + L*(-2 + D*L*(2*pi*i**2)**2)) +
					2*C*(D*S**2 + L*(-1 + D*L*(2*pi*i**2)**2)) +
					C**2*(2*R*S + S**2 + L**2*(2*pi*i**2)**2 +
					R**2*(1 + D*(2*pi*i**2)**2*(D*S**2 + L*(-2 + D*L*(2*pi*i**2)**2)))))))
					))
 	for i in range(1, 4500)],
	fmt='-', c='green')
#teo1corr3 = ax1.errorbar(x=[i**2 for i in range(1, 4500)],
#		y=[20*log10(np.absolute(
#					sqrt((1 + C*(2*pi*i**2)**2*(C*S**2 + L*(-2 + C*L*(2*pi*i**2)**2)))/
#					(1 + (D**2*R**2 - 2*C*(L - D*R**2) + C**2*(R + S)**2)*(2*pi*i**2)**2 +
#					C*(L*(C*L - 2*D*(C + D)*R**2) + C*D**2*R**2*S**2)*(2*pi*i**2)**4 +
#					C**2*D**2*L**2*R**2*(2*pi*i**2)**6))
#					))
# 	for i in range(1, 4500)],
#	fmt='-', c='yellow')

gain = ax1.errorbar(x=freQ, y=V,
    #yerr=dy, #xerr=,
    fmt='.', c='black')

v0 = ax1.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')
#db = ax1.axhline(y=-3, linewidth=1, color='grey')
    
ax1.set_ylabel(u'Attenuazione segnale [$dB$]', labelpad=2, fontsize=14)

ax1.text(1/(2*pi*(L*C)**(0.5))+1000, -50+1.5, r'$\nu_0$', size=15, va='center')

ax1.grid(True)
ax1.set_ylim((-50, 1))
plt.setp(ax1.get_xticklabels(), visible=False)
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
teo2 = ax2.errorbar(x=[i**2 for i in range(1, 4500)], y=[360/(pi*2)*np.arctan(R/(2*pi*i**2*L-1/(2*pi*i**2*C))) for i in range(1, 4500)],
    fmt=':', c='red')
teo2corr = ax2.errorbar(x=[i**2 for i in range(1, 4500)],
	y=[360/(pi*2)*np.arctan(R*(2*pi*i**2*L-1/(2*pi*i**2*C))/(S*(R+S)+(2*pi*i**2*L-1/(2*pi*i**2*C))**2)) for i in range(1, 4500)],
    fmt='-.', c='blue')
teo2corr2 = ax2.errorbar(x=[i**2 for i in range(1, 4500)],
	y=[360/(pi*2)*np.arctan(
				(C*R*(2*pi*i**2)*(-1 + ((C + 2*D)*L - D*(C + D)*S**2)*(2*pi*i**2)**2 -
				D*(C + D)*L**2*(2*pi*i**2)**4))/
				(1 + (-2*(C + D)*L + C**2*R*S + (C + D)**2*S**2)*(2*pi*i**2)**2 +
				(C + D)**2*L**2*(2*pi*i**2)**4)
				) for i in range(1, 4500)],
	fmt='-', c='green')

fase = ax2.errorbar(x=freQ, y=phi,
    #yerr=, #xerr=,
    fmt='.', c='black')

v0 = ax2.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')
db = ax1.axhline(y=-3, linewidth=1, color='grey')

ax1.annotate("", (650, -3), xytext=(20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
ax1.annotate("", (141000, -3), xytext=(-20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))
ax1.text(1/(2*pi*(C*L)**(0.5))+500, -4.5, r'$\Delta\nu$', size=13, va='center')

ax2.set_ylabel(u'Fase [$^\circ$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$Hz$ ]', labelpad=2, fontsize=14)

ax2.set_ylim((-91, 91))
ax2.set_xlim((10,20000000))
#ax2.yaxis.set_label_position("right") # posiziona il label sulla destra
#ax2.yaxis.tick_right() # posiziona i ticks sulla destra
#ax2.set_yticks(np.arange(-18, 18.1, 3))
ax2.set_yticks(np.arange(-90, 91, 30))
#ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

ax2.grid(True)
ax2.legend((fase, teo2, teo2corr, teo2corr2), ("Dati sperimentali", "andamento teorico", r'correzione con resistenza $R_L$', r'correzione con $R_L$ e $C_p$'), 'upper left',
    prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.96,
    top=0.94, bottom=0.08, hspace=0.05, wspace=0.05)
# mostra grafico
plt.show()
