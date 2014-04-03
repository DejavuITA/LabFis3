from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

data_0 = np.genfromtxt("../dati/scope_0.csv", delimiter=',', skip_header=1, names=True)
TIM_0 = data_0['xaxis']
CH1_0 = data_0['y1']
CH2_0 = data_0['y2']

data_1 = np.genfromtxt("../dati/scope_1.csv", delimiter=',', skip_header=1, names=True)
TIM_1 = data_1['xaxis']
CH1_1 = data_1['y1']
CH2_1 = data_1['y2']

data_2 = np.genfromtxt("../dati/scope_2.csv", delimiter=',', skip_header=1, names=True)
TIM_2 = data_2['xaxis']
CH1_2 = data_2['y1']
CH2_2 = data_2['y2']

data_3 = np.genfromtxt("../dati/scope_3.csv", delimiter=',', skip_header=1, names=True)
TIM_3 = data_3['xaxis']
CH1_3 = data_3['y1']
CH2_3 = data_3['y2']

data_4 = np.genfromtxt("../dati/scope_4.csv", delimiter=',', skip_header=1, names=True)
TIM_4 = data_4['xaxis']
CH1_4 = data_4['y1']
CH2_4 = data_4['y2']

rcParams['font.size'] = 15
### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(18, 18), dpi=65)
# Titolo del grafico
f1.suptitle("5 grafici in 1",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(3, 2, 1)
CH1_0 = ax1.errorbar(x=TIM_0, y=CH1_0, fmt='-', c='blue', linewidth=2)
CH2_0 = ax1.errorbar(x=TIM_0, y=CH2_0, fmt='-', c='red', linewidth=2)

ax1.grid(True)
ax1.legend((CH1_0, CH2_0), ("CH1_0", "CH2_0"), 'upper left', prop={'size': 12})

# GRAFICO 2
ax1 = f1.add_subplot(3, 2, 2)
CH1_1 = ax1.errorbar(x=TIM_1, y=CH1_1, fmt='-', c='blue', linewidth=2)
CH2_1 = ax1.errorbar(x=TIM_1, y=CH2_1, fmt='-', c='red', linewidth=2)

ax1.grid(True)
ax1.legend((CH1_1, CH2_1), ("CH1_1", "CH2_1"), 'upper left', prop={'size': 12})

# GRAFICO 3
ax1 = f1.add_subplot(3, 2, 3)
CH1_2 = ax1.errorbar(x=TIM_2, y=CH1_2, fmt='-', c='blue', linewidth=2)
CH2_2 = ax1.errorbar(x=TIM_2, y=CH2_2, fmt='-', c='red', linewidth=2)

ax1.grid(True)
ax1.legend((CH1_2, CH2_2), ("CH1_2", "CH2_2"), 'upper left', prop={'size': 12})

# GRAFICO 4
ax1 = f1.add_subplot(3, 2, 4)
CH1_3 = ax1.errorbar(x=TIM_3, y=CH1_3, fmt='-', c='blue', linewidth=2)
CH2_3 = ax1.errorbar(x=TIM_3, y=CH2_3, fmt='-', c='red', linewidth=2)

ax1.grid(True)
ax1.legend((CH1_3, CH2_3), ("CH1_3", "CH2_3"), 'upper left', prop={'size': 12})

# GRAFICO 5
ax1 = f1.add_subplot(3, 2, 5)
CH1_4 = ax1.errorbar(x=TIM_4, y=CH1_4, fmt='-', c='blue', linewidth=2)
CH2_4 = ax1.errorbar(x=TIM_4, y=CH2_4, fmt='-', c='red', linewidth=2)

ax1.grid(True)
ax1.legend((CH1_4, CH2_4), ("CH1_4", "CH2_4"), 'upper left', prop={'size': 12})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.95,
    top=0.92, bottom=0.12, hspace=0.08, wspace=0)

# mostra grafico
plt.show() 
