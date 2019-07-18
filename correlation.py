import matplotlib.pyplot as plt
import numpy as np
def correlation(matrix, xylabel, filename=None):
    fig = plt.figure(figsize=(int(len(matrix[0]))*2, int(len(matrix[0]))*2))
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(matrix)
    ax.set_xticks(np.arange(len(xylabel)))
    ax.set_yticks(np.arange(len(xylabel)))
    ax.set_xticklabels(xylabel)
    ax.set_yticklabels(xylabel)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            ax.text(j, i, matrix[i][j], ha="center", va="center", color="w", fontsize=30)
    plt.tight_layout()
    if filename is not None:
        plt.savefig(filename + '.pdf', bbox_inches='tight', pad_inches = 0, )#
    #plt.show()

if __name__ == "__main__":
    farmers = ["Agrifun_dhfidhfius_djifosjofijfjij", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]
    correlation([[1, -0.2, 0.4, -0.9], [0.3, 1, -0.4, 0.02], [-0.1, 0.21, 1, 0.32], [0.2, -0.4, 0.08, 1]], farmers, "test")