from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

C1 =100E-9
R1 =( # *10**3
0.0500,
0.1000,
5.000,
20.000,
30.000,
60.000)
Vpp1 =10.06
Vmax1 =(
7.10,
7.84,
8.39,
7.76,
6.97,
4.62)

C2 =( # / 10**6
5.1E-03,
50E-03,
200E-03,
600E-03,
3E-00)
R2 =1000
Vpp2 =10.06
Vmax2 =(
2.93,
7.34,
8.13,
8.30,
6.66)

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(15, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Rilevatore di fronti di salita/discesa",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(121, axes_class=AA.Axes)

dati1 = ax1.errorbar(
	x=R1,
	y=Vmax1,
	fmt='o', c='#444444', linewidth=2)

ax1.set_xlabel(r'Resistenza [$k\Omega$]', labelpad=8, fontsize=16)
ax1.set_ylabel(r'$V_{MAX} [V]$', labelpad=0, fontsize=16)

ax1.set_xlim((-4.000,64.000))
	#ax1.set_xticklabels(("","-20","-10","0","10","20"))
ax1.set_ylim((0,11))

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
(dati1, ),
(r'$V_{MAX}$ in funzione di $R$', ), 'upper left', prop={'size': 16})

# GRAFICO 2

ax2 = host_subplot(122, axes_class=AA.Axes)

dati2 = ax2.errorbar(
	x=C2,
	y=Vmax2,
	fmt='o', c='#444444', linewidth=2)

ax2.set_xlabel(r'Capacità [$\mu F$]', labelpad=8, fontsize=16)
#ax2.set_ylabel(u'd.d.p. [V]', labelpad=3, fontsize=16)

ax2.set_ylim((0,11))
ax2.axis["left"].major_ticklabels.set_visible(False)
ax2.set_xlim((-0.2,3.200))
#ax2.set_xticklabels(("","-20","-10","0","10","20"))

ax3 = ax2.twin()
ax3.axis["top"].major_ticklabels.set_visible(False)
ax3.set_ylabel(r'$V_{MAX} [V]$', labelpad=3, fontsize=16)


ax2.grid(True)


# questo produce una legenda
ax2.legend(
(dati2, ),
(r'$V_{MAX}$ in funzione di $C$', ), 'upper right', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.05, right=0.95,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
