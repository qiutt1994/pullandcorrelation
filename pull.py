import matplotlib
#matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc, rcParams


def pull(centre, error, names, filename=None, datac=None, datae=None):
    x = range(1, len(centre) + 1)
    fig = plt.figure(figsize=(0.2*len(centre),4))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_ylim(-3, 5)
    ax.set_xlim(0, len(centre) + 1)
    #ax.set_aspect(aspect=1/len(centre)*45)
    xband = [0,len(centre) + 2]
    y1 = [1,1]
    ym1 = [-1,-1]
    y2 = [2,2]
    ym2 = [-2,-2]
    ax.fill_between(xband,y2,ym2,color='yellow')
    ax.fill_between(xband,y1,ym1,color='lime')

    dataline = ax.errorbar(x, centre, color='k', linestyle="",
                 yerr=error, fmt='_', markersize='8')
    if datac is None:
        for i, each in enumerate(x):
            plt.text(each, 2.1, str("{: .3f}".format(centre[i])) + r" $\pm$ " + str("{:.3f}".format(error[i])), fontsize=7, rotation='vertical')
    if datac is not None and datae is not None:
        x = np.array(x) + 0.25
        asimovline = ax.errorbar(x, datac, color='r', linestyle="",
                    yerr=datae, fmt='_', markersize='8')
        plt.legend(handles=[dataline, asimovline], labels=["data", "asimov"], frameon=False)
        for i, each in enumerate(x):
            plt.text(each-0.6, 2.1, str("{: .3f}".format(centre[i])) + r" $\pm$ " + str("{:.3f}".format(error[i])), fontsize=6, rotation='vertical')
            plt.text(each-0.17, 2.1, str("{: .3f}".format(datac[i])) + r" $\pm$ " + str("{:.3f}".format(datae[i])), fontsize=6, rotation='vertical', c="r")

    # Set number of ticks for x-axis
    ax.set_xticks(x)
    # Set ticks labels for x-axis
    ax.set_xticklabels(names, rotation=90, fontsize=8)
    ax.set_ylabel(r"$\mathit{(\theta_{fit}-\theta_{0})/\Delta\theta}$",fontsize=15)
    #plt.tight_layout()
    if filename is not None:
        plt.savefig(filename + '.pdf', bbox_inches='tight', pad_inches = 0.04)#
    #plt.show()
    plt.close(fig)

if __name__ == "__main__":
    pull([0.1,0.2,-0.3]*10,[1,1.1,1.1]*10,['SysFT_EFF_Eigen_Light_4_AntiKt2PV0TrackJets','bdfasffdhsfsdiuhfidhfdsfsdfsdfdsf','fdisujfdsfoihfisdufhid']*10, "test", 
    [0.11,0.19,-0.2]*10,[1.2,1,1]*10)