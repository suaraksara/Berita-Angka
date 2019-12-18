#angka_tempo.py

hari = input('Mau tanggal berapa?(dua digit): \n')
bulan = input('Bulan? (dua digit): \n')
tahun = input('Tahun? (empat digit): \n')

tanggal = tahun + "/" +bulan+ "/" + hari
namafile = tahun + "_" +bulan+ "_" + hari + "_"
tempo = 'https://www.tempo.co/indeks/'

from requests import get
from bs4 import BeautifulSoup as bs

def bikin_sup(url):
    a = get(url)
    b = bs(a.text, 'html5lib')
    return(b)

sup_tempo = bikin_sup(tempo+tanggal)

seksi = sup_tempo.select('section')

judul = seksi[2].select('h2')

kabeh_judul = [i.get_text() for i in judul]

taut = [i['href'] for i in seksi[2].select('a')]

kabeh_link = taut[0::2]

def ada_angka(kalimat):
    return any(char.isdigit() for char in kalimat)

angka = [ada_angka(i) for i in kabeh_judul]

import pandas as pd

data_cnbc = pd.DataFrame({'judul': kabeh_judul,
             'tautan' : kabeh_link,
                'ada_angka': angka})

berita_dg_angka = data_cnbc.loc[data_cnbc['ada_angka'] == True]
#print(berita_dg_angka)
berita_dg_angka.to_csv(namafile+"_"+'angka_dalam_tempo.csv')



from time import sleep

for row in berita_dg_angka.itertuples():
    print ("Judul : \n", row.judul)
    print ("Tautan : \n", row.tautan)
    sleep(1.5)