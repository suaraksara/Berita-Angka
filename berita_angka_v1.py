#gabungan, sementara detik, tempo, cnbc, kompas (13 Des 2019)

from runpy import run_path as rp

media = {1: 'Kompas', 2: 'Tempo', 3:'CNBC', 4:'Detik', 5:'Republika', 6:'Antara', 7:'Okezone'}

for k,v in media.items():
    print(k, ":", v)



coblos = input('Silakan pilih nomor media:\n')

pilihan_ = media[int(coblos)]

pilihan_

if pilihan_ == "Kompas":
    rp('angka_kompas.py')
elif pilihan_ == "Detik":
    rp('angka_detik.py')
elif pilihan_ == "Tempo":
    rp('angka_tempo.py')
elif pilihan_ == "CNBC":
    rp('angka_cnbc.py')
elif pilihan_ == "Republika":
	rp('republika.py')
elif pilihan_ == "Antara":
	rp('angka_antara.py')
elif pilihan_ == "Okezone":
	rp('angka_okezone.py')
else:
    print("Urung milih, son")