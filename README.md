# Adatvizualizációs műhely beadandó
*Molnár Adrián (Neptun kód: LWPJBS)*

### Beadandó célja:
#### Adatvizualizációs eszköz önálló használatának elsajátítátsa

### Választott eszközök:
  - **Python 3.7** 
    - *pandas könyvtár:* Nagy méretű fájlok kezelésére alkalmas
    - *matplotlib könyvtár:* Adatvizualizációs eszközökkel rendelkezik
  - **VisualStudio fejlesztői környezet**
    - VisualStudioval egyszerűen inportálhatóak a beadandóhoz szükséges könyvtárak. Az elkészült kód futtatására is alkalmas
 
### Adathalmaz:
  - KSH weboldaláról letöltött, magyarországi turizmussal kapcsolatos adatok

### Megvalósítás:

  **Első lépésben az adathalmazt python szabványoknak megfelőlre alakítottam (ékezetek eltávolítás). A beolvasás, azonosítás, új adatok     képzése a "pandas" könyvtár segítségével történt.**
  
  **A diagramok létrehozásához a matplotlib könyvtár pyplot és numpy gyűjteményeit használtam. A diagramok külalakjának testreszabása a     pyplot beépített funkcióival történt, úgy mint: vonalstílus, vonalszín, háttérstílus, alapstílus, oszlopdiagramok színe, szélessége,     több diagramtípus egy koordinátarendszeren való megjelenítése. A program futtatásakor a diagramok png formátumú fényképeit               automatikusan   a gyökérkönyvtárba generálja a "plt.savefig('1_graf.png')" sor.**
  
  **Az alap adathalmazhoz hozzáfűzött oszlopokat is készít a program a pandas könyvát segítségével, amit a memóriban tárol. A program       lefutása után az alap adathalmaz nem változik meg. Ezekből az általunk készített adatokból olyan vizualizációkat készíthetünk,           amelyekből egyszerűbben vonhatóak le a következtetések.**
      
### Könyvtárstruktúra:
  - **PythonApplication1.py:** python forráskódot tartalmazó futtatható forrsáfájl. A külömböző diagramok megjelenítéséhez a "#" komment      jelek eltávolítása szükséges.
  - **.png fotók:** kapott diagramok png képformátumban.
  - **turizmus.xls:** adathalmaz

### Fejlesztési lehetőségek:
  - **Menüredszer kialakítása**
  - **Diagramok külalkjának megformázása a felhasználástól függően**
  - **Különböző kimutatásokank megfelelő adatok készítése az alap adathalmazból (pandas könyvtár)**
  - **Az eredmények összevetése az évenkénti gazdasági növekedés/csökkenés adataival**
