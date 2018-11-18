import pandas as pd
df = pd.read_csv("saturated.csv")
df1 = pd.read_csv("superheated.csv")

mini = {}
maxi = {}
minInd = {}
maxInd = {}
press = set()
for i in range(239):
    num = df1.iloc[i]['Psat']
    temp = df1.iloc[i]['Tsat']
    press.add(num)
    if(mini.get(num)):
        if(temp<mini.get(num)):
            mini[num]=temp
            minInd[num] = i
    else:
        mini.update({num : temp})
        minInd.update({num:i})
        
    if(maxi.get(num)):
        if(temp>maxi.get(num)):
            maxi[num]=temp
            maxInd[num] = i
    else:
        maxi.update({num : temp})
        maxInd.update({num : i})

def saturatedPressure(x):
    if(x<40 or x>2000):
        return -1
    if(x==40):
        Tsat = df.iloc[0]['Tsat']
        vf = df.iloc[0]['vf']
        vfg = df.iloc[0]['vfg']
        vg = vf + vfg
        uf = df.iloc[0]['uf']
        ufg = df.iloc[0]['ufg']
        ug = uf + ufg
        hf = df.iloc[0]['hf']
        hfg = df.iloc[0]['hfg']
        hg = hf + hfg
        sf = df.iloc[0]['sf']
        sfg = df.iloc[0]['sfg']
        sg = sf + sfg
        return [x,Tsat,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
    if(x==2000):
        Tsat = df.iloc[103]['Tsat']
        vf = df.iloc[103]['vf']
        vfg = df.iloc[103]['vfg']
        vg = vf + vfg
        uf = df.iloc[103]['uf']
        ufg = df.iloc[103]['ufg']
        ug = uf + ufg
        hf = df.iloc[103]['hf']
        hfg = df.iloc[103]['hfg']
        hg = hf + hfg
        sf = df.iloc[103]['sf']
        sfg = df.iloc[103]['sfg']
        sg = sf + sfg
        return [x,Tsat,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
    for i in range(0,105):
        if(x<df.iloc[i]['Psat']):
            upper=i
            lower=i-1
            x1 = df.iloc[i]['Psat']
            x2 = df.iloc[i-1]['Psat']
            uTsat = df.iloc[i]['Tsat']
            lTsat = df.iloc[i-1]['Tsat']
            uvf = df.iloc[i]['vf']
            lvf = df.iloc[i-1]['vf']
            uvfg = df.iloc[i]['vfg']
            lvfg = df.iloc[i-1]['vfg']
            uuf = df.iloc[i]['uf']
            luf = df.iloc[i-1]['uf']
            uufg = df.iloc[i]['ufg']
            lufg = df.iloc[i-1]['ufg']
            uhf = df.iloc[i]['hf']
            lhf = df.iloc[i-1]['hf']
            uhfg = df.iloc[i]['hfg']
            lhfg = df.iloc[i-1]['hfg']
            usf = df.iloc[i]['sf']
            lsf = df.iloc[i-1]['sf']
            usfg = df.iloc[i]['sfg']
            lsfg = df.iloc[i-1]['sfg']
            Tsat = ((x2-x)/((x2-x1)*1.0))*lTsat*1.0 + ((x-x1)/((x2-x1)*1.0))*uTsat*1.0
            vf = ((x2-x)/((x2-x1)*1.0))*lvf*1.0 + ((x-x1)/((x2-x1)*1.0))*uvf*1.0
            vfg = ((x2-x)/((x2-x1)*1.0))*lvfg*1.0 + ((x-x1)/((x2-x1)*1.0))*uvfg*1.0
            vg = vf + vfg
            uf = ((x2-x)/((x2-x1)*1.0))*luf*1.0 + ((x-x1)/((x2-x1)*1.0))*uuf*1.0
            ufg = ((x2-x)/((x2-x1)*1.0))*lufg*1.0 + ((x-x1)/((x2-x1)*1.0))*uufg*1.0
            ug = uf + ufg
            hf = ((x2-x)/((x2-x1)*1.0))*lhf*1.0 + ((x-x1)/((x2-x1)*1.0))*uhf*1.0
            hfg = ((x2-x)/((x2-x1)*1.0))*lhfg*1.0 + ((x-x1)/((x2-x1)*1.0))*uhfg*1.0
            hg = hf + hfg
            sf = ((x2-x)/((x2-x1)*1.0))*lsf*1.0 + ((x-x1)/((x2-x1)*1.0))*usf*1.0
            sfg = ((x2-x)/((x2-x1)*1.0))*lsfg*1.0 + ((x-x1)/((x2-x1)*1.0))*usfg*1.0
            sg = sf + sfg
            return [x,Tsat,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
        elif(x==df.iloc[i]['Psat']):
            Tsat = df.iloc[i]['Tsat']
            vf = df.iloc[i]['vf']
            vfg = df.iloc[i]['vfg']
            vg = vf + vfg
            uf = df.iloc[i]['uf']
            ufg = df.iloc[i]['ufg']
            ug = uf + ufg
            hf = df.iloc[i]['hf']
            hfg = df.iloc[i]['hfg']
            hg = hf + hfg
            sf = df.iloc[i]['sf']
            sfg = df.iloc[i]['sfg']
            sg = sf + sfg
            return [x,Tsat,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
        
def saturatedTemperature(x):
    if(x<-50.3 or x>50):
        return -1
    if(x==-50.3):
        Psat = df.iloc[0]['Psat']
        vf = df.iloc[0]['vf']
        vfg = df.iloc[0]['vfg']
        vg = vf + vfg
        uf = df.iloc[0]['uf']
        ufg = df.iloc[0]['ufg']
        ug = uf + ufg
        hf = df.iloc[0]['hf']
        hfg = df.iloc[0]['hfg']
        hg = hf + hfg
        sf = df.iloc[0]['sf']
        sfg = df.iloc[0]['sfg']
        sg = sf + sfg
        return [Psat,x,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
    if(x==50):
        Psat = df.iloc[104]['Psat']
        vf = df.iloc[104]['vf']
        vfg = df.iloc[104]['vfg']
        vg = vf + vfg
        uf = df.iloc[104]['uf']
        ufg = df.iloc[104]['ufg']
        ug = uf + ufg
        hf = df.iloc[104]['hf']
        hfg = df.iloc[104]['hfg']
        hg = hf + hfg
        sf = df.iloc[104]['sf']
        sfg = df.iloc[104]['sfg']
        sg = sf + sfg
        return [Psat,x,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
    for i in range(0,105):
        if(x<df.iloc[i]['Tsat']):
            upper=i
            lower=i-1
            x1 = df.iloc[i]['Tsat']
            x2 = df.iloc[i-1]['Tsat']
            uPsat = df.iloc[i]['Psat']
            lPsat = df.iloc[i-1]['Psat']
            uvf = df.iloc[i]['vf']
            lvf = df.iloc[i-1]['vf']
            uvfg = df.iloc[i]['vfg']
            lvfg = df.iloc[i-1]['vfg']
            uuf = df.iloc[i]['uf']
            luf = df.iloc[i-1]['uf']
            uufg = df.iloc[i]['ufg']
            lufg = df.iloc[i-1]['ufg']
            uhf = df.iloc[i]['hf']
            lhf = df.iloc[i-1]['hf']
            uhfg = df.iloc[i]['hfg']
            lhfg = df.iloc[i-1]['hfg']
            usf = df.iloc[i]['sf']
            lsf = df.iloc[i-1]['sf']
            usfg = df.iloc[i]['sfg']
            lsfg = df.iloc[i-1]['sfg']
            Psat = ((x2-x)/((x2-x1)*1.0))*lPsat*1.0 + ((x-x1)/((x2-x1)*1.0))*uPsat*1.0
            vf = ((x2-x)/((x2-x1)*1.0))*lvf*1.0 + ((x-x1)/((x2-x1)*1.0))*uvf*1.0
            vfg = ((x2-x)/((x2-x1)*1.0))*lvfg*1.0 + ((x-x1)/((x2-x1)*1.0))*uvfg*1.0
            vg = vf + vfg
            uf = ((x2-x)/((x2-x1)*1.0))*luf*1.0 + ((x-x1)/((x2-x1)*1.0))*uuf*1.0
            ufg = ((x2-x)/((x2-x1)*1.0))*lufg*1.0 + ((x-x1)/((x2-x1)*1.0))*uufg*1.0
            ug = uf + ufg
            hf = ((x2-x)/((x2-x1)*1.0))*lhf*1.0 + ((x-x1)/((x2-x1)*1.0))*uhf*1.0
            hfg = ((x2-x)/((x2-x1)*1.0))*lhfg*1.0 + ((x-x1)/((x2-x1)*1.0))*uhfg*1.0
            hg = hf + hfg
            sf = ((x2-x)/((x2-x1)*1.0))*lsf*1.0 + ((x-x1)/((x2-x1)*1.0))*usf*1.0
            sfg = ((x2-x)/((x2-x1)*1.0))*lsfg*1.0 + ((x-x1)/((x2-x1)*1.0))*usfg*1.0
            sg = sf + sfg
            return [Psat,x,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
        elif(x==df.iloc[i]['Tsat']):
            Psat = df.iloc[i]['Psat']
            vf = df.iloc[i]['vf'] 
            vfg = df.iloc[i]['vfg']
            vg = vf + vfg
            uf = df.iloc[i]['uf']
            ufg = df.iloc[i]['ufg']
            ug = uf + ufg
            hf = df.iloc[i]['hf']
            hfg = df.iloc[i]['hfg']
            hg = hf + hfg
            sf = df.iloc[i]['sf']
            sfg = df.iloc[i]['sfg']
            sg = sf + sfg
            return [Psat,x,vf,vfg,vg,uf,ufg,ug,hf,hfg,hg,sf,sfg,sg] 
        

def superheated(x,y):
    if(x>2000 or x<50):
        return -2
    if(x in press):
        if(y<mini[x] or y>maxi[x]):
            return [-1,mini[x],maxi[x]]
        lInd = minInd[x]
        rInd = maxInd[x]+1
        for i in range(lInd,rInd):
            if(y<df1.iloc[i]['Tsat']):
                x1 = df1.iloc[i]['Tsat']
                x2 = df1.iloc[i-1]['Tsat']
                uv = df1.iloc[i]['v']
                lv = df1.iloc[i-1]['v']
                uu = df1.iloc[i]['u']
                lu = df1.iloc[i-1]['u']
                uh = df1.iloc[i]['h']
                lh = df1.iloc[i-1]['h']
                us = df1.iloc[i]['s']
                ls = df1.iloc[i-1]['s']
                v = ((x2-y)/((x2-x1)*1.0))*lv*1.0 + ((y-x1)/((x2-x1)*1.0))*uv*1.0
                u = ((x2-y)/((x2-x1)*1.0))*lu*1.0 + ((y-x1)/((x2-x1)*1.0))*uu*1.0
                h = ((x2-y)/((x2-x1)*1.0))*lh*1.0 + ((y-x1)/((x2-x1)*1.0))*uh*1.0
                s = ((x2-y)/((x2-x1)*1.0))*ls*1.0 + ((y-x1)/((x2-x1)*1.0))*us*1.0
                return [x,y,v,u,h,s]
            elif(y==df1.iloc[i]['Tsat']):
                v = df1.iloc[i]['v']
                u = df1.iloc[i]['u']
                h = df1.iloc[i]['h']
                s = df1.iloc[i]['s']
                return [x,y,v,u,h,s]
    else:      
        try:  
            lNum = 0
            rNum = 0
            ls =[]
            for i in press:
                ls.append(i)
            ls.sort()
            for i in range(0,21):
                if(x<ls[i]):
                    lNum = ls[i-1]
                    rNum = ls[i]
                    break
            if(y<df1.iloc[minInd[rNum]]['Tsat'] or y>df1.iloc[maxInd[rNum]]['Tsat']):
                return [-1,mini[rNum],maxi[rNum]]
            lyNum = 0
            ryNum = 0
            for i in range(minInd[rNum],maxInd[rNum]+1):
                if(y<=df1.iloc[i]['Tsat']):
                    lyNum = df1.iloc[i-1]['Tsat']
                    ryNum = df1.iloc[i]['Tsat']
                    break
            lefth = 0
            righth = 0
            for i in range(minInd[lNum],maxInd[lNum]+1):
                if(df1.iloc[i]['Tsat']==lyNum):
                    lefth = 1
                if(df1.iloc[i]['Tsat']==ryNum):
                    righth = 1
            x1 = lNum
            x2 = rNum
            y1 = lyNum
            y2 = ryNum
            if(lefth==1 and righth==1):
                df2 = df1.loc[(df1['Psat']==lNum) & (df1['Tsat']==lyNum)]
                ulv = df2.iloc[0]['v']
                ulu = df2.iloc[0]['u']
                ulh = df2.iloc[0]['h']
                uls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==lNum) & (df1['Tsat']==ryNum)]
                uuv = df2.iloc[0]['v']
                uuu = df2.iloc[0]['u']
                uuh = df2.iloc[0]['h']
                uus = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==lyNum)]
                llv = df2.iloc[0]['v']
                llu = df2.iloc[0]['u']
                llh = df2.iloc[0]['h']
                lls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==ryNum)]
                luv = df2.iloc[0]['v']
                luu = df2.iloc[0]['u']
                luh = df2.iloc[0]['h']
                lus = df2.iloc[0]['s']

                v = (((y2-y)/((y2-y1)*1.0))*ulv*1.0 + ((y-y1)/((y2-y1)*1.0))*uuv*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llv*1.0 + ((y-y1)/((y2-y1)*1.0))*luv*1.0)*((x-x1)/(x2-x1))
                u = (((y2-y)/((y2-y1)*1.0))*ulu*1.0 + ((y-y1)/((y2-y1)*1.0))*uuu*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llu*1.0 + ((y-y1)/((y2-y1)*1.0))*luu*1.0)*((x-x1)/(x2-x1))
                h = (((y2-y)/((y2-y1)*1.0))*ulh*1.0 + ((y-y1)/((y2-y1)*1.0))*uuh*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llh*1.0 + ((y-y1)/((y2-y1)*1.0))*luh*1.0)*((x-x1)/(x2-x1))
                s = (((y2-y)/((y2-y1)*1.0))*uls*1.0 + ((y-y1)/((y2-y1)*1.0))*uus*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*lls*1.0 + ((y-y1)/((y2-y1)*1.0))*lus*1.0)*((x-x1)/(x2-x1))
                return [x,y,v,u,h,s]       
            if(lefth==0 and righth==1):
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==lyNum)]
                ulv = df2.iloc[0]['v']
                ulu = df2.iloc[0]['u']
                ulh = df2.iloc[0]['h']
                uls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==lNum) & (df1['Tsat']==ryNum)]
                uuv = df2.iloc[0]['v']
                uuu = df2.iloc[0]['u']
                uuh = df2.iloc[0]['h']
                uus = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==lyNum)]
                llv = df2.iloc[0]['v']
                llu = df2.iloc[0]['u']
                llh = df2.iloc[0]['h']
                lls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==ryNum)]
                luv = df2.iloc[0]['v']
                luu = df2.iloc[0]['u']
                luh = df2.iloc[0]['h']
                lus = df2.iloc[0]['s']

                v = (((y2-y)/((y2-y1)*1.0))*ulv*1.0 + ((y-y1)/((y2-y1)*1.0))*uuv*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llv*1.0 + ((y-y1)/((y2-y1)*1.0))*luv*1.0)*((x-x1)/(x2-x1))
                u = (((y2-y)/((y2-y1)*1.0))*ulu*1.0 + ((y-y1)/((y2-y1)*1.0))*uuu*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llu*1.0 + ((y-y1)/((y2-y1)*1.0))*luu*1.0)*((x-x1)/(x2-x1))
                h = (((y2-y)/((y2-y1)*1.0))*ulh*1.0 + ((y-y1)/((y2-y1)*1.0))*uuh*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llh*1.0 + ((y-y1)/((y2-y1)*1.0))*luh*1.0)*((x-x1)/(x2-x1))
                s = (((y2-y)/((y2-y1)*1.0))*uls*1.0 + ((y-y1)/((y2-y1)*1.0))*uus*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*lls*1.0 + ((y-y1)/((y2-y1)*1.0))*lus*1.0)*((x-x1)/(x2-x1))
                return [x,y,v,u,h,s]    
            if(lefth==1 and righth==0):
                df2 = df1.loc[(df1['Psat']==lNum) & (df1['Tsat']==lyNum)]
                ulv = df2.iloc[0]['v']
                ulu = df2.iloc[0]['u']
                ulh = df2.iloc[0]['h']
                uls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==ryNum)]
                uuv = df2.iloc[0]['v']
                uuu = df2.iloc[0]['u']
                uuh = df2.iloc[0]['h']
                uus = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==lyNum)]
                llv = df2.iloc[0]['v']
                llu = df2.iloc[0]['u']
                llh = df2.iloc[0]['h']
                lls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==ryNum)]
                luv = df2.iloc[0]['v']
                luu = df2.iloc[0]['u']
                luh = df2.iloc[0]['h']
                lus = df2.iloc[0]['s']

                v = (((y2-y)/((y2-y1)*1.0))*ulv*1.0 + ((y-y1)/((y2-y1)*1.0))*uuv*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llv*1.0 + ((y-y1)/((y2-y1)*1.0))*luv*1.0)*((x-x1)/(x2-x1))
                u = (((y2-y)/((y2-y1)*1.0))*ulu*1.0 + ((y-y1)/((y2-y1)*1.0))*uuu*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llu*1.0 + ((y-y1)/((y2-y1)*1.0))*luu*1.0)*((x-x1)/(x2-x1))
                h = (((y2-y)/((y2-y1)*1.0))*ulh*1.0 + ((y-y1)/((y2-y1)*1.0))*uuh*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llh*1.0 + ((y-y1)/((y2-y1)*1.0))*luh*1.0)*((x-x1)/(x2-x1))
                s = (((y2-y)/((y2-y1)*1.0))*uls*1.0 + ((y-y1)/((y2-y1)*1.0))*uus*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*lls*1.0 + ((y-y1)/((y2-y1)*1.0))*lus*1.0)*((x-x1)/(x2-x1))
                return [x,y,v,u,h,s]    
            if(lefth==0 and righth==0):
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==lyNum)]
                ulv = df2.iloc[0]['v']
                ulu = df2.iloc[0]['u']
                ulh = df2.iloc[0]['h']
                uls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==ryNum)]
                uuv = df2.iloc[0]['v']
                uuu = df2.iloc[0]['u']
                uuh = df2.iloc[0]['h']
                uus = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==lyNum)]
                llv = df2.iloc[0]['v']
                llu = df2.iloc[0]['u']
                llh = df2.iloc[0]['h']
                lls = df2.iloc[0]['s']
                df2 = df1.loc[(df1['Psat']==rNum) & (df1['Tsat']==ryNum)]
                luv = df2.iloc[0]['v']
                luu = df2.iloc[0]['u']
                luh = df2.iloc[0]['h']
                lus = df2.iloc[0]['s']

                v = (((y2-y)/((y2-y1)*1.0))*ulv*1.0 + ((y-y1)/((y2-y1)*1.0))*uuv*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llv*1.0 + ((y-y1)/((y2-y1)*1.0))*luv*1.0)*((x-x1)/(x2-x1))
                u = (((y2-y)/((y2-y1)*1.0))*ulu*1.0 + ((y-y1)/((y2-y1)*1.0))*uuu*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llu*1.0 + ((y-y1)/((y2-y1)*1.0))*luu*1.0)*((x-x1)/(x2-x1))
                h = (((y2-y)/((y2-y1)*1.0))*ulh*1.0 + ((y-y1)/((y2-y1)*1.0))*uuh*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*llh*1.0 + ((y-y1)/((y2-y1)*1.0))*luh*1.0)*((x-x1)/(x2-x1))
                s = (((y2-y)/((y2-y1)*1.0))*uls*1.0 + ((y-y1)/((y2-y1)*1.0))*uus*1.0)*((x2-x)/(x2-x1))+(((y2-y)/((y2-y1)*1.0))*lls*1.0 + ((y-y1)/((y2-y1)*1.0))*lus*1.0)*((x-x1)/(x2-x1))
                return [x,y,v,u,h,s]     
        except:
            return -3
        
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window = Tk()
window.title("Ammonia Steam Table")
tab_control = ttk.Notebook(window)

