#angka_okezone.py
from requests import get
from bs4 import BeautifulSoup as bs
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

def bikin_sup(url):
    a = get(url, headers=headers)
    b = bs(a.text, 'html5lib')
    return(b)


halaman_detik = [str(i*15) for i in range(0, 40)]

hari = input('Hari ini tanggal berapa?(dua digit): \n')
bulan = input('Bulan? (dua digit): \n')
tahun = input('Tahun? (dua digit): \n')

tanggal = tahun + "/" + bulan + "/" + hari + "/"
namafile = tahun + '_' + bulan + '_' + hari

kabeh_judul = []
kabeh_link = []
for i in halaman_detik:
    indeks_cnbc = "https://index.okezone.com/bydate/index/"+ tanggal + i + "/"
    sup_cnbc = bikin_sup(indeks_cnbc)
    sleep(0.7)
    berita_cnbc = sup_cnbc.find_all('h4', class_="f17")
    for a in berita_cnbc:
        b = a.find('a')
        c = a.get_text()
        d = b['href']
        kabeh_judul.append(c)
        kabeh_link.append(d)
        #print(d)

def ada_angka(kalimat):
    return any(char.isdigit() for char in kalimat)

angka = [ada_angka(i) for i in kabeh_judul]

import pandas as pd

data_cnbc = pd.DataFrame({'judul': kabeh_judul,
             'tautan' : kabeh_link,
                'ada_angka': angka})
data_cnbc = data_cnbc.drop_duplicates(subset=['judul'])
berita_dg_angka = data_cnbc.loc[data_cnbc['ada_angka'] == True]
#print(berita_dg_angka)
berita_dg_angka.to_csv(namafile+'_'+'angka_dalam_okezone.csv')




for row in berita_dg_angka.itertuples():
    print ("Judul : \n", row.judul)
    print ("Tautan : \n", row.tautan)
    sleep(1.5)