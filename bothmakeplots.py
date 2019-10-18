from pull import *
from correlation import *


def makecorrelation(allnames, corrmatrix, filename):
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
    correlation(syscorrmatrix, realsysname, filename)

    toberemove = []
    for i in range(len(realsysname)):
        donotremoveit = 0
        for each in syscorrmatrix[i]:
            if abs(each) > 0.2:
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
    correlation(syscorrmatrix_sm, realsysname_sm, filename + "sm")

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
                corr_tem.reverse()
                corrmatrix.append(corr_tem)
        if "NUISANCE_PARAMETERS" in each_line:
            ispull = True
        if "CORRELATION_MATRIX" in each_line:
            iscorr = True


sysnames_as = []
syspullcentre_as = []
syspullerror_as = []
statnames_as = []
statpullcentre_as = []
statpullerror_as = []
allnames_as = []
corrmatrix_as = []
with open("GlobalFit_fitres_unconditionnal_mu0_as.txt") as f:
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
                allnames_as.append(name_tem)
                if not havemu:
                    if name_tem[0] == 'n':
                        allnames_as[-1] = 'mu'
                        allnames_as.append(name_tem)
                        havemu = True
                if "gamma_stat" in name_tem:
                    statnames_as.append(name_tem)
                    statpullcentre_as.append(pullcentre_tem)
                    statpullerror_as.append(pullerror_tem)
                else:
                    sysnames_as.append(name_tem)
                    syspullcentre_as.append(pullcentre_tem)
                    syspullerror_as.append(pullerror_tem)
            else:
                ispull = False
        elif iscorr:
            corr_tem = [float(i) for i in each_line.split()]
            if len(corr_tem) > 3:
                corr_tem.reverse()
                corrmatrix_as.append(corr_tem)
        if "NUISANCE_PARAMETERS" in each_line:
            ispull = True
        if "CORRELATION_MATRIX" in each_line:
            iscorr = True

for each, eachas in zip(sysnames, sysnames_as):
    if each != eachas:
        print("Error: sysname order does not match!")
        exit(1)

middlepull = int(len(sysnames)/2)
pull(syspullcentre,syspullerror,sysnames,"pullplot", datac=syspullcentre_as, datae=syspullerror_as)
pull(syspullcentre[0:middlepull],syspullerror[0:middlepull],sysnames[0:middlepull],"pullplot1", datac=syspullcentre_as[0:middlepull], datae=syspullerror_as[0:middlepull])
pull(syspullcentre[middlepull+1:],syspullerror[middlepull+1:],sysnames[middlepull+1:],"pullplot2", datac=syspullcentre_as[middlepull+1:], datae=syspullerror_as[middlepull+1:])
pull(statpullcentre,statpullerror,statnames,"pullstatplot", datac=statpullcentre_as, datae=statpullerror_as)

makecorrelation(allnames, corrmatrix, "correlation_sysandnorm")
makecorrelation(allnames_as, corrmatrix_as, "correlation_sysandnorm_as")