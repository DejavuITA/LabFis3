from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt(	"../dati/2014_05_06_001.csv",
			delimiter=',',skip_header=1,names=True)
t_01 = data1['x']
V1_01 = data1['1']
V2_01 = data1['2']
data2 = np.genfromtxt(	"../dati/2014_05_06_002.csv",
			delimiter=',',skip_header=1,names=True)
t_02 = data2['x']
V1_02 = data2['1']
V2_02 = data2['2']
data3 = np.genfromtxt(	"../dati/2014_05_06_003.csv",
			delimiter=',',skip_header=1,names=True)
t_03 = data3['x']
V1_03 = data3['1']
V2_03 = data3['2']
data4 = np.genfromtxt(	"../dati/2014_05_06_004.csv",
			delimiter=',',skip_header=1,names=True)
t_04 = data4['x']
V1_04 = data4['1']
V2_04 = data4['2']
data5 = np.genfromtxt(	"../dati/2014_05_06_005.csv",
			delimiter=',',skip_header=1,names=True)
t_05 = data5['x']
V1_05 = data5['1']
V2_05 = data5['2']
data6 = np.genfromtxt(	"../dati/2014_05_06_006.csv",
			delimiter=',',skip_header=1,names=True)
t_06 = data6['x']
V1_06 = data6['1']
V2_06 = data6['2']
data7 = np.genfromtxt(	"../dati/2014_05_06_007.csv",
			delimiter=',',skip_header=1,names=True)
t_07 = data7['x']
V1_07 = data7['1']
V2_07 = data7['2']
data8 = np.genfromtxt(	"../dati/2014_05_06_008.csv",
			delimiter=',',skip_header=1,names=True)
t_08 = data8['x']
V1_08 = data8['1']
V2_08 = data8['2']
data9 = np.genfromtxt(	"../dati/2014_05_06_009.csv",
			delimiter=',',skip_header=1,names=True)
t_09 = data9['x']
V1_09 = data9['1']
V2_09 = data9['2']
data10 = np.genfromtxt(	"../dati/2014_05_06_002.csv",
			delimiter=',',skip_header=1,names=True)
t_10 = data10['x']
V1_10 = data10['1']
V2_10 = data10['2']

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(15, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Amplificatore ad emettitore comune", y=0.97, fontsize=17)

# GRAFICO 1
ax3 = host_subplot(121, axes_class=AA.Axes)

in3 = ax3.errorbar(x=t_03*10**3, y=V1_03, fmt='-', c='blue', linewidth=2)
out3 = ax3.errorbar(x=t_03*10**3, y=4.96+V2_03, fmt='-', c='red', linewidth=2)
ax3.axhline(4.96, c='black', linewidth=1, linestyle='dashed')

ax3.text(0, -1.64, r'tempo [$ms$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
ax3.text(-1.20	, 4.5, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)
ax3.text(1,4.9, r'$offset$= 4.96$V$', ha='right', va='top', fontsize=15)

ax3.set_xlim((-1.1,1.1))
ax3.set_ylim((-1,10))

ax3.grid(True)
# questo produce una legenda
ax3.legend((in3, out3), ("input sig.", "output sig."),
	'upper left', prop={'size': 16})

# GRAFICO 2
ax4 = host_subplot(122, axes_class=AA.Axes)

in4 = ax4.errorbar(x=t_05*10**3, y=V1_05, fmt='-', c='black', linewidth=2)
out4 = ax4.errorbar(x=t_05*10**3, y=5.96+V2_05, fmt='-', c='green', linewidth=2)
ax4.axhline(4.96, c='black', linewidth=1, linestyle='dashed')

ax4.text(0, -1.64, r'tempo [$ms$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
ax4.text(1.22, 4.5, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)
ax4.text(1,4.9, r'$offset$= 4.96$V$', ha='right', va='top', fontsize=15)

ax4.set_xlim((-1.1,1.1))
ax4.set_ylim((-1,10))
#ax4.set_yticks((-5,-4,-2,0,2,4,5))

ax4b = ax4.twin()
#ax4b.set_yticks((-5,-4,-2,0,2,4,5))
ax4b.axis["top"].major_ticklabels.set_visible(False)
ax4.axis["left"].major_ticklabels.set_visible(False)

ax4.grid(True)
# questo produce una legenda
ax4.legend((in4, out4), ("input sig.", "output sig."),
	'upper left', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.04, right=0.96,
    top=0.92, bottom=0.09, hspace=0.08, wspace=0.04)

# mostra grafico
plt.show()
