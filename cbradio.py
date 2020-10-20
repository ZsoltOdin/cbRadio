from collections import namedtuple


def atszamol_percre(ora, perc):
    ido = ora*60 + perc
    return ido


adas = namedtuple('adas', 'Ora Perc AdasDb Nev')

adasok = []
soforok = set()

with open('cb.txt') as f:
    next(f)
    for sor in f:
        a = adas(int(sor.split(';')[0]), int(sor.split(';')[1]), int(sor.split(';')[2]), sor.strip().split(';')[3])
        adasok.append(a)

print('3. feladat: Adások száma: ', len(adasok))

for adat in adasok:
    if adat[2] == 4:
        print('4. feladat: ', adat[3])
        break

print(adasok[2])

bekert_sofor = input('Kérem adja meg a sofőrt: ')
for sofor in adasok:
    if sofor.Nev == bekert_sofor:
        print('Benne van')
        break

for adas in adasok:
    soforok.add(adas.Nev)

if bekert_sofor in soforok:
    hivas_db = 0
    for adas in adasok:
        if adas.Nev == bekert_sofor:
            hivas_db += adas.AdasDb
    print(f'{bekert_sofor} sofőrnek {hivas_db} hívása volt összesen.')
else:
    print('Nincs ilyen nevű sofőr!')

with open('cb2.txt', 'w') as w:
    w.write('Kezdes;Nev;AdasDb ')
    for adas in adasok:
        w.write(f'{atszamol_percre(adas.Ora, adas.Perc)};{adas.Nev};{adas.AdasDb} ')
