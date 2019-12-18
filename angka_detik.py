#Skrip alfa

from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd

hari = input('Tanggal? (dua digit): \n')
bulan = input('Bulan? (dua digit): \n')
tahun = input('Tahun? (empat digit): \n')
x = bulan+'/'+hari+'/'+tahun

halaman_detik = [str(i) for i in range(1, 21)]

def ada_angka(kalimat):
    return any(char.isdigit() for char in kalimat)

#https://news.detik.com/indeks?date=12%2F10%2F2019
kabeh_sup_detik = []
kabeh_judul = []
kabeh_link = []
for i in halaman_detik:
    indeks_lengkap = 'https://news.detik.com/indeks/'+ i +'?date='+ x
    #print(indeks_lengkap)
    a = get(indeks_lengkap)
    sup_a = bs(a.text, 'html5lib')
    kabeh_sup_detik.append(sup_a)

    for i in sup_a.select('h3', class_="media-title"):
        a = i.get_text()
        #b = a.get_text()
        kabeh_judul.append(a)
    for i in sup_a.select('h3', class_="media-title"):
        a = i.find('a')
        b = a['href']
        kabeh_link.append(b)


#print(len(kabeh_link))
#print(len(kabeh_judul))
angka = [ada_angka(i) for i in kabeh_judul]
#print(len(angka))
data_detik = pd.DataFrame({'judul': kabeh_judul,
             'tautan' : kabeh_link,
                'ada_angka': angka})


berita_dg_angka = data_detik.loc[data_detik['ada_angka'] == True]
#print(berita_dg_angka)
identitas = x.replace('/', '_')
berita_dg_angka.to_csv(identitas+ '_' +'angka_dalam_detik.csv')

from time import sleep

for row in berita_dg_angka.itertuples():
    print ("Judul : \n", row.judul)
    print ("Tautan : \n", row.tautan)
    sleep(1.5)
