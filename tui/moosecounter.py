class pole:
    stany = {0: "brak pionka", 1: "pionek bialy", 2: "pionek czarny"}
    stan = None

    def pojawil_sie_bialy_pionek(self):
        stan = 1

    def pojawil_sie_czarny_pionek(self):
        stan = 2

    def pionek_opuscil_pole(self):
        stan = 0

szachownica = [8]
for wiersz in range(0, 7):
    szachownica[wiersz] = [8]
    for kolumna in range(0, 7):
        szachownica[wiersz][kolumna] = pole

a = raw_input("Ile masz lat ?")
info1 = "sprzedac piwo"
info2 = "nie sprzedawac piwa"

a = int(a)

if (a > 18):
    print(info1)
else:
    print(info2)
#c = raw_input("podaj nazwe imienia dziadka")
#print(b + " siedzi obok "+ a + " i " +b+ " sie jara bo " +a + " ma niezle cycki")