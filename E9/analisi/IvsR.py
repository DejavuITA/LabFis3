from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt(	"../dati/E9_dc.csv",
			delimiter=',',skip_header=1,names=True)
R = data1['Resistenza']
I = data1['Corrente']


rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle(r"Corrente $I_L$ in funzione della resistenza dicarico $R_L$",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)

Vcc= 9.93
Ra= 1000+200
data = ax1.errorbar(	x=R, y=I/1000, fmt='-', c='#A0A0A0', linewidth=1)
linear = ax1.errorbar(	x=np.arange(9000,52000,1),
			y=1000*Vcc/(Ra+np.arange(9000,52000,1)),
			fmt='--', c='green', linewidth=2)
data = ax1.errorbar(	x=R, y=I/1000, fmt='.', c='#000000', linewidth=2)
#    markersize=7, markeredgewidth=1)

ax1.text(25000, 0.12, r'$R_L$ [Ω]', ha='center', va='center', fontsize=16)
ax1.set_ylabel(r'$I_L$ [mA]', labelpad=0, fontsize=16)

ax1.set_xlim((-1000,51000))
ax1.set_ylim((0.15,0.9))
ax1.set_xticklabels(('0','0','10k','20k','30k','40k','50k'))

ax1.grid(True)

# questo produce una legenda
ax1.legend((data, linear), (r'dati sperimentali', r'andamento ohmico'), 'upper right', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.07, right=0.98,
    top=0.92, bottom=0.07, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
