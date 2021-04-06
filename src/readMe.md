### *Tugas Kecil III IF2211 Strategi Algoritma*

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester II Tahun 2020/2021*

## Algoritma A*
Algoritma A* adalah algoritma pencarian yang dapat digunakan untuk mencari rute terpendek antara state awal dan state akhir. Algoritma A* termasuk kedalam jenis *Informed Search*.<br />
Terdapat 3 parameter yang perlu di perhitungkan dalam Algoritma A* yaitu:
- g(n) : biaya dari state awal hingga state saat ini
- h(n) : estimasi biaya dari state saat ini hingga state akhir (*heuristic value*)
- f(n) : estimasi biaya dari state awal hingga state akhir. `f(n) = g(n) + h(n)` 

## Requirement
- Windows 10
- [Python 3](https://www.python.org/downloads/)
- [JupyterLab](https://jupyter.org/install)
- [Folium](https://python-visualization.github.io/folium/installing.html)

## Executing
- Pastikan semua Requirement sudah terpenuhi, jika belum maka install terlebih dahulu
- Program dapat dijalankan dengan mengeksekusi file `run_main.bat`
- Alternatif lain, Program dapat dijalankan dengan mengeksekusi file `main.exe` pada folder bin
- File data graf tersedia di folder `test/`

## Visualization
- Instalasi Requirement Folium dan JupterLab dapat dilakukan dengan menjalankan perintah `$ pip install folium` dan `pip install jupyterlab` pada Terminal
- Untuk visualisasi peta dan hasil rute pencarian, dapat dilakukan dengan mengeksekusi file `run_visualisasi.bat`
- Program jupyer-lab akan terbuka
- Alternatif lain, visualisasi dapat dijalankan dengan membuka file `visualisasi.ipynb` pada folder `src/`
- Anda dapat mengubah file graf yang ingin digunakan dengan mengganti nilai variabel `input_file` pada cell ke-2
- Untuk mengubah simpul awal dan simpul tujuan dapat dilakukan dengan mengganti nilai variabel `input_startNode` dan `input_finalNode` pada cell ke-2
- Pastikan bahwa input yang dimasukkan valid, lalu jalankan semua cell
- Pada cell ke-4 ditampilkan daftar simpul yang tersedia pada program
- Pada cell ke-5 ditampilkan visualisasi dari peta dan graph yang dimasukan
- Pada cell ke-6 ditampilkan hasil pencarian rute
- Pada cell ke-7 ditampilkan visualisasi dari rute yang didapatkan 


## Author
- 
- 
