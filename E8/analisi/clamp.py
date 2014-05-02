from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

#### dati del cc3 ####
data1 = np.genfromtxt(	"../dati/scope_5_clip_1.csv",
			delimiter=',',skip_header=1,names=True )
t = data1['x']
V1 = data1['1']
V2 = data1['2']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle(r'emitter follower con partitore: fenomeno del $clamping$', y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)

in1 = ax1.errorbar(x=t*10**3, y=V1, fmt='-', c='blue', linewidth=2)
out1 = ax1.errorbar(x=t*10**3, y=V2, fmt='--', c='red', linewidth=2)

ax1.text(0, -8.7, r'tempo [$ms$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
ax1.text(-295, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

ax1.set_xlim((-280,280))
ax1.set_ylim((-7.8,7.8))

#ax1.set_yticks((-5,-4,-2,0,2,4,5))
#ax1.set_xticklabels(('-50','-40','-30','-20','-10','0','4.8',''))

ax1.grid(True)
# questo produce una legenda
ax1.legend((in1, out1), ("input sig.", "output sig."),
	'lower right', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.05, right=0.98,
    top=0.92, bottom=0.08, hspace=0.08, wspace=0.04)

# mostra grafico
plt.show()
