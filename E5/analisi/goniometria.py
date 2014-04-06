from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

rcParams['font.size'] = 15

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Corrente e derivata della corrente", y=0.97, fontsize=15)

f = 1/50
w = 2*pi*f
T = 1/f
t = np.arange(-10,60,0.01)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
# crea plot con le barre d'errore (o anche senza)
cos = ax1.errorbar(x=t, y=np.cos(w*t), c='red')
ax1.axvline(x=0.93*T/2/pi, linewidth=1, color='grey')
ax1.axvline(x=T/2-0.93*T/2/pi, linewidth=1, color='grey')

ax1.set_ylabel(u'Intensità di corrente [A]', labelpad=2, fontsize=14)

ax1.annotate('', xy=(0, 0),  xycoords='data',
                xytext=(T/4, 0), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->", ) )
ax1.text(T/8-1, 0.1, r'$T / 4$', size=12, va='center', ha='center')

ax1.annotate('', xy=(T/4, 0),  xycoords='data',
                xytext=(0.93*T/2/pi+12, 0), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->", ) )
ax1.text(T/4+(0.93*T/2/pi+12-T/4)*0.5, 0.1, r'$\Delta t$', size=15, va='center', ha='center')

ax1.annotate('', xy=(0, -0.08),  xycoords='data',
                xytext=(0.93*T/2/pi+12, -0.08), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->", ) )
ax1.text((0.93*T/2/pi+12)/2, -0.20, r'$t_{att}$', size=15, va='center', ha='center')


ax1.set_ylim(-1.1,1.1)
ax1.set_xlim(-6,60)

ax1.set_yticks((-1, -0.5, 0, 0.5, 1))
ax1.get_yaxis().set_ticklabels((r'$I_0$',r'$-\frac{I_0}{2}$',0,r'$\frac{I_0}{2}$',r'$I_0$'))

ax1.grid(True)
plt.setp(ax1.get_xticklabels(), visible=False)
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2,)
# crea plot con le barre d'errore (o anche senza)
sin = ax2.errorbar(x=t, y=-np.sin(w*t), c='blue')

ax2.axhline(y=0.8, linewidth=1, color='grey')
ax2.axhline(y=-0.8, linewidth=1, color='grey')

ax2.axvline(x=0.93*T/2/pi, linewidth=1, color='grey')
ax2.axvline(x=T/2-0.93*T/2/pi, linewidth=1, color='grey')

ax2.annotate('', xy=(0.93*T/2/pi, 0),  xycoords='data',
                xytext=(0.93*T/2/pi+12, 0), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->", ) )
ax2.text(0.93*T/2/pi+12/2, 0.1, r'$\tau$', size=15, va='center', ha='center')

ax2.annotate('', xy=(0, 0),  xycoords='data',
                xytext=(0.93*T/2/pi, 0), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->", ) )
ax2.text(0.93*T/2/pi/2, 0.1, r'$t^*$', size=15, va='center', ha='center')

ax2.annotate('', xy=(0, -0.08),  xycoords='data',
                xytext=(0.93*T/2/pi+12, -0.08), textcoords='data', va='center',
                arrowprops=dict(arrowstyle="<->", ) )
ax2.text((0.93*T/2/pi+12)/2, -0.20, r'$t_{att}$', size=15, va='center', ha='center')

ax2.set_ylabel(u'Derivata della corrente [A / s]', labelpad=2, fontsize=14)
#ax2.set_ylabel(r'$\frac{dI}{dt}$ [A / s]', labelpad=-10, fontsize=14)
ax2.set_xlabel(u'Tempo [$ms$]', labelpad=2, fontsize=14)

ax2.set_ylim(-1.1,1.1)
ax2.set_xlim(-6,60)

#ax2.yaxis.set_label_position("right") # posiziona il label sulla destra
#ax2.yaxis.tick_right() # posiziona i ticks sulla destra
ax2.set_yticks((-1, -0.8, 0, 0.8, 1))
ax2.get_yaxis().set_ticklabels((r'$I_0 \omega$',r'$-K$',0,r'$K$',r'$I_0 \omega$'))

ax2.grid(True)
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.96, top=0.94, bottom=0.08, hspace=0.05, wspace=0.05)
# mostra grafico
plt.show() 
