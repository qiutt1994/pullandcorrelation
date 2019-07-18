from pull import *
from correlation import *

sysnames = []
syspullcentre = []
syspullerror = []
statnames = []
statpullcentre = []
statpullerror = []
allnames = []
corrmatrix = []
with open("GlobalFit_fitres_unconditionnal_mu0.txt") as f:
    ispull = False
    iscorr = False
    havemu = False
    for each_line in f:
        if ispull:
            if "&" in each_line:
                iname = each_line.index("&")
                name_tem = each_line[0:iname]
                name_tem = name_tem.replace('\\','')
                name_tem = name_tem.replace(' ','')
                i1centre = each_line.index("$") + 1
                i2centre = each_line.index("^")
                pullcentre_tem = float(each_line[i1centre:i2centre])
                i1error = each_line.index("+") + 1
                i2error = each_line.index("}")
                pullerror_tem = float(each_line[i1error:i2error])
                allnames.append(name_tem)
                if not havemu:
                    if name_tem[0] == 'n':
                        allnames[-1] = 'mu'
                        allnames.append(name_tem)
                        havemu = True
                if "gamma_stat" in name_tem:
                    statnames.append(name_tem)
                    statpullcentre.append(pullcentre_tem)
                    statpullerror.append(pullerror_tem)
                else:
                    sysnames.append(name_tem)
                    syspullcentre.append(pullcentre_tem)
                    syspullerror.append(pullerror_tem)
            else:
                ispull = False
        elif iscorr:
            corr_tem = [float(i) for i in each_line.split()]
            if len(corr_tem) > 3:
                corrmatrix.append(corr_tem)
        if "NUISANCE_PARAMETERS" in each_line:
            ispull = True
        if "CORRELATION_MATRIX" in each_line:
            iscorr = True

pull(syspullcentre,syspullerror,sysnames,"pullplot")
pull(statpullcentre,statpullerror,statnames,"pullstatplot")

corrmatrix.reverse()
toberemove = []
realsysname = []
for i in range(len(allnames)):
    # if "gamma_stat" in allnames[i]:
    #     toberemove.append(i)
    # if "mu" == allnames[i]:
    #     toberemove.append(i)
    if allnames[i][0:3] != "Sys":
        toberemove.append(i)
        #print(allnames[i][0:3])
    else:
        realsysname.append(allnames[i])

syscorrmatrix = []
for i in range(len(allnames)):
    if i not in toberemove:
        tem_corr = []
        for j in range(len(corrmatrix[i])):
            if j not in toberemove:
                tem_corr.append(corrmatrix[i][j])
        syscorrmatrix.append(tem_corr)

#print(len(syscorrmatrix), len(syscorrmatrix[0]), len(realsysname))
correlation(syscorrmatrix, realsysname, "correlation_sys")