from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt("../dati/scope_e7_1.csv", delimiter=',',
			skip_header=1, names=True)
t1 = data1['x']
V11 = data1['1']
V12 = data1['2']

data2 = np.genfromtxt("../dati/scope_e7_2.csv", delimiter=',',
			skip_header=1, names=True)
t2 = data2['x']
V21 = data2['1']
V22 = data2['2']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(15, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Rilevatore di fronti di salita/discesa",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(121, axes_class=AA.Axes)

#ax1.axhline(y=5.3, c='black', linewidth=1, linestyle='dashed')

#ax1.annotate('', xy=(-5, 9.7),  xycoords='data',
#                xytext=(-5, 5.3), textcoords='data', va='center',
#                arrowprops=dict(arrowstyle="<->",
#                                )
#                )

#ax1.text(18.3,8.1, r'$V_{DC}$', fontsize=16,va='bottom', ha='left')

#dati1V1 = ax1.errorbar(x=t1*1000, y=V21, fmt='-', c='#00FF00', linewidth=2)
#dati1V2 = ax1.errorbar(x=t1*1000, y=V22, fmt='-', c='#00AA00', linewidth=2)


dati2V2 = ax1.errorbar(
	x=t2*1000,
	y=V22+179.41265E-03,
	fmt='-', c='#444444', linewidth=2)
dati2V1 = ax1.errorbar(
	x=t2*1000,
	y=(np.abs(V21+93.04342E-03)+V21+93.04342E-03)*0.5,#-93.04342E-03*0.5,
	fmt='-', c='#FF0000', linewidth=2)

ax1.set_xlabel(u'Tempo [ms]', labelpad=8, fontsize=16)
ax1.set_ylabel(u'd.d.p. [V]', labelpad=0, fontsize=16)

ax1.set_xlim((-29,29))
#ax1.set_xticklabels(("","-20","-10","0","10","20"))
ax1.set_ylim((-0.4,12.15))

#ax1.set_xticks((-50,-40,-30,-20,-10,0,4.8))
#ax1.set_yticks((0,2,4,6,8,8.06,10))

# ax2 is responsible for "top" axis and "right" axis
#ax2 = ax1.twin()
#ax2.set_yticks((8.06,))
#ax2.set_xticklabels(("5.7",))
#ax2.set_xticklabels(["$0$", r"$\frac{1}{2}\pi$",r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
#ax2.axis["top"].major_ticklabels.set_visible(False)

ax1.grid(True)

# questo produce una legenda
ax1.legend(
#(dati1V1, dati1V2),
(dati2V2, dati2V1),
("Segnale in input", "Segnale in output"), 'upper left', prop={'size': 16})

ax2 = host_subplot(122, axes_class=AA.Axes)
dati1V2 = ax2.errorbar(x=t1*1000, y=V12+78.12512E-03,
	fmt='-', c='#444444', linewidth=2)
dati1V1 = ax2.errorbar(x=t1*1000, y=V11+78.12512E-03,
	fmt='-', c='#00CC00', linewidth=2)

ax2.set_xlabel(u'Tempo [ms]', labelpad=8, fontsize=16)
#ax2.set_ylabel(u'd.d.p. [V]', labelpad=3, fontsize=16)

ax2.set_ylim((-0.4,12.15))
ax2.axis["left"].major_ticklabels.set_visible(False)
ax2.set_xlim((-29,29))
#ax2.set_xticklabels(("","-20","-10","0","10","20"))

ax3 = ax2.twin()
ax3.axis["top"].major_ticklabels.set_visible(False)
ax3.set_ylabel(u'd.d.p. [V]', labelpad=3, fontsize=16)

ax2.grid(True)


# questo produce una legenda
ax2.legend(
(dati1V1, dati1V2),
("Segnale in input", "Segnale in output"), 'upper right', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.05, right=0.95,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
