from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

data4 = np.genfromtxt("../dati/n4.csv", delimiter=',', skip_header=1, names=True)
t4 = data4['second']
V4 = data4['Volt']

data5 = np.genfromtxt("../dati/n5.csv", delimiter=',', skip_header=1, names=True)
t5 = data5['second']
V5 = data5['Volt']

data6 = np.genfromtxt("../dati/n6.csv", delimiter=',', skip_header=1, names=True)
t6 = data6['second']
V6 = data6['Volt']

data7 = np.genfromtxt("../dati/n7.csv", delimiter=',', skip_header=1, names=True)
t7 = data7['second']
V7 = data7['Volt']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Caratteristica volt-amperometrica di un diodo 1N4007",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)

dati4 = ax1.errorbar(x=t4, y=V4, fmt='-', c='blue', linewidth=2)
dati5 = ax1.errorbar(x=t5, y=V5, fmt='x-', c='blue', linewidth=2)

dati6 = ax1.errorbar(x=t6, y=V6,
    fmt='-', c='blue', linewidth=2)
#    markersize=7, markeredgewidth=1)
dati7 = ax1.errorbar(x=t7, y=V7,
    fmt='-', c='#000000', linewidth=2)

ax1.set_xlabel(u'Tempo [s]',
    labelpad=8, fontsize=16)
ax1.set_ylabel(u'd.d.p. [V]',
    labelpad=0, fontsize=16)

ax1.set_xlim((-0.01,0.01))
ax1.set_ylim((-0.1,10.5))

ax1.grid(True)

# questo produce una legenda
ax1.legend((dati6, dati7), ("Ia serie di dati", "IIa serie di dati"), 'upper left', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.08, right=0.97,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