#Style
style = ttk.Style()
style.theme_create("mkt", parent="alt", settings={
    "TNotebook": {
        "configure": {
            "tabmargins": [2, 2, 2, 2],
            "background": "#333333",
            },
    },
    "TNotebook.Tab": {
        "configure": {
            "padding": [5, 1], 
            "background": "#333333",
            "foreground": "white",
            "font": ["system",11],
            "padding": [10,10]
        },
        "map": {
            "background": [("selected", "#F57713")],
            "expand": [("selected", [1, 1, 1, 0])] 
        } 
    },
    "TFrame": {
        "configure": {
            "background": "#333333",
        }
    }
})

style.theme_use("mkt")

#Commands
def pressureData():
    try:
        val = float(txt.get())
        mylist = saturatedPressure(val)
        if(mylist==-1):
            messagebox.showwarning('Out of range error', 'Please Enter Pressure(in kPa) between [40,2000]')
        else:
            Psat.configure(text="Saturation Pressure Psat = {} kPa".format(mylist[0]))
            Tsat.configure(text="Saturation Temperature Tsat = {} C".format(mylist[1]))
            vfl.configure(text="Specific Volume vf = {} m3/kg".format(mylist[2]))
            vfgl.configure(text="Specific Volume vfg = {} m3/kg".format(mylist[3]))
            vgl.configure(text="Specific Volume vg = {} m3/kg".format(mylist[4]))
            ufl.configure(text="Internal Energy uf = {} kJ/kg".format(mylist[5]))
            ufgl.configure(text="Internal Energy ufg = {} kJ/kg".format(mylist[6]))
            ugl.configure(text="Internal Energy ug = {} kJ/kg".format(mylist[7]))
            hfl.configure(text="Enthalpy hf = {} kJ/kg".format(mylist[8]))
            hfgl.configure(text="Enthalpy hfg = {} kJ/kg".format(mylist[9]))
            hgl.configure(text="Enthalpy hg = {} kJ/kg".format(mylist[10]))
            sfl.configure(text="Entropy sf = {} kJ/(kg*K)".format(mylist[11]))
            sfgl.configure(text="Entropy sfg = {} kJ/(kg*K)".format(mylist[12]))
            sgl.configure(text="Entropy sg = {} kJ/(kg*K)".format(mylist[13]))
    except:
        messagebox.showwarning('Irrelevant Data', 'Please Enter Pressure(in kPa)')
    
