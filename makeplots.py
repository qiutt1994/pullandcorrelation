from pull import *
from correlation import *
import os

sysnames = []
syspullcentre = []
syspullerror = []
statnames = []
statpullcentre = []
statpullerror = []
allnames = []
corrmatrix = []

havemu = False
asimovfile = "GlobalFit_fitres_unconditionnal_mu0.txt"
if "GlobalFit_fitres_conditionnal_mu0.txt" in os.listdir():
    asimovfile = "GlobalFit_fitres_conditionnal_mu0.txt"
    havemu = True

with open(asimovfile) as f:
    ispull = False
    iscorr = False
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
                corr_tem.reverse()
                corrmatrix.append(corr_tem)
        if "NUISANCE_PARAMETERS" in each_line:
            ispull = True
        if "CORRELATION_MATRIX" in each_line:
            iscorr = True

pull(syspullcentre,syspullerror,sysnames,"pullplot")
pull(statpullcentre,statpullerror,statnames,"pullstatplot")

middlepull = int(len(sysnames)/2)
pull(syspullcentre[0:middlepull],syspullerror[0:middlepull],sysnames[0:middlepull],"pullplot1")
pull(syspullcentre[middlepull+1:],syspullerror[middlepull+1:],sysnames[middlepull+1:],"pullplot2")

#corrmatrix.reverse()
toberemove = []
realsysname = []
for i in range(len(allnames)):
    # if "gamma_stat" in allnames[i]:
    #     toberemove.append(i)
    # if "mu" == allnames[i]:
    #     toberemove.append(i)
    #if allnames[i][0:3] != "Sys":
    if "bin" in allnames[i]:
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
correlation(syscorrmatrix, realsysname, "correlation_sysandnorm")

toberemove = []
for i in range(len(realsysname)):
    donotremoveit = 0
    for each in syscorrmatrix[i]:
        if abs(each) > 0.3:
            donotremoveit += 1
    if donotremoveit < 2:
        toberemove.append(i)


#print(toberemove)
syscorrmatrix_sm = []
realsysname_sm = []
for i in range(len(realsysname)):
    if i in toberemove:
        continue
    realsysname_sm.append(realsysname[i])
    tem = []
    for j in range(len(syscorrmatrix[i])):
        if j not in toberemove:
            tem.append(syscorrmatrix[i][j])
    syscorrmatrix_sm.append(tem)
correlation(syscorrmatrix_sm, realsysname_sm, "correlation_sysandnorm_sm", number=True)
