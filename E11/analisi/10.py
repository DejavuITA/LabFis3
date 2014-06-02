from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

#### dati ####
data01 = np.genfromtxt("../dati/scope_10_001.csv", delimiter=',')
t_01 = data01[2:,0]
V1_01 = data01[2:,1]
V2_01 = data01[2:,2]
data02 = np.genfromtxt("../dati/scope_10_002.csv", delimiter=',')
t_02 = data02[2:,0]
V1_02 = data02[2:,1]
V2_02 = data02[2:,2]
data03 = np.genfromtxt("../dati/scope_10_003.csv", delimiter=',')
t_03 = data03[2:,0]
V1_03 = data03[2:,1]
V2_03 = data03[2:,2]
data04 = np.genfromtxt("../dati/scope_10_004.csv", delimiter=',')
t_04 = data04[2:,0]
V1_04 = data04[2:,1]
V2_04 = data04[2:,2]

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(15, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Serie 10", y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(221, axes_class=AA.Axes)

in1 = ax1.errorbar(x=t_01, y=V1_01, fmt='-', c='black', linewidth=2)
out1 = ax1.errorbar(x=t_01, y=V2_01, fmt='--', c='green', linewidth=2)

ax1.grid(True)

# GRAFICO 2
ax2 = host_subplot(222, axes_class=AA.Axes)

in2 = ax2.errorbar(x=t_02, y=V1_02, fmt='-', c='black', linewidth=2)
out2 = ax2.errorbar(x=t_02, y=V2_02, fmt='--', c='green', linewidth=2)

ax2.grid(True)

# GRAFICO 3
ax3 = host_subplot(223, axes_class=AA.Axes)

in3 = ax3.errorbar(x=t_03, y=V1_03, fmt='-', c='black', linewidth=2)
out3 = ax3.errorbar(x=t_03, y=V2_03, fmt='--', c='green', linewidth=2)

ax3.grid(True)

# GRAFICO 4
ax4 = host_subplot(224, axes_class=AA.Axes)

in4 = ax4.errorbar(x=t_04, y=V1_04, fmt='-', c='black', linewidth=2)
out4 = ax4.errorbar(x=t_04, y=V2_04, fmt='--', c='green', linewidth=2)

ax4.grid(True)

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.04, right=0.98,
    top=0.92, bottom=0.05, hspace=0.08, wspace=0.04)

# mostra grafico
plt.show()