#Tab
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Saturated Ammonia(By Pressure)')
tab_control.add(tab2, text='Saturated Ammonia(By Temperature)')
tab_control.add(tab3, text='Super Heated Ammonia')

#Tab 1
lbl1 = Label(tab1, text = 'Ammonia Pressure (kPa)',font=("Helvetica Bold", 15),foreground="#43ABC8", background="#333333")
lbl1.grid(column=0, row=0, pady=(10,0))
txt = Entry(tab1,width=20)
txt.grid(column=1, row=0, padx=(5,0), pady=(10,0))
txt.focus()
pData = Button(tab1, text="Submit", command=pressureData,relief=RAISED, background="#3598DC", foreground="white")
pData.grid(column=3, row=0, padx=(5,0), pady=(10,0))

Psat = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
Psat.grid(column=0,row=1, pady=(30,0))
Tsat = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
Tsat.grid(column=0,row=2, pady=(10,0))
vfl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
vfl.grid(column=0,row=3, pady=(10,0))
vfgl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
vfgl.grid(column=0,row=4, pady=(10,0))
vgl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
vgl.grid(column=0,row=5, pady=(10,0))
ufl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
ufl.grid(column=0,row=6,  pady=(10,0))
ufgl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
ufgl.grid(column=0,row=7, pady=(10,0))
ugl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
ugl.grid(column=0,row=8, pady=(10,0))
hfl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
hfl.grid(column=0,row=9, pady=(10,0))
hfgl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
hfgl.grid(column=0,row=10, pady=(10,0))
hgl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
hgl.grid(column=0,row=11, pady=(10,0))
sfl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
sfl.grid(column=0,row=12, pady=(10,0))
sfgl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
sfgl.grid(column=0,row=13, pady=(10,0))
sgl = Label(tab1,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
sgl.grid(column=0,row=14, pady=(10,0))

def temperatureData():
    try:
        val = float(txt2.get())
        mylist = saturatedTemperature(val)
        if(mylist==-1):
            messagebox.showwarning('Out of Range Error', 'Please Enter Temperature(in C) between [-50.3,50]')
        else:
            Psat2.configure(text="Saturation Pressure Psat = {} kPa".format(mylist[0]))
            Tsat2.configure(text="Saturation Temperature Tsat = {} C".format(mylist[1]))
            vfl2.configure(text="Specific Volume vf = {} m3/kg".format(mylist[2]))
            vfgl2.configure(text="Specific Volume vfg = {} m3/kg".format(mylist[3]))
            vgl2.configure(text="Specific Volume vg = {} m3/kg".format(mylist[4]))
            ufl2.configure(text="Internal Energy uf = {} kJ/kg".format(mylist[5]))
            ufgl2.configure(text="Internal Energy ufg = {} kJ/kg".format(mylist[6]))
            ugl2.configure(text="Internal Energy ug = {} kJ/kg".format(mylist[7]))
            hfl2.configure(text="Enthalpy hf = {} kJ/kg".format(mylist[8]))
            hfgl2.configure(text="Enthalpy hfg = {} kJ/kg".format(mylist[9]))
            hgl2.configure(text="Enthalpy hg = {} kJ/kg".format(mylist[10]))
            sfl2.configure(text="Entropy sf = {} kJ/(kg*K)".format(mylist[11]))
            sfgl2.configure(text="Entropy sfg = {} kJ/(kg*K)".format(mylist[12]))
            sgl2.configure(text="Entropy sg = {} kJ/(kg*K)".format(mylist[13]))
    except:
        messagebox.showwarning('Irrelevant Data', 'Please Enter Temperature(in C)')
    

#Tab 2
lbl2 = Label(tab2, text = 'Ammonia Temperature (C)',font=("Helvetica Bold", 15),foreground="#43ABC8", background="#333333")
lbl2.grid(column=0, row=0, pady=(10,0))
txt2 = Entry(tab2,width=20)
txt2.grid(column=1, row=0, padx=(5,0), pady=(10,0))
txt2.focus()
tData = Button(tab2, text="Submit", command=temperatureData,relief=RAISED, background="#3598DC", foreground="white")
tData.grid(column=3, row=0, padx=(5,0), pady=(10,0))

Psat2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
Psat2.grid(column=0,row=1, pady=(30,0))
Tsat2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
Tsat2.grid(column=0,row=2, pady=(10,0))
vfl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
vfl2.grid(column=0,row=3, pady=(10,0))
vfgl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
vfgl2.grid(column=0,row=4, pady=(10,0))
vgl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
vgl2.grid(column=0,row=5, pady=(10,0))
ufl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
ufl2.grid(column=0,row=6,  pady=(10,0))
ufgl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
ufgl2.grid(column=0,row=7, pady=(10,0))
ugl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
ugl2.grid(column=0,row=8, pady=(10,0))
hfl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
hfl2.grid(column=0,row=9, pady=(10,0))
hfgl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
hfgl2.grid(column=0,row=10, pady=(10,0))
hgl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
hgl2.grid(column=0,row=11, pady=(10,0))
sfl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
sfl2.grid(column=0,row=12, pady=(10,0))
sfgl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
sfgl2.grid(column=0,row=13, pady=(10,0))
sgl2 = Label(tab2,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
sgl2.grid(column=0,row=14, pady=(10,0))

def superData():
    try:
        val1 = float(txt3.get())
        val2 = float(txt4.get())
        mylist = superheated(val1,val2)
        if(mylist==-2):
            messagebox.showwarning('Out of Range Error', 'Please Enter Pressure(in kPa) between [50,2000]')
        elif(mylist==-3):
            messagebox.showwarning('Sorry', 'Internal Error')
        else:
            if(mylist[0]==-1):
                messagebox.showwarning("Out of Range Error", "Please Enter Temperature(in C) between [{},{}]".format(mylist[1],mylist[2]))
            else: 
                Psat3.configure(text="Saturation Pressure Psat = {} kPa".format(mylist[0]))
                Tsat3.configure(text="Saturation Temperature Tsat = {} C".format(mylist[1]))
                v3.configure(text="Volume v = {} m3/kg".format(mylist[2]))
                u3.configure(text="Internal Energy u = {} m3/kg".format(mylist[3]))
                h3.configure(text="Enthalpy h = {} m3/kg".format(mylist[4]))
                s3.configure(text="Entropy s = {} kJ/kg".format(mylist[5]))
    except:
        messagebox.showwarning('Irrelevant Data', 'Please Enter Data Properly')

#Tab 3
lbl3 = Label(tab3, text = 'Ammonia Pressure (kPa)',font=("Helvetica Bold", 15),foreground="#43ABC8", background="#333333")
lbl3.grid(column=0, row=0, pady=(10,0))
txt3 = Entry(tab3,width=20)
txt3.grid(column=1, row=0, padx=(5,0), pady=(10,0))
txt3.focus()
lbl4 = Label(tab3, text = 'Ammonia Temperature (C)',font=("Helvetica Bold", 15),foreground="#43ABC8", background="#333333")
lbl4.grid(column=0, row=1, pady=(10,0))
txt4 = Entry(tab3,width=20)
txt4.grid(column=1, row=1, padx=(5,0), pady=(10,0))
supData = Button(tab3, text="Submit", command=superData,relief=RAISED, background="#3598DC", foreground="white")
supData.grid(column=0, row=2, pady=(10,0))

Psat3 = Label(tab3,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
Psat3.grid(column=0,row=3, pady=(30,0))
Tsat3 = Label(tab3,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
Tsat3.grid(column=0,row=4, pady=(10,0))
v3 = Label(tab3,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
v3.grid(column=0,row=5, pady=(10,0))
u3 = Label(tab3,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
u3.grid(column=0,row=6, pady=(10,0))
h3 = Label(tab3,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
h3.grid(column=0,row=7, pady=(10,0))
s3 = Label(tab3,text = "", font=("Helvetica Bold", 11), foreground="#ff0000", background="#333333")
s3.grid(column=0,row=8, pady=(5,0))

#both
tab_control.pack(expand=1, fill='both')
window.geometry('900x600')
window.attributes('-zoomed', True)
window.mainloop()