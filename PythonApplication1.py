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

Ev_indexes = np.arange(len(Ev))
def_width = 0.4

plt.figure(figsize=(10,4))
plt.xlabel('Ev')
plt.title('Vendegelyszakak/Vendegek/Ev')
plt.bar(Ev_indexes-def_width/2,Vendegelyszakak, width = def_width, label = 'Vendegelyszakak')
plt.bar(Ev_indexes+def_width/2,Vendeg, width = def_width, label = 'Vendeg')
plt.legend()
plt.xticks(ticks = Ev_indexes, labels = Ev, rotation = 90)
plt.grid(True)
plt.tight_layout()
plt.savefig('5_graf.png')
plt.show()