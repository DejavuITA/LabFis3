from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

data1 = np.genfromtxt("../dati/scope_a_0.csv", delimiter=',', skip_header=1, names=True)
t1 = data1['second']
V1 = data1['Volt']

data2 = np.genfromtxt("../dati/scope_a_1.csv", delimiter=',', skip_header=1, names=True)
t2 = data2['second']
V2 = data2['Volt']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Forma d'onda trasformata dal ponte di Graetz",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)

dati1 = ax1.errorbar(x=1000*t1, y=-V1,
    fmt='-', c='grey', linewidth=2)
#    markersize=7, markeredgewidth=1)
dati2 = ax1.errorbar(x=1000*t2, y=V2,
    fmt='-', c='blue', linewidth=2)

ax1.set_xlabel(u'Tempo [ms]',
    labelpad=8, fontsize=16)
ax1.set_ylabel(u'd.d.p. [V]',
    labelpad=-8, fontsize=16)

ax1.set_xlim((-26,26))
ax1.set_ylim((-12,12))

ax1.grid(True)

# questo produce una legenda
ax1.legend((dati1, dati2), ("V generatore", "V carico"), 'lower left', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.06, right=0.98,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
