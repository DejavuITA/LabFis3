from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt("../dati/E6_zener.csv", delimiter=',',skip_header=1,names=True)
Vin = data1['Vin']
Vout = data1['Vout']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Stabilizzatore di corrente",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)

# crea plot con le barre d'errore (o anche senza)

#ax1.axhline(y=-25.5, xmin=0.865, xmax=1, c='black',linewidth=1,linestyle='dashed')
#ax1.axvline(x=5.75, ymin=0, ymax=0.4875, c='black',linewidth=1,linestyle='dashed')

zener = ax1.errorbar(x=Vin, y=Vout,
    fmt='o--', c='blue', linewidth=2)
#    markersize=7, markeredgewidth=1)

ax1.set_xlabel(u'd.d.p. [V]',
    labelpad=8, fontsize=16)
ax1.set_ylabel(u'd.d.p. [V]',
    labelpad=-4, fontsize=16)

#ax1.text(8.3, -16,r'$I_{@P_{max}}$', horizontalalignment='left', verticalalignment='center', fontsize=20)

#ax1.annotate(r'$I_{sc}$', xy=(5.75, 0),  xycoords='data',
#                xytext=(5.75-10, 50), textcoords='data',
#		va='center', fontsize=20,
#                arrowprops=dict(arrowstyle="->",
#                                )
#                )

ax1.set_xlim((-0.4,20.4))
ax1.set_ylim((-0.3,6.8))

#ax1.set_xticks((-50,-40,-30,-20,-10,0,4.8,5.75))
#ax1.set_xticklabels(('-50','-40','-30','-20','-10','0','4.8',''))
#ax1.set_yticks((-100,-50,-25.5,-20.6,0,50,100))
#ax1.set_yticklabels(('-100','-50','','-20.6','0','50','100'))

# ax2 is responsible for "top" axis and "right" axis
#ax2 = ax1.twin()
#ax2.set_yticks((-100,-50,-25.5,-20.6,0,50,100))
#ax2.set_yticklabels(("","","-25.5",))
#ax2.set_xticks((-50,-40,-30,-20,-10,0,4.8,5.75))
#ax2.set_xticklabels(('','','','','','','','5.75'))

ax1.grid(True)

# questo produce una legenda
ax1.legend((zener, ), ("diodo zener", ), 'lower right', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.06, right=0.97,
    top=0.93, bottom=0.10, hspace=0, wspace=0)

# mostra grafico
plt.show()
