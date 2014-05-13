from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt("../dati/circ1.csv", delimiter=',',skip_header=1,names=True)
ib = data1['ib']
ic = data1['ic']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 45/8), dpi=65)
# Titolo del grafico
f1.suptitle("Transistor BC107B\nCorrente di base in funzione di corrente di collettore",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)
m= 12/0.039
slope = ax1.errorbar(x=np.arange(-0.1,0.1,0.01), y=m*np.arange(-0.1,0.1,0.01),
		fmt='-', c='black', linewidth=2)
sat = ax1.errorbar(x=ib, y=ic-ib,
    fmt='o--', c='grey', linewidth=2)

#ax1.set_xlabel(r'$I_B$ [mA]', labelpad=8, fontsize=16)		# Vers.1
#ax1.text(-0.13, 6.7, r'$I_C$ [mA]', rotation='vertical',	# Vers.1
#	ha='center', va='center', fontsize=15)
ax1.text(0.5, -1.5, r'$I_B$ [mA]', rotation='horizontal',	# Vers.2
	ha='center', va='center', fontsize=15)
ax1.text(-0.08, 6.7, r'$I_C$ [mA]', rotation='vertical',	# Vers.2
	ha='center', va='center', fontsize=15)


#ax1.set_xlim((-0.05,2.05))					# Vers.1
ax1.set_xlim((-0.04,1.054))					# Vers.2
ax1.set_ylim((-0.6,14.0))

#ax1.set_xticks((-50,-40,-30,-20,-10,0,4.8,5.75))
#ax1.set_xticklabels(('-50','-40','-30','-20','-10','0','4.8',''))

#ax2 = ax1.twin()

ax1.grid(True)

# questo produce una legenda
ax1.legend((sat, ), ("corrente di collettore", ), 'lower right', prop={'size': 16})

# questo imposta i bordi del grafico
#f1.subplots_adjust(left=0.06, right=0.98,			# Vers.1
#    top=0.88, bottom=0.11, hspace=0.08, wspace=0)		# Vers.1
f1.subplots_adjust(left=0.06, right=0.98,			# Vers.2
    top=0.88, bottom=0.09, hspace=0.08, wspace=0)		# Vers.2

# mostra grafico
plt.show()
