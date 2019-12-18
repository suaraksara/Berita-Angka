from requests import get
from bs4 import BeautifulSoup as bs

def bikin_sup(url):
    a = get(url)
    b = bs(a.text, 'html5lib')
    return(b)


halaman_detik = [str(i) for i in range(1, 21)]

hari = input('Mau tanggal berapa?(dua digit): \n')
bulan = input('Bulan? (dua digit): \n')
tahun = input('Tahun? (empat digit): \n')

tanggal = tahun + '/' + bulan + '/' + hari
namafile = tahun + '_' + bulan + '_' + hari

kabeh_judul = []
kabeh_link = []
for i in halaman_detik:
    indeks_cnbc = 'https://www.cnbcindonesia.com/indeks/'+ i + '?date=' + tanggal
    sup_cnbc = bikin_sup(indeks_cnbc)
    berita_cnbc = sup_cnbc.select('article')
    #judul_cnbc = sup_cnbc.select('div', class_='box_text')
    for a in berita_cnbc:
        box = a.select_one('div', class_='box_text')
        juds = box.select_one('h2')
        b = juds.get_text().strip()
        kabeh_judul.append(b)
        #print(b)
    for c in berita_cnbc:
        e = c.find('a')
        d = e['href']
        kabeh_link.append(d)
        #print(d)

def ada_angka(kalimat):
    return any(char.isdigit() for char in kalimat)

angka = [ada_angka(i) for i in kabeh_judul]

import pandas as pd

data_cnbc = pd.DataFrame({'judul': kabeh_judul,
             'tautan' : kabeh_link,
                'ada_angka': angka})

berita_dg_angka = data_cnbc.loc[data_cnbc['ada_angka'] == True]
#print(berita_dg_angka)
berita_dg_angka.to_csv(namafile+'_'+'angka_dalam_cnbc.csv')



from time import sleep

for row in berita_dg_angka.itertuples():
    print ("Judul : \n", row.judul)
    print ("Tautan : \n", row.tautan)
    sleep(1.5)