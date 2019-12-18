from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

hari = input('Tanggal? (dua digit): \n')
bulan = input('Bulan? (dua digit): \n')
tahun = input('Tahun? (empat digit): \n')

x = tahun + "-" + bulan + "-" + hari   #input('Masukkan tanggal dalam format tttt/bb/hh, \n misal. 12 Agustus 2018 ditulis 2018-08-12 : \n \n')
namafile = tahun + "_" + bulan + "_" + hari +"_"
halaman_kompas = [str(i) for i in range(1, 21)]

def ada_angka(kalimat):
    return any(char.isdigit() for char in kalimat)

kabeh_sup_kompas = []
kabeh_judul = []
kabeh_link = []
for i in halaman_kompas:
    indeks_lengkap = 'https://news.kompas.com/search/'+ x + '/' + i
    a = get(indeks_lengkap, headers = headers)
    sup_kompas = bs(a.text, 'html5lib')
    kabeh_sup_kompas.append(sup_kompas)

    for i in sup_kompas.select('.article__link'):
        a = i.get_text()
        kabeh_judul.append(a)
    for i in sup_kompas.select('.article__link'):
        b = i['href']
        kabeh_link.append(b)
    sleep(0.5)


angka = [ada_angka(i) for i in kabeh_judul]

data_kompas = pd.DataFrame({'judul': kabeh_judul,
             'tautan' : kabeh_link,
                'ada_angka': angka})


berita_dg_angka = data_kompas.loc[data_kompas['ada_angka'] == True]
print(berita_dg_angka)
berita_dg_angka.to_csv(namafile+'angka_dalam_kompas.csv')


for row in berita_dg_angka.itertuples():
    print ("Judul : \n \n", row.judul)
    print ("Tautan : \n \n", row.tautan)
    sleep(2)
