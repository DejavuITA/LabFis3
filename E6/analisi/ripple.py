from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt("../dati/n1.csv", delimiter=',', skip_header=1, names=True)
t1 = data1['second']
V1 = data1['Volt']

data3 = np.genfromtxt("../dati/n3.csv", delimiter=',', skip_header=1, names=True)
t3 = data3['second']
V3 = data3['Volt']

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

data11 = np.genfromtxt("../dati/n11.csv", delimiter=',', skip_header=1,names=True)
t11 = data11['second']
V11 = data11['Volt']

data12 = np.genfromtxt("../dati/n12.csv", delimiter=',', skip_header=1,names=True)
t12 = data12['second']
V12 = data12['Volt']

data13 = np.genfromtxt("../dati/n13.csv", delimiter=',', skip_header=1,names=True)
t13 = data13['second']
V13 = data13['Volt']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Ponte di Graetz: segnale stabilizzato",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)

# crea plot con le barre d'errore (o anche senza)

#ax1.axhline(y=8.06, c='black', linewidth=1)
ax1.axhline(y=7.90, c='black', linewidth=1)
ax1.axhline(y=9.72424631, c='black', linewidth=1, linestyle='dashed')
ax1.axhline(y=5.3, c='black', linewidth=1, linestyle='dashed')

ax1.annotate('', xy=(-5, 9.7),  xycoords='data',
                xytext=(-5, 5.3), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->",
                                )
                )
ax1.text(-5+0.25,7, r'$V_{AC}$', fontsize=16,va='center', ha='left')
ax1.text(18.3,8.1, r'$V_{DC}$', fontsize=16,va='bottom', ha='left')

#dati1 = ax1.errorbar(x=t1, y=V1, fmt='-', c='#00FF00', linewidth=2)

dati3 = ax1.errorbar(x=t3*1000, y=V3, fmt='-', c='#777777', linewidth=2)
dati4 = ax1.errorbar(x=t4*1000, y=V4, fmt='--', c='#00AA00', linewidth=2)
#dati5 = ax1.errorbar(x=t5, y=V5, fmt='-', c='#8888FF', linewidth=2)
#dati6 = ax1.errorbar(x=t6, y=V6, fmt='-', c='#FF00BB', linewidth=2)
dati7 = ax1.errorbar(x=t7*1000, y=9.72424631+0.95*(V7-9.72424631), fmt='-', c='#FF0000', linewidth=2)

	##dati11 = ax1.errorbar(x=t11*1000, y=V11, fmt='-', c='#00FFFF', linewidth=2)
	##dati12 = ax1.errorbar(x=t12, y=V12, fmt='-', c='#0000AA', linewidth=2)
	##dati13 = ax1.errorbar(x=t13, y=V13, fmt='-', c='#00AAAA', linewidth=2)

ax1.set_xlabel(u'Tempo [ms]', labelpad=8, fontsize=16)
#ax1.set_ylabel(u'd.d.p. [V]', labelpad=-8, fontsize=16)
ax1.text(-21.3,0, u'd.d.p. [V]', fontsize=15, va='center', ha='center', rotation='vertical')

ax1.set_xlim((-20,20))
#ax1.set_ylim((-0.7,10.5))
ax1.set_ylim((-12,12))

#ax1.set_xticks((-50,-40,-30,-20,-10,0,4.8))
#ax1.set_yticks((0,2,4,6,8,8.06,10))

# ax2 is responsible for "top" axis and "right" axis
ax2 = ax1.twin()
ax2.set_yticks((7.9,))
ax2.set_yticklabels(("8.06",))
#ax2.set_xticklabels(["$0$", r"$\frac{1}{2}\pi$",r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
ax2.axis["top"].major_ticklabels.set_visible(False)

ax1.grid(True)

# questo produce una legenda
ax1.legend((dati3, dati4, dati7), ("Segnale in input", "Segnale raddrizzato","Segnale in output"), 'lower left', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.06, right=0.94,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
