from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data1 = np.genfromtxt(	"../dati/2014_05_06_201.csv",
			delimiter=',',skip_header=1,names=True)
V01_1 = data1['1']
V01_2 = data1['2']
data2 = np.genfromtxt(	"../dati/2014_05_06_202.csv",
			delimiter=',',skip_header=1,names=True)
V02_1 = data2['1']
V02_2 = data2['2']
data3 = np.genfromtxt(	"../dati/2014_05_06_203.csv",
			delimiter=',',skip_header=1,names=True)
V03_1 = data3['1']
V03_2 = data3['2']
data4 = np.genfromtxt(	"../dati/2014_05_06_204.csv",
			delimiter=',',skip_header=1,names=True)
V04_1 = data4['1']
V04_2 = data4['2']
data5 = np.genfromtxt(	"../dati/2014_05_06_205.csv",
			delimiter=',',skip_header=1,names=True)
V05_1 = data5['1']
V05_2 = data5['2']
data6 = np.genfromtxt(	"../dati/2014_05_06_206.csv",
			delimiter=',',skip_header=1,names=True)
V06_1 = data6['1']
V06_2 = data6['2']
data7 = np.genfromtxt(	"../dati/2014_05_06_207.csv",
			delimiter=',',skip_header=1,names=True)
V07_1 = data7['1']
V07_2 = data7['2']
data8 = np.genfromtxt(	"../dati/2014_05_06_208.csv",
			delimiter=',',skip_header=1,names=True)
V08_1 = data8['1']
V08_2 = data8['2']
data9 = np.genfromtxt(	"../dati/2014_05_06_209.csv",
			delimiter=',',skip_header=1,names=True)
V09_1 = data9['1']
V09_2 = data9['2']
data10 = np.genfromtxt(	"../dati/2014_05_06_210.csv",
			delimiter=',',skip_header=1,names=True)
V10_1 = data10['1']
V10_2 = data10['2']


rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Caratteristica di uscita del transistor",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)

# crea plot con le barre d'errore (o anche senza)

#ax1.axhline(y=-25.5, xmin=0.865, xmax=1, c='black',linewidth=1,linestyle='dashed')
#ax1.axvline(x=5.75, ymin=0, ymax=0.4875, c='black',linewidth=1,linestyle='dashed')

#slope = ax1.errorbar(x=np.arange(-7.1,-6.3,0.001), y=A+B*np.arange(-7.1,-6.3,0.001),
#    fmt='-', c='gray', linewidth=2)
ma90 = ax1.errorbar(	x=(V01_1[209:529]-V01_2[209:529]), y=V01_2[209:529]*100,
			fmt='-', c='#000000', linewidth=2)
ma80 = ax1.errorbar(	x=(V02_1[305:625]-V02_2[305:625]), y=V02_2[305:625]*100,
			fmt='-', c='#101010', linewidth=2)
ma70 = ax1.errorbar(	x=(V03_1[20:340]-V03_2[20:340]), y=V03_2[20:340]*100,
			fmt='-', c='#202020', linewidth=2)
ma60 = ax1.errorbar(	x=(V04_1[185:505]-V04_2[185:505]), y=V04_2[185:505]*100,
			fmt='-', c='#303030', linewidth=2)
ma50 = ax1.errorbar(	x=(V05_1[146:466]-V05_2[146:466]), y=V05_2[146:466]*100,
			fmt='-', c='#404040', linewidth=2)
ma40 = ax1.errorbar(	x=(V06_1[3:323]-V06_2[3:323]), y=V06_2[3:323]*100,
			fmt='-', c='#505050', linewidth=2)
ma30 = ax1.errorbar(	x=(V07_1[177:497]-V07_2[177:497]), y=V07_2[177:497]*100,
			fmt='-', c='#606060', linewidth=2)
ma20 = ax1.errorbar(	x=(V08_1[297:617]-V08_2[297:617]), y=V08_2[297:617]*100,
			fmt='-', c='#707070', linewidth=2)
ma10 = ax1.errorbar(	x=(V09_1[184:504]-V09_2[184:504]), y=V09_2[184:504]*100,
			fmt='-', c='#808080', linewidth=2)
ma1 = ax1.errorbar(	x=(V10_1[212:532]-V10_2[212:532]), y=V10_2[212:532]*100,
			fmt='-', c='#909090', linewidth=2)
#    markersize=7, markeredgewidth=1)

ax1.text(5, -3.5, r'$V_{CE}$ [V]', ha='center', va='center', fontsize=16)
ax1.set_ylabel(r'$I_C$ [mA]', labelpad=-4, fontsize=16)

ax1.text(10.1, 1.2,'1.0 µA', ha='right', va='center', fontsize=16)
ax1.text(9.6, 4.3,'10.4 µA', ha='center', va='center', fontsize=16)
ax1.text(9.4, 8.5,'22.9 µA', ha='center', va='center', fontsize=16)
ax1.text(9.2, 11.8,'32.6 µA', ha='center', va='center', fontsize=16)
ax1.text(9.0, 15,'42.3 µA', ha='center', va='center', fontsize=16)
ax1.text(8.8, 18.5,'52.0 µA', ha='center', va='center', fontsize=16)
ax1.text(8.6, 22,'61.7 µA', ha='center', va='center', fontsize=16)
ax1.text(8.4, 25.8,'71.5 µA', ha='center', va='center', fontsize=16)
ax1.text(8.2, 29,'81.2 µA', ha='center', va='center', fontsize=16)
ax1.text(8.0, 32,'90.9 µA', ha='center', va='center', fontsize=16)


#ax1.annotate(r'$I_{sc}$', xy=(5.75, 0),  xycoords='data',
#                xytext=(5.75-10, 50), textcoords='data',
#		va='center', fontsize=20,
#                arrowprops=dict(arrowstyle="->",
#                                )
#                )

ax1.set_xlim((-0.25,10.25))
ax1.set_ylim((-2,34))

#ax1.set_xticks((-50,-40,-30,-20,-10,0,4.8,5.75))
#ax1.set_xticklabels(('-50','-40','-30','-20','-10','0','4.8',''))
#ax1.set_yticks((-100,-50,-25.5,-20.6,0,50,100))
#ax1.set_yticklabels(('-100','-50','','-20.6','0','50','100'))

# ax2 is responsible for "top" axis and "right" axis
#ax2 = ax1.twin()
#ax2.set_yticks((-100,-50,-25.5,-20.6,0,50,100))
#ax2.set_yticklabels(("","","-25.5",))
#ax2.set_xticks((-50,-40,-30,-20,-10,0,4.8,5.75))
#ax2.set_xticklabels(('','','','','','','','5.75'))

ax1.grid(True)

# questo produce una legenda
#ax1.legend((ma1, ma90), (r'1.000 µA', r'90.9 µA'), 'upper right', prop={'size': 16})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.07, right=0.98,
    top=0.93, bottom=0.08, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
