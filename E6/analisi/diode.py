from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

data1 = np.genfromtxt("../dati/diode_fw.csv", delimiter=',', skip_header=1, names=True)
data2 = np.genfromtxt("../dati/diode_back.csv", delimiter=',', skip_header=1, names=True)
diodeV2 = data2['VDC']
diodeV1 = data1['VDC']
diodeI2 = data2['IDC']
diodeI1 = data1['IDC']

M = (0.706-0.346)/(1.19-1.00)
Q = 0.346 - M*1.00

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Caratteristica volt-amperometrica di un diodo 1N4007",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)

slope = ax1.errorbar(x=np.arange(0.5,1.5,0.01), y=Q+M*np.arange(0.5,1.5,0.01),
    fmt='-', c='gray', linewidth=2)
ax1.axvline(x=-Q/M, c='black', linewidth=1, linestyle='dashed')

############### ---- ###############
# sto provando a ricreare la legge #
#   teorica ma con poco successo   #
############### ---- ###############
Is = 10**(-10)
q = 1.602176565*10**(-19)
K = 1.3806488*10**(-16)
T = 300
#Vt = 1000*K*T/q*1000*1000*1000*1000*1000*1000*1000*1000*1000*1000
Vt = K*1.3806488*1.602176565
Vt = 10**(-3)
Is = 10**(-12)

A=4.649E-08
B=0.05543
C=0.3755

teo = ax1.errorbar(
	x=B*np.log((np.arange(-0,0.8,0.001)/A+1))+C*np.arange(-0,0.8,0.001),
	y=np.arange(-0,0.8,0.001),
	fmt='-', c='green', linewidth=2)

#ax1.errorbar(	x=np.arange(-3,2,0.05),
#		y=np.arange(-3,2,0.05)*0.5,
#	fmt='*--', c='blue', linewidth=2)
############### ---- ###############
#             diamine!             #
############### ---- ###############

ax1.errorbar(x=diodeV1, y=diodeI1,
    fmt='o', c='red', linewidth=2)
#    markersize=7, markeredgewidth=1)
diode = ax1.errorbar(x=diodeV2, y=diodeI2,
    fmt='o--', c='red', linewidth=2)

ax1.set_xlabel(u'd.d.p. [V]',
    labelpad=8, fontsize=16)
ax1.set_ylabel(u'Intensità di corrente [mA]',
    labelpad=8, fontsize=16)

ax1.set_xlim((-2.1,1.25))
ax1.set_ylim((-0.04,0.74))

ax1.grid(True)

# questo produce una legenda
ax1.legend((diode, teo), ("diodo 1N4007", "fit teorico"), 'upper left', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.08, right=0.97,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)

# mostra grafico
plt.show() 
