from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

data1 = np.genfromtxt("../dati/night_cell_back.csv", delimiter=',', skip_header=1, names=True)
data2 = np.genfromtxt("../dati/night_cell_fw.csv", delimiter=',', skip_header=1, names=True)
nightV1 = data1['VDC']
nightV2 = data2['VDC']
nightI1 = data1['IDC']
nightI2 = data2['IDC']

data3 = np.genfromtxt("../dati/light_cell_back.csv", delimiter=',', skip_header=1, names=True)
data4 = np.genfromtxt("../dati/light_cell_fw.csv", delimiter=',', skip_header=1, names=True)
lightV1 = data3['VDC']
lightV2 = data4['VDC']
lightI1 = data3['IDC']
lightI2 = data4['IDC']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Caratteristica volt-amperometrica di un diodo 1N4007",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)

night = ax1.errorbar(x=nightV1, y=nightI1,
    fmt='o--', c='blue', linewidth=2)
#    markersize=7, markeredgewidth=1)
ax1.errorbar(x=nightV2, y=nightI2,
    fmt='o--', c='blue', linewidth=2)

light = ax1.errorbar(x=lightV1, y=lightI1,
    fmt='o--', c='red', linewidth=2)
#    markersize=7, markeredgewidth=1)
ax1.errorbar(x=lightV2, y=lightI2,
    fmt='o--', c='red', linewidth=2)

ax1.set_xlabel(u'd.d.p. [V]',
    labelpad=8, fontsize=16)
ax1.set_ylabel(u'Intensità di corrente [mA]',
    labelpad=0, fontsize=16)

ax1.set_xlim((-51,8))
ax1.set_ylim((-65,105))

ax1.grid(True)

# questo produce una legenda
ax1.legend((night, light), ("cella solare protetta da radiazioni", "cella solare esposta a luce"), 'upper left', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.08, right=0.97,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)

# mostra grafico
plt.show() 
