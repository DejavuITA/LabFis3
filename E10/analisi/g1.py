from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

# Qui vanno i dati
data1 = np.genfromtxt(	"../dati/pessimo_nome.csv",
			delimiter=',',skip_header=1,names=True)
Vin = data1['Vin']
Vout = data1['Vout']
phase = data1['phase']
freq = data1['freq']

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Grafico di Bode per l'amplificatore differenziale",
    y=0.97, fontsize=15)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
ax1.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
#teo1 = ax1.errorbar(x=[i**2 for i in range(8, 1000)],
#y=[20*log10(np.absolute())],    fmt='-.', c='red')

signal = ax1.errorbar(x=freq*1000, y=10*np.log10(Vout*1000/Vin), fmt='.', c='black')

ax1.axhline(y=10*log10(30), linewidth=1, color='grey', linestyle='dashed')
ax1.text(1100000, 10*log10(30)-0.25, r'$log_{10}(30)$', size=16, va='top', ha='left')

#dbv0 = 10*log10(((L**2)*((1/(2*pi*(C*L)**(0.5)))**2)*4*pi**2+S**2)/((R+S)**2+(((1/(2*pi*(C*L)**(0.5)))**2)*4*pi**2)*(L**2+C*(L*(-2+C*L*((1/(2*pi*(C*L)**(0.5)))**2)*4*pi**2)+C*S**2)*(R**2))))-3
#v0 = ax1.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')
#db = ax1.axhline(y=dbv0, linewidth=1, color='grey')
#ax1.annotate("", (10680, dbv0), xytext=(20, 0), textcoords='offset points', arrowprops=dict(facecolor='grey',arrowstyle='-|>', connectionstyle="arc3,rad=0.0"))

ax1.set_ylabel(u'Gain [$dB$]', labelpad=2, fontsize=14)

#ax1.text(1/(2*pi*(L*C)**(0.5))+500, -60+1.5, r'$\nu_0$', size=15, va='center')

ax1.grid(True)
ax1.set_ylim((0, 16))
#ax1.get_yaxis().set_ticklabels(("-60", "-40", "-20", "0"))
#ax1.legend((signal, teo1), ("Dati sperimentali", "andamento teorico"), 'upper center', prop={'size': 12})
plt.setp(ax1.get_xticklabels(), visible=False)
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
fase = ax2.errorbar(x=freq*1000, y=phase, fmt='.', c='black')

#v0 = ax2.axvline(x=1/(2*pi*(C*L)**(0.5)), linewidth=1, color='grey')

ax2.set_ylabel(u'Fase [$^\circ$]', labelpad=2, fontsize=14)
ax2.set_xlabel(u'Frequenza [$Hz$]', labelpad=0, fontsize=14)

#ax2.set_yticks(np.arange(-90, 90.1, 30))
ax2.set_ylim((-2,92))
ax2.set_xlim((900,5000000))
#ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

ax2.grid(True)
ax2.legend((signal), ("Dati sperimentali", ),
	'lower right', prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.08, right=0.97,
    top=0.94, bottom=0.07, hspace=0.04, wspace=0.04)
# mostra grafico
plt.show()
