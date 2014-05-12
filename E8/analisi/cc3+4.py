from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

#### dati del cc3 ####
data1 = np.genfromtxt("../dati/scope_3_1.csv",delimiter=',',skip_header=1,names=True)
t_1 = data1['x']
V1_1 = data1['1']
V2_1 = data1['2']
#data2 = np.genfromtxt("../dati/scope_3_1.csv",delimiter=',',skip_header=1,names=True)
#t_2 = data2['x']
#V1_2 = data2['1']
#V2_2 = data2['2']
#i dati sono praticamente uguali!!!
#### dati del cc4 ####
data3 = np.genfromtxt("../dati/scope_4_1.csv",delimiter=',',skip_header=1,names=True)
t_3 = data3['x']
V1_3 = data3['1']
V2_3 = data3['2']
data4 = np.genfromtxt("../dati/scope_4_2.csv",delimiter=',',skip_header=1,names=True)
t_4 = data4['x']
V1_4 = data4['1']
V2_4 = data4['2']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(15, 7), dpi=65)
# Titolo del grafico
f1.suptitle("emitter follower semplice e polarizzato", y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(121, axes_class=AA.Axes)

in1 = ax1.errorbar(x=t_1*10**6, y=V1_1, fmt='-', c='blue', linewidth=2)
out1 = ax1.errorbar(x=t_1*10**6, y=V2_1, fmt='--', c='red', linewidth=2)

#in2 = ax1.errorbar(x=t_2, y=-V1_2, fmt='-', c='green', linewidth=2)
#out2 = ax1.errorbar(x=t_2, y=-V2_2, fmt='-', c='yellow', linewidth=2)

ax1.text(0, -6.8, r'tempo [$\mu s$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
ax1.text(-60, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

ax1.set_xlim((-55,55))
ax1.set_ylim((-6,6))

ax1.set_yticks((-5,-4,-2,0,2,4,5))
#ax1.set_xticklabels(('-50','-40','-30','-20','-10','0','4.8',''))

ax1.grid(True)
# questo produce una legenda
ax1.legend((in1, out1), ("input sig.", "output sig."),
	'lower left', prop={'size': 16})

# GRAFICO 2
ax2 = host_subplot(122, axes_class=AA.Axes)

in4 = ax2.errorbar(x=t_4*10**6, y=V1_4, fmt='-', c='black', linewidth=2)
out4 = ax2.errorbar(x=t_4*10**6, y=V2_4, fmt='--', c='green', linewidth=2)

ax2.text(0, -6.8, r'tempo [$\mu s$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
ax2.text(61, 0, r'd.d.p. [V]', rotation='vertical',
	ha='center', va='center', fontsize=15)

ax2.set_xlim((-55,55))
ax2.set_ylim((-6,6))
ax2.set_yticks((-5,-4,-2,0,2,4,5))

ax3 = ax2.twin()
ax3.set_yticks((-5,-4,-2,0,2,4,5))
ax3.axis["top"].major_ticklabels.set_visible(False)
ax2.axis["left"].major_ticklabels.set_visible(False)

ax2.grid(True)
# questo produce una legenda
ax2.legend((in4, out4), ("input sig.", "output sig."),
	'upper right', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.04, right=0.96,
    top=0.92, bottom=0.09, hspace=0.08, wspace=0.04)

# mostra grafico
plt.show()
