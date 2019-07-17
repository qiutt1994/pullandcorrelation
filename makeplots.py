from pull import *

sysnames = []
syspullcentre = []
syspullerror = []
statnames = []
statpullcentre = []
statpullerror = []
allnames = []

with open("GlobalFit_fitres_unconditionnal_mu0.txt") as f:
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
                if "gamma_stat" in name_tem:
                    statnames.append(name_tem)
                    statpullcentre.append(pullcentre_tem)
                    statpullerror.append(pullerror_tem)
                else:
                    print(name_tem)
                    sysnames.append(name_tem)
                    syspullcentre.append(pullcentre_tem)
                    syspullerror.append(pullerror_tem)
            else:
                ispull = False
        if "NUISANCE_PARAMETERS" in each_line:
            ispull = True
        if "CORRELATION_MATRIX" in each_line:
            iscorr = True

pull(syspullcentre,syspullerror,sysnames,"pullplot")
pull(statpullcentre,statpullerror,statnames,"pullstatplot")