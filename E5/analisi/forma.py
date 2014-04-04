from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

data = np.genfromtxt("../dati/scope_4.csv", delimiter=',', skip_header=1, names=True)
TIM = data['xaxis']
CH1 = data['y1']
CH2 = data['y2']

rcParams['font.size'] = 15
### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Forma d'onda",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)

CH1 = ax1.errorbar(x=TIM*10**(3), y=CH1,#+0.6,
    fmt='-', c='#888888', linewidth=2)
#    markersize=7, markeredgewidth=1)
CH2 = ax1.errorbar(x=TIM*10**(3), y=CH2,#-0.6,
    fmt='--', c='red', linewidth=2)

annDt = ax1.annotate('', xy=(8.75, -1),  xycoords='data',
                xytext=(17.25, -1), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->",
                           #     connectionstyle="bar",
                           #     ec="k",
                           #     shrinkA=5, shrinkB=5,
                                )
                )
textDt = ax1.annotate(r'$\Delta$ t', xy=(13,-1.5), xytext=None, xycoords='data', textcoords='data', arrowprops=None, va='center', ha='center')

annTau = ax1.annotate('', xy=(7.25, +1),  xycoords='data',
                xytext=(17.25, +1), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->",
                           #     connectionstyle="bar",
                           #     ec="k",
                           #     shrinkA=5, shrinkB=5,
                                )
                )
textTau = ax1.annotate(r'$t_{att}$', xy=(12.25,+2), xytext=None, xycoords='data', textcoords='data', arrowprops=None, va='center', ha='center')
    
ax1.set_ylabel(u'd.d.p. [V]',
    labelpad=10, fontsize=16)
ax1.set_xlabel(u'Tempo [ms]',
    labelpad=8, fontsize=14)


ax1.grid(True)

# questo produce una legenda
ax1.legend((CH1, CH2), ("CH1", "CH2"), 'upper left', prop={'size': 12})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.95,
    top=0.92, bottom=0.12, hspace=0.08, wspace=0)

# mostra grafico
plt.show() 
