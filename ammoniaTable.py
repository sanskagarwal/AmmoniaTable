import pandas as pd
df = pd.read_csv("saturated.csv")

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
        
from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Ammonia Steam Table")
tab_control = ttk.Notebook(window)

#Style
style = ttk.Style()
style.theme_create("mkkt", parent="alt", settings={
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

style.theme_use("mkkt")

#Commands
def pressureData():
    val = float(txt.get())
    mylist = saturatedPressure(val)
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

#Tab
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Saturated Ammonia(By Pressure)')
tab_control.add(tab2, text='Saturated Ammonia(By Temperature)')
tab_control.add(tab3, text='Super Heated Ammni')

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
    val = float(txt2.get())
    mylist = saturatedTemperature(val)
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

#both
tab_control.pack(expand=1, fill='both')
window.geometry('900x600')
window.attributes('-zoomed', True)
window.mainloop()