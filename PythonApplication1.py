import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('bmh')
#A következő sor a grafikonok stílusát "Képregényszerűre" változtatja
#plt.xkcd()

readed = pd.read_excel("turizmus.xls")

Ev = readed['Ev']
Ferohely = readed['Ferohely']
Egyseg = readed['Egyseg']
Vendeg = readed['Vendeg']
Vendegelyszakak = readed['Vendegelyszakak']

readed['Kihasznaltsag'] = readed['Vendeg']/readed['Ferohely']*100
Kihasznaltsag = readed['Kihasznaltsag']

readed['Foglalt_ejszakak'] = readed['Vendegelyszakak']/readed['Vendeg']
Foglalt_ejszakak = readed['Foglalt_ejszakak']

Vendegek_evtizedenkent = [0,0,0,0,0]

for i in range(len(Ev)):
    if(Ev[i]<1970): 
        Vendegek_evtizedenkent[0] += Vendeg[i]
    else: 
        if(Ev[i]<1980):
            Vendegek_evtizedenkent[1] += Vendeg[i]
        else:
            if(Ev[i]<1990):
                Vendegek_evtizedenkent[2] += Vendeg[i]
            else:
                if(Ev[i]<2000):
                    Vendegek_evtizedenkent[3] += Vendeg[i]
                else:
                    if(Ev[i]<2010):
                        Vendegek_evtizedenkent[4] += Vendeg[i]




# 1_graf grafikon a ferohelyekrol evszamok szerint

#plt.xlabel('Ev')
#plt.ylabel('Ferohely')
#plt.title('Ferohely/Ev')
#plt.plot(Ev,Ferohely,'g-', linewidth = 3 ,label = 'Ferohely')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
##plt.savefig('1_graf.png')
#plt.show()


# 2_graf grafikon a vendegelyszakakrol es a vendegekrol evszamok szerint

#plt.xlabel('Ev')
#plt.title('Vendegelyszakak/Vendegek/Ev')
#plt.plot(Ev,Vendegelyszakak,'r--',label = 'Vendegelyszakak')
#plt.plot(Ev,Vendeg,'g--',label = 'Vendeg')
#plt.fill_between(Ev,Vendegelyszakak,Vendeg,interpolate=True,alpha = 0.25,color = 'red')
#plt.fill_between(Ev,Vendeg,interpolate=True,alpha = 0.25,color = 'green')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
##plt.savefig('2_graf.png')
#plt.show()


# 3_graf oszlopdiagram + grafikon Ferohelyek, Vendegek, Vendegelyszakak

#plt.xlabel('Ev')
#plt.bar(Ev,Ferohely, label = 'Ferohely')
#plt.plot(Ev,Vendegelyszakak,'g-',label = 'Vendegelyszakak')
#plt.plot(Ev,Vendeg,'r-',label = 'Vendeg')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
#plt.savefig('3_graf.png')
#plt.show()


# 4_graf grafikon a vendegelyszakakrol es a vendegekrol evszamok szerint

#plt.xlabel('Ev')
#plt.title('Ferohelyek/Vendegek/Ev')
#plt.bar(Ev,Ferohely,label = 'Ferohely')
#plt.bar(Ev,Vendeg,label = 'Vendeg')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
#plt.savefig('4_graf.png')
#plt.show()


# 5_graf oszlopdiagram a vendegek es a vendegelyszakak szamarol

#Ev_indexes = np.arange(len(Ev))
#def_width = 0.4
#
#plt.figure(figsize=(10,4))
#plt.xlabel('Ev')
#plt.title('Vendegelyszakak/Vendegek/Ev')
#plt.bar(Ev_indexes-def_width/2,Vendegelyszakak, width = def_width, label = 'Vendegelyszakak')
#plt.bar(Ev_indexes+def_width/2,Vendeg, width = def_width, label = 'Vendeg')
#plt.legend()
#plt.xticks(ticks = Ev_indexes, labels = Ev, rotation = 90)
#plt.grid(True)
#plt.tight_layout()
##plt.savefig('5_graf.png')
#plt.show()

# 6_graf diagram eloallitott adatbol kihasznaltsagrol

#plt.xlabel('Ev')
#plt.ylabel('Kihasznaltsag (%)')
#plt.title('Evszerinti szazalekos kihasznaltsag')
#plt.plot(Ev,Kihasznaltsag,'r-', linewidth = 2 ,label = 'Kihasznaltsag')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
##plt.savefig('6_graf.png')
#plt.show()

# 7_graf oszlop diagram eloallitott adatbol foglalt helyekrol

#plt.xlabel('Ev')
#plt.ylabel('Foglalt ejszakak(db)')
#plt.title('Evszerinti foglalt ejszakak darabszama')
#plt.plot(Ev,Foglalt_ejszakak,'y-', linewidth = 2 ,label = 'Foglalt ejszakak')
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
##plt.savefig('7_graf.png')
#plt.show()

# 8_graf tortadiagram eloallitott adatokbol a vendegek evtizendenkenti eloszlasarol


#labels = ['60-as evek','70-es evek','80-as evek','90-es evek','00-es evek']
#colors = ['blue','red','green','yellow','purple']
#explode = [0.3,0,0,0,0]
#plt.pie(Vendegek_evtizedenkent, labels=labels, colors = colors, explode = explode, shadow = True ,wedgeprops={'edgecolor':'black'})
#
#plt.title("Vendegek eloszlasa evtizedenkent")
#plt.grid(True)
#plt.tight_layout()
##plt.savefig('8_graf.png')
#plt.show()