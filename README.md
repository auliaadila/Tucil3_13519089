# *Tugas Kecil III IF2211 Strategi Algoritma*

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester II Tahun 2020/2021*

## Algoritma A*
Algoritma A* adalah algoritma pencarian untuk mencari rute terpendek dari satu state ke state yang lain. Algoritma ini termasuk kedalam jenis *Informed Search*.<br />
Algoritma ini memiliki 3 elemen/fungsi penting, yaitu:
- g(n) : fungsi yang menghitung biaya real dari state awal hingga state saat ini
- h(n) : fungsi yang menghitung estimasi biaya dari state saat ini hingga node akhir (*heuristic value*)
- f(n) : fungsi yang menghitungh estimasi biaya dari state awal hingga state akhir. 
- Rumus utama dari algoritma ini adalah `f(n) = g(n) + h(n)` 

## Requirement
- [Python 3](https://www.python.org/downloads/)
- [JupyterLab](https://jupyter.org/install)
- [Folium](https://python-visualization.github.io/folium/installing.html)
- [Extension Jupyter Notebook pada VSCode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

## Executing
- Instalasi Requirement Folium dan JupterLab dapat dilakukan dengan menjalankan perintah `$ pip install folium` dan `pip install jupyterlab` pada Terminal
- Visualisasi dapat dilihat dengan membuka file `main.ipynb` pada folder `src/`
  
## Visualisasi dengan ipynb
- Akan ada 2 cell sebagai perwakilan visualisasi untuk kondisi awal (inisialisasi peta) yang juga menampilkan daftar nama simpul yang tersedia dan kondisi setelah di beri masukan simpul asal dan simpul tujuan (visualisasi peta dan path)
- Pada cell pertama, Anda dapat merubah file input pada variabel `filename` dengan file testcase yang tersedia pada `test/`, yaitu `itb.txt`, `ahmaddahlan.txt`, `alun2.txt`, `buahbatu.txt`, `bandung.txt`, `jakarta.txt`
- Pada cell kedua, Anda dapat merubah file input seperti poin sebelumnya dan juga mengubah argumen simpul asal dan simpul tujuan di fungsi aStar argumen ke-3 dan ke-4
- Pastikan masukan yang diberikan valid sesuai dengan nama file dan simpul yang tersedia
- Program dapat dijalankan (menekan tombol run pada visual studio code)


## Author
- Syarifah Aisha Geubrina Yasmin (13519089 / K02)
- Aulia Adila (13519100 / K02)
