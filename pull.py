import matplotlib
#matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc, rcParams


def pull(centre, error, names, filename=None):
    x = range(1, len(centre) + 1)
    fig = plt.figure(figsize=(0.2*len(centre),7))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_ylim(-4, 4)
    ax.set_xlim(0, len(centre) + 1)
    #ax.set_aspect(aspect=1/len(centre)*45)
    xband = [0,len(centre) + 2]
    y1 = [1,1]
    ym1 = [-1,-1]
    y2 = [2,2]
    ym2 = [-2,-2]
    ax.fill_between(xband,y2,ym2,color='yellow')
    ax.fill_between(xband,y1,ym1,color='lime')

    ax.errorbar(x, centre, color='k', linestyle="",
                 yerr=error, fmt='_', markersize='8')

    # Set number of ticks for x-axis
    ax.set_xticks(x)
    # Set ticks labels for x-axis
    ax.set_xticklabels(names, rotation=90, fontsize=8)
    ax.set_ylabel(r"$\mathit{(\theta_{fit}-\theta_{fit})/\Delta\theta}$",fontsize=15)
    plt.tight_layout()
    if filename is not None:
        plt.savefig(filename + '.pdf', bbox_inches='tight', pad_inches = 0, )#
    #plt.show()

if __name__ == "__main__":
    pull([0.1,0.2,-0.3]*10,[1,1.1,1.1]*10,['SysFT_EFF_Eigen_Light_4_AntiKt2PV0TrackJets','bdfasffdhsfsdiuhfidhfdsfsdfsdfdsf','fdisujfdsfoihfisdufhid']*10, "test")