from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

#import matplotlib.cbook as cbook	# DOGE
#from scipy.misc import imread		# DOGE

#dogesmall = cbook.get_sample_data('/usr/lib/python3/dist-packages/scipy/misc/lena.dat')#'dogesmall.jpg')
#img = imread(dogesmall)
#plt.imshow(dogesmall, zorder=0)#, extent=[0.5, 8.0, 1.0, 7.0])

data1 = np.genfromtxt(	"../dati/2014_05_13_001.csv",
			delimiter=',',skip_header=1,names=True)
t_01 = data1['x']
V1_01 = data1['1']
V2_01 = data1['2']
#print(np.amax(V1_03), np.amax(-V1_03), np.amax(V2_03), np.amax(-V2_03),)

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Amplificatore alle differenze", y=0.97, fontsize=17)

# GRAFICO 1
ax3 = host_subplot(111, axes_class=AA.Axes)

in3 = ax3.errorbar(x=t_01*10**3, y=V1_01, fmt='-', c='blue', linewidth=2)
out3 = ax3.errorbar(x=t_01*10**3, y=V2_01, fmt='-', c='red', linewidth=2)
#ax3.axhline(4.5, c='black', linewidth=1, linestyle='dotted')

ax3.text(0, -6.7, r'tempo [$ms$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
ax3.text(-1.06, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

ax3.set_yticks((-4.5,-4,-2,0,2,4,4.5))

ax3.set_xlim((-1.1,1.1))
ax3.set_ylim((-5,5))

ax3.grid(True)
# questo produce una legenda
ax3.legend((in3, out3), ("input sig. ($v_{in1}$ - $v_{in2}$)", "output sig."),
	'lower left', prop={'size': 16})

# GRAFICO 2
#DOGE#ax4 = host_subplot(122, axes_class=AA.Axes)

#ax4.set_xlim((-1.1,1.1))
#ax4.set_ylim((-1,10))
#ax4.set_yticks((-5,-4,-2,0,2,4,5))

#DOGE#ax4b = ax4.twin()
#ax4b.set_yticks((-5,-4,-2,0,2,4,5))
#DOGE#ax4b.axis["top"].major_ticklabels.set_visible(False)
#DOGE#ax4.axis["left"].major_ticklabels.set_visible(False)

#ax4.grid(True)
# questo produce una legenda

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.05, right=0.98,
    top=0.92, bottom=0.09, hspace=0.08, wspace=0.04)

# mostra grafico
plt.show()
