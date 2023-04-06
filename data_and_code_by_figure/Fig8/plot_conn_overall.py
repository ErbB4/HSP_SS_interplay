import numpy as np 
import matplotlib.pyplot as plt 
from pathlib import Path 
import matplotlib.gridspec as gridspec
import scipy as scipy
from scipy import stats

#define plotting parameters
plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["axes.linewidth"]=.5
plt.rcParams["lines.linewidth"]=1.
plt.rcParams["lines.markersize"]=2
plt.rcParams["xtick.labelsize"]=6
plt.rcParams["ytick.labelsize"]=6
plt.rcParams["font.family"] = "arial"
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.rcParams["legend.fontsize"] = 6
plt.rcParams['xtick.minor.width'] = 0.5
plt.rcParams['xtick.major.width'] = 0.5
plt.rcParams['ytick.minor.width'] = 0.5
plt.rcParams['ytick.major.width'] = 0.5


def cm2inch(value):
    #transfer the unit of figure size from cm to inch
    return value/2.54


def plot_rates(gf,sf,ax):
    T = "C://Users/han/Desktop/GaussianHSP-SC/with-sandra/alpha2/datafullw/paramspace/"
    time_points = np.load(T+str(gf)+"/"+str(sf)+"/sampling_time_points_seed_0.npy")
    i=0
    str_ll = np.load(T+str(gf)+"/"+str(sf)+"/str_ll_seed_"+str(i)+".npy")

    ax.plot(time_points/1000.,str_ll,color='#666666')
    ax.plot(time_points/1000.,[0.1]*len(time_points),'--',color='grey',linewidth=0.5)
    ax.plot(time_points/1000.,[0.]*len(time_points),'--',color='grey',linewidth=0.5)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.set_xlim(5800,7600)
    ax.set_ylim(-0.02,0.3)
    ax.set_xticks([])
    ax.set_yticks([])

fig = plt.figure(figsize=(cm2inch(6.5), cm2inch(3.5)))
gs1 = gridspec.GridSpec(3, 4)
gs1.update(top=0.95,bottom=0.1,left=0.05,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax4 = plt.subplot(gs1[0,3])

ax5 = plt.subplot(gs1[1,0])
ax6 = plt.subplot(gs1[1,1])
ax7 = plt.subplot(gs1[1,2])
ax8 = plt.subplot(gs1[1,3])

ax9 = plt.subplot(gs1[2,0])
ax10 = plt.subplot(gs1[2,1])
ax11 = plt.subplot(gs1[2,2])
ax12 = plt.subplot(gs1[2,3])


plot_rates(1,2,ax1)
plot_rates(1,4,ax2)
plot_rates(1,6,ax3)
plot_rates(1,8,ax4)

plot_rates(5,2,ax5)
plot_rates(5,4,ax6)
plot_rates(5,6,ax7)
plot_rates(5,8,ax8)

plot_rates(10,2,ax9)
plot_rates(10,4,ax10)
plot_rates(10,6,ax11)
plot_rates(10,8,ax12)


ax2.set_title(r"$\Gamma_\mathrm{struc.(S-S)}$")

ax1.text(6700,0.24,r"0.02",fontsize=6.,ha='center',va='bottom')
ax2.text(6700,0.24,r"0.04",fontsize=6.,ha='center',va='bottom')
ax3.text(6700,0.24,r"0.06",fontsize=6.,ha='center',va='bottom')
ax4.text(6700,0.24,r"0.08",fontsize=6.,ha='center',va='bottom')

ax1.set_ylabel(r"$10\%$",fontsize=6.)
ax5.set_ylabel(r"$50\%$",fontsize=6.)
ax9.set_ylabel(r"$100\%$",fontsize=6.)




for ax in [ax9,ax10,ax11,ax12]:
    ax.spines['bottom'].set_visible(True)
    ax.set_xticks([6000])
    ax.set_xticklabels(["silencing"])


plt.savefig("example_conn.svg")
plt.show()