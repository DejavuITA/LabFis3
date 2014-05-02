from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt("../dati/scope_5_2.csv", delimiter=',',names=True)
Vin1 = data1['peak1']
Vout1 = data1['peak2']
data2 = np.genfromtxt("../dati/scope_5_3.csv", delimiter=',',names=True)
Vin2 = data2['peak1']
Vout2 = data2['peak2']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 45/8), dpi=65)
# Titolo del grafico
f1.suptitle("emitter follower con partitore",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)

Hz2 = ax1.errorbar(x=Vin1, y=Vout1, fmt='o--', c='blue', linewidth=2)
Hz10 = ax1.errorbar(x=Vin2, y=Vout2, fmt='o--', c='red', linewidth=2)

ax1.text(3,-0.2, r'$V_{in}$ [$V$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
ax1.text(0.65, 2.6, r'$V_{out}$ [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

ax1.set_xlim(0.8,5.2)
ax1.set_ylim(0.2,5.0)
#ax1.set_xticks((-50,-40,-30,-20,-10,0,4.8,5.75))
#ax1.set_xticklabels(('-50','-40','-30','-20','-10','0','4.8',''))

#ax2 = ax1.twin()

ax1.grid(True)

# questo produce una legenda
ax1.legend((Hz2, Hz10), ("2 Hz", "10 Hz"), 'lower right', prop={'size': 16})

# bordi
f1.subplots_adjust(left=0.06, right=0.98,
    top=0.92, bottom=0.11, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
