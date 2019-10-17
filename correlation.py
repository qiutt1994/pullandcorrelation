import matplotlib.pyplot as plt
import numpy as np

def correlation(matrix, xylabel, filename=None, number=False):
    if len(matrix) != len(matrix[0]) or len(matrix) != len(xylabel):
        print("correlation error: wrong input list size.")
        exit(1)
    fig = plt.figure(figsize=(int(len(matrix[0]))*0.2, int(len(matrix[0]))*0.2))
    ax = fig.add_subplot(1, 1, 1)
    im = ax.imshow(matrix, cmap= 'bwr')
    im.set_clim(-1, 1)
    ax.set_xticks(np.arange(len(xylabel)))
    ax.set_yticks(np.arange(len(xylabel)))
    ax.set_xticklabels(xylabel,fontsize=5)
    ax.set_yticklabels(xylabel,fontsize=5)
    ax.set_xticks(np.arange(-0.5, len(xylabel), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(xylabel), 1), minor=True)
    ax.grid( which='minor')

    from mpl_toolkits.axes_grid1 import make_axes_locatable
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes("right", "5%", pad="3%")
    #plt.colorbar(im, cax=cax)
    plt.colorbar(im, ax=ax, shrink=0.9, cax=cax)
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    if number:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                ax.text(j, i, matrix[i][j], ha="center", va="center", color="w", fontsize=4)
    plt.tight_layout()
    if filename is not None:
        plt.savefig(filename + '.pdf', bbox_inches='tight', pad_inches = 0,)#
    plt.show()
    plt.close(fig)
if __name__ == "__main__":
    farmers = ["Agrifun_dhfidhfius_djifosjofijfjij", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
    correlation([[1, -0.2, 0.4, -0.9], [0.3, 1, -0.4, 0.02], [-0.1, 0.21, 1, 0.32], [0.2, -0.4, 0.08, 1]], farmers, "test", True)