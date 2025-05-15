# Laporan Proyek Machine Learning - Nino Fachrurozy

## Domain Proyek

Sepak bola adalah olahraga terpopuler di seluruh dunia. Menurut FIFA, terdapat 5 miliar penggemar sepakbola di dunia *[1]*. Perkembangan teknologi dan informasi, yang dimulai dari pencatatan statistik secara manual oleh Charles Reep pada 1950 *[2]* membuat banyaknya data sepakbola yang tersedia.

Analisis data sepakbola menjadi penting saat ini, salah satunya untuk menjaga agar suatu tim tetap kompetitif dalam aspek pertandingan maupun keuangan *[3]*. Analisis yang baik juga mampu membantu tim dalam menyusun strategi terbaik untuk mencapai kejayaan *[4]*. Sehingga penting untuk menentukan suatu formulasi untuk analisis sepakbola, salah satunya prediksi hasil pertandingan.

Oleh karena itu, bermunculan banyak keinginan pengembangan metodologi untuk memprediksi hasil akhir pertandingan sepakbola dengan melakukan analisis dari berbagai faktor *[5]*. Beberapa di antaranya seperti menggunakan pemodelan distribusi binomial dari data performa pertandingan *[6]*, studi tentang model Poisson dan korelasinya dengan skor sepakbola *[7]*, hingga prediksi hasil dengan memanfaatkan deep learning *[8]*.

## Business Understanding

Sistem dengan menggunakan faktor yang tepat dapat membuat prediksi yang akurat. Namun dalam sepakbola terdapat banyak sekali data, selain itu juga perlu mempertimbangkan data apa saja yang berpengaruh terhadap hasil akhir.

### Problem Statements

- Bagaimana cara membuat model machine learning untuk memprediksi hasil pertandingan sepakbola berdasarkan data statistik pertandingan?

### Goals

- Membuat model machine learning yang dapat memprediksi hasil pertandingan sepakbola berdasarkan data statistik pertandingan masa lalu

### Solution Statements

- Membuat model prediktif dari kumpulan statistik pertandingan sepakbola dan hasilnya
- Melakukan analisis terhadap data untuk menentukan fitur apa saja yang akan digunakan untuk membuat model
- Proses pemodelan menggunakan beberapa algoritma regresi seperti Linear Regression, Random Forest, Support Vector Regression (SVR), dan Multi Layer Perceptron (MLP). Setelah itu diukur dengan parameter mean squared error (MSE) dan hasil prediksi tiap model akan dibandingkan.

## Data Understanding

[Dataset](https://raw.githubusercontent.com/nfach98/FootballPredictor/refs/heads/main/matches.csv) yang digunakan dalam proyek ini adalah data pertandingan yang diperoleh dari website statistik sepakbola [FBref](https://fbref.com/en/) dengan metode scraping. Dataset berisi 16.340 statistik pertandingan dari 5 liga top dan 2 liga kontinental Eropa, bervariasi dengan data pertandingan paling lama berasal dari musim 2015-2016 hingga 2024-2025. Berikut daftar liga yang terdapat dalam dataset.

- Premier League (Inggris)
- La Liga (Spanyol)
- Serie A (Italia)
- Bundesliga (Jerman)
- Ligue 1 (Prancis)
- UEFA Champions League (Eropa)
- UEFA Europa League (Eropa)

Berikut penjelasan dari seluruh kolom dalam dataset tersebut yang berjumlah 53 kolom.

| Kolom | Penjelasan | Non-Null Count |  Dtype  |
|:------:|:--------------:|:-------:|:-------:|
| league | Nama liga dari suatu pertandingan | 16340 non-null | object |
| region | Wilayah asal liga | 16340 non-null | object |
| type | Tipe tingkat pertandingan, dalam dataset ini semuanya berisi Club | 16340 non-null | object |
| season | Musim digelarnya pertandingan | 16340 non-null | object |
| round | Babak pertandingan | 16340 non-null | object |
| date | Tanggal pertandingan | 16340 non-null | object |
| time | Waktu pertandingan | 16340 non-null | object |
| H_team_name | Nama tim tuan rumah | 16340 non-null | object |
| H_goals | Jumlah gol tim tuan rumah | 16340 non-null | int64  |
| A_goals | Jumlah gol tim tamu | 16340 non-null | int64  |
| A_team_name | Nama tim tamu | 16340 non-null | object |
| H_possession | Persentase penguasaan bola tim tuan rumah | 16340 non-null | int64 |
| H_passes_completed | Jumlah umpan akurat tim tuan rumah | 16340 non-null | int64 |
| H_passes_total | Total seluruh umpan tim tuan rumah | 16340 non-null | int64 |
| H_shots_on_target | Jumlah tembakan tepat sasaran tim tuan rumah | 16340 non-null | int64 |
| H_shots_total | Total seluruh tembakan tim tuan rumah | 16340 non-null | int64 |
| H_saves | Jumlah penyelamatan tim tuan rumah | 16340 non-null | int64 |
| H_yellow_cards | Jumlah kartu kuning tim tuan rumah | 16340 non-null | int64 |
| H_red_cards | Jumlah kartu merah tim tuan rumah | 16340 non-null | int64 |
| H_own_goals | Jumlah gol bunuh diri tim tuan rumah | 16340 non-null | int64 |
| H_fouls | Jumlah pelanggaran tim tuan rumah | 16340 non-null | int64 |
| H_corners | Jumlah tendangan sudut tim tuan rumah | 16340 non-null | int64 |
| H_crosses | Jumlah umpan silang tim tuan rumah | 16340 non-null | int64 |
| H_touches | Jumlah sentuhan bola tim tuan rumah | 16340 non-null | int64 |
| H_tackles | Jumlah tekel tim tuan rumah | 16340 non-null | int64 |
| H_interceptions | Jumlah potongan bola tim tuan rumah | 16340 non-null | int64 |
| H_aerials_won | Jumlah menang duel udara tim tuan rumah | 16340 non-null | int64 |
| H_clearances | Jumlah sapuan tim tuan rumah | 16340 non-null | int64 |
| H_offsides | Jumlah offside tim tuan rumah | 16340 non-null | int64 |
| H_goal_kicks | Jumlah tendangan gawang tim tuan rumah | 16340 non-null | int64 |
| H_throw_ins | Jumlah lemparan ke dalam tim tuan rumah | 16340 non-null | int64 |
| H_long_balls | Jumlah umpan panjang tim tuan rumah | 16340 non-null | int64 |
| A_possession | Persentase penguasaan bola tim tamu | 16340 non-null | int64 |
| A_passes_completed | Jumlah umpan akurat tim tamu | 16340 non-null | int64 |
| A_passes_total | Total seluruh umpan tim tamu | 16340 non-null | int64 |
| A_shots_on_target | Jumlah tembakan tepat sasaran tim tamu | 16340 non-null | int64 |
| A_shots_total | Total seluruh tembakan tim tamu | 16340 non-null | int64 |
| A_saves | Jumlah penyelamatan tim tamu | 16340 non-null | int64 |
| A_yellow_cards | Jumlah kartu kuning tim tamu | 16340 non-null | int64 |
| A_red_cards | Jumlah kartu merah tim tamu | 16340 non-null | int64 |
| A_own_goals | Jumlah gol bunuh diri tim tamu | 16340 non-null | int64 |
| A_fouls | Jumlah pelanggaran tim tamu | 16340 non-null | int64 |
| A_corners | Jumlah tendangan sudut tim tamu | 16340 non-null | int64 |
| A_crosses | Jumlah umpan silang tim tamu | 16340 non-null | int64 |
| A_touches | Jumlah sentuhan bola tim tamu | 16340 non-null | int64 |
| A_tackles | Jumlah tekel tim tamu | 16340 non-null | int64 |
| A_interceptions | Jumlah potongan bola tim tamu | 16340 non-null | int64 |
| A_aerials_won | Jumlah menang duel udara tim tamu | 16340 non-null | int64 |
| A_clearances | Jumlah sapuan tim tamu | 16340 non-null | int64 |
| A_offsides | Jumlah offside tim tamu | 16340 non-null | int64 |
| A_goal_kicks | Jumlah tendangan gawang tim tamu | 16340 non-null | int64 |
| A_throw_ins | Jumlah lemparan ke dalam tim tamu | 16340 non-null | int64 |
| A_long_balls | Jumlah umpan panjang tim tamu | 16340 non-null | int64 |

Dataset ini memiliki 44 kolom bertipe int dan sisanya 9 kolom berupa object.

### Data balance

Pemeriksaan terhadap keseimbangan nilai dalam dataset perlu dilakukan untuk memastikan model tidak dibuat dari data yang cenderung pada salah satu nilai.

![Grafik pemenang pertandingan](https://raw.githubusercontent.com/nfach98/FootballPredictor/refs/heads/main/images/graph_winner.png)

Grafik di atas menunjukkan data dalam datset berdasarkan pemenang pertandingan. Dapat dilihat hampir 50% pemenang pertandingan dalam dataset adalah tim tuan rumah (*Home*), disusul tim tamu (*Away*) dan pertandingan berakhir imbang (*Draw*).

Untuk melengkapi data, dibuat beberapa kolom baru dari kolom yang sudah ada. Berikut kolom yang akan dibuat.

| Kolom | Penjelasan |
|:------:|:------------:|
| H_shots_percentage | Persentase tembakan akurat tim tuan rumah |
| H_saves_percentage | Persentase penyelamatan tim tuan rumah |
| H_passes_percentage | Persentase umpan akurat tim tuan rumah |
| A_shots_percentage | Persentase tembakan akurat tim tamu |
| A_saves_percentage | Persentase penyelamatan tim tamu |
| A_passes_percentage | Persentase umpan akurat tim tamu |

### Missing value

Setelah melakukan pembuatan kolom-kolom baru ini terdapat beberapa error dalam data seperti data kosong atau data menjadi tak hingga (inf). Hal ini karena dibuat dari pembagian kolom yang sudah ada, dan terdapat beberapa data yang dibagi 0. Berikut adalah jumlah data tiap kolom yang memiliki data tidak valid.

| Kolom | Jumlah  |
|:------:|:-------:|
| H_shots_percentage | 12 |
| A_shots_percentage | 12 |
| H_saves_percentage | 690 |
| A_saves_percentage | 354 |

Solusi untuk mengatasi data-data ini adalah dengan mengisinya dengan nilai 0, sehingga baris yang mengandung nilai ini masih bisa digunakan dalam pembangunan model.

### Duplicate

Data duplikat perlu dihilangkan untuk mengurangi bias dari model yang dibuat. Setelah dilakukan pemeriksaan, tidak terdapat data duplikat pada dataset yang digunakan dalam proyek ini.

### Outlier

Untuk membuat model yang baik perlu juga dilakukan pemeriksaan terhadap data yang di luar lingkungan dataset, biasa disebut *outlier*. Data *outlier* bisa ditangani dengan salah satu metode yaitu IQR (Inter Quartile Range). IQR bekerja dengan mengurutkan dan membagi data menjadi 4 bagian yang ditandai oleh 3 titik yang disebut kuartil (Q). Data yang digunakan adalah yang berada di antara kuartil pertama (Q1) dan kuartil ketiga (Q3).

![Grafik boxplot outlier](https://raw.githubusercontent.com/nfach98/FootballPredictor/refs/heads/main/images/graph_outlier.png)

Grafik di atas adalah hasil pemeriksaan *outlier* pada tiap kolom. Terlihat cukup banyak data *outlier* pada dataset ini. Setelah *outlier* dihilangkan, tersisa 7.873 baris data yang semua kolomnya di dalam jangkauan Q1 dan Q3.

### Univariate analysis

Menentukan variabel mana saja yang digunakan akan sangat berpengaruh terhadap hasil dari model yang dibuat. Salah satu yang dapat dilakukan adalah memeriksa distribusi data yang dapat dibuat menggunakan visualisasi histogram.

![Grafik histogram](https://raw.githubusercontent.com/nfach98/FootballPredictor/refs/heads/main/images/graph_hist.png)

Grafik ini adalah grafik histogram untuk masing-masing data numerik. Beberapa hal yang dapat dipahami dari histogram ini:

- Sebagian besar dari diagram menunjukkan distribusi normal, yang terlihat dari diagram berbentuk lonceng (bell curve).

- Seluruh data kartu merah dan gol bunuh diri untuk kedua tim bernilai 0. Menunjukkan adanya kartu merah atau gol bunuh diri dalam dataset ini adalah *outlier*.

- Data gol tim tuan rumah (H_goals) tersebar lebih merata daripada gol tim tamu (A_goals), yang mana tim tamu lebih sering mencetak 1 gol atau tidak mencetak gol. Namun jangkauan data gol tim tamu lebih besar hingga mencapai 5 gol.

### Multivariate analysis

Memeriksa variabel yang berkorelasi kuat dengan hasil akhir pertandingan juga penting untuk menentukan variabel yang akan digunakan dalam pembangunan model. Visualisasi berupa matriks korelasi (*correlation matrix*) dapat digunakan untuk membantu dalam masalah ini. Berikut adalah *correlation matrix* dari setiap kolom.

![Grafik korelasi](https://raw.githubusercontent.com/nfach98/FootballPredictor/refs/heads/main/images/graph_correlation.png)

Dalam matriks ini korelasi paling kuat mempunyai nilai 1 atau -1 yang ditunjukkan dengan warna paling gelap, sedangkan korelasi mendekati 0 menunjukkan pengaruh kecil suatu variabel terhadap variabel lain.

- Beberapa variabel seperti penguasaan bola berkorelasi sangat kuat dengan data umpan dan sentuhan bola, menunjukkan variabel-variabel ini memiliki informasi yang sama yaitu tentang kontrol dan penguasaan bola.
- Variabel yang memiliki korelasi sangat kuat dengan jumlah gol yaitu jumlah tembakan tepat sasaran, akurasi tembakan tepat sasaran, dan akurasi penyelamatan dari tim lawan.
- Hal ini bisa dipahami karena cara untuk dapat mencetak gol adalah dengan menciptakan sebanyak mungkin tembakan, dan semakin akurat tembakan, maka akan semakin memperbesar peluang gol *[9]*. Sebaliknya tingginya akurasi penyelamatan dapat mencegah gol untuk tim lawan *[10]*, terlihat dari nilai korelasi negatif yang kuat.

Untuk proyek ini setiap variabel yang memiliki korelasi dengan variabel H_goals atau A_goals minimal 0,10 baik positif maupun negatif akan digunakan di dalam model. Variabel-variabel tersebut beserta nilai korelasinya dapat dilihat pada tabel ini.

| Kolom | Korelasi H_goals | Korelasi A_goals |
|:------:|:-------:|:-------:|
| H_shots_on_target | **0.50** | -0.06 |
| H_shots_total | **0.22** | -0.05 |
| H_crosses | **-0.16** | **0.10** |
| H_throw_ins | **-0.11** | 0.01 |
| H_shots_percentage | **0.38** | **-0.20** |
| H_passes_percentage | **0.10** | -0.00 |
| H_saves_percentage | 0.02 | **-0.56** |
| H_crosses | **-0.16** | **0.10** |
| H_aerials_won | -0.02 | **-0.11** |
| H_clearances | 0.08 | **-0.17** |
| A_shots_on_target | -0.07 | **0.54** |
| A_shots_total | -0.05 | **0.27** |
| A_crosses | 0.09 | **-0.18** |
| A_throw_ins | -0.01 | **-0.10** |
| A_shots_percentage | -0.04 | **0.45** |
| A_passes_percentage | -0.02 | **0.10** |
| A_saves_percentage | **-0.54** | 0.02 |
| A_clearances | **-0.15** | 0.07 |

## Data Preparation

Variabel-variabel terpilih dengan standar korelasi yang ditetapkan akan menjadi fitur dari model yang dibuat, sedangkan untuk target adalah variabel H_goals dan A_goals.

Agar dapat mencapai konvergensi model dengan lebih cepat, maka akan dilakukan standardisasi data terlebih dahulu. Teknik yang digunakan adalah dengan library StandarScaler. Ini menjadikan data mempunyai rata-rata (mean) mendekati atau sama dengan 0 dan standar deviasi mendekati 1.

Pembagian dataset menjadi data *training* dan data *testing* juga perlu dilakukan untuk mempertahankan sebagaian data yang akan digunakan dalam pengujian. Dalam proyek ini proporsi data *training* dan *testing* adalah 90:10. Hasilnya, sebanyak 7.085 baris sebagai data *training* dan sisanya 788 baris sebagai data *testing*.

## Modeling

### Linear Regression

Metode ini adalah metode yang digunakan untuk menemukan hubungan antara nilai dependen dengan satu atau banyak nilai independen lainnya *[11]*. Dapat digunakan untuk memprediksi nilai dependen berdasarkan kumpulan nilai lain. Metode ini dipilih karena merupakan algoritma paling sederhana untuk regresi *[12]*.

**Kelebihan:**

- Metode regresi yang sederhana dan mudah diimplementasikan
- Efisien karena hanya butuh daya komputasi yang lebih rendah daripada model-model yang lebih kompleks
- Akurasi tinggi jika digunakan untuk data yang benar-benar linear

**Kekurangan:**

- Tidak cocok untuk data yang bersifat non-linear
- Sensitif terhadap data *outlier*
- Kesulitan dalam menangani data berdimensi tinggi

### Random Forest

Random forest termasuk dalam algoritma ensemble learning, yang berarti menggabungkan prediksi dari banyak model dengan tujuan prediksi yang dihasilkan lebih baik dari model tunggal. Metode ini bekerja dengan membuat banyak *decision tree* lalu menggabungkan hasil-hasil prediksinya dengan menghitung rata-rata tiap prediksi *[13]*.

**Kelebihan:**

- Akurasi lebih tinggi karena menggabungkan banyak hasil dari *decision tree*
- Cocok untuk dataset besar
- Mampu mengurangi *overfitting* dengan menggunakan rata-rata hasil banyak model

**Kekurangan:**

- Sumber daya yang dibutuhkan besar karena harus melatih banyak model
- Kurang mudah untuk dipahami seperti model tunggal
- Sensitif terhadap data *noise*, terutama jika memiliki variasi data yang besar

### Support Vector Regression (SVR)

SVR adalah algoritma regresi yang didasarkan pada Support Vector Machines (SVM). Cara kerjanya mirip dengan SVM, yaitu mencari *hyperplane* paling optimal dalam suatu dimensi data.

Yang membedakan pada algoritma regresi *hyperplane* ini adalah generalisasi dari data-data yang ada, sedangkan pada SVM *hyperplane* ini adalah pemisah antar kelas. Selain itu dalam SVR terdapat *epsilon-insensitive loss function* yang akan mengabaikan *error* selama dalam batas tertentu *[14]*.

**Kelebihan:**

- Efisien dalam ruang berdimensi tinggi, sehingga cocok untuk data dengan fitur banyak dan kompleks
- Adanya *epsilon-insensitive loss function* membuat lebih tahan terhadap *outlier*
- Fleksibilitas yang dapat diatur dengan fungsi kernel

**Kekurangan:**

- Butuh daya komputasi besar
- Sensitif terhadap *hyperparameter*

### Multi-Layer Perceptron (MLP)

Jaringan saraf tiruan yang terdiri dari beberapa *layer* (lapisan) neuron, seperti *layer* input, *hidden layer*, dan *layer* output. Setiap neuron dalam *layer* yang berdekatan terhubung dengan suatu nilai bobot.

Dalam proses pelatihan MLP menggunakan teknik *feedforward propagation* dan *backpropagation*. Dalam proses *feedforward propagation* data akan diproses dari *layer* ke *layer*. Setiap *layer* memiliki fungsi aktivasi yang memproses input sebelum diteruskan ke *layer* berikutnya.

Sedangkan proses *backpropagation* menyesuaikan bobot pada koneksi secara iteratif yang bertujuan untuk meminimalkan *error* *[15]*.

**Kelebihan:**

- Mampu menangkap hubungan kompleks pada data
- Fleksibel karena arsitektur model dapat diatur, seperti jumlah *layer*, jumlah neuron, maupun fungsi aktivasi
- Cocok untuk data berdimensi tinggi karena kompleksitas algoritmanya

**Kekurangan:**

- Butuh daya komputasi besar
- Rawan mengakibatkan *overfitting* jika arsitektur tidak disusun sesuai konteks
- Butuh data yang banyak dan dalam jumlah besar

## Evaluation

Metrik *error* yang digunakan dalam perbandingan model-model yang sudah dilatih adalah root mean squared error (RMSE). Cara kerjanya dengan menghitung selisih kuadrat setiap data, lalu menghitung rata-rata dari semua selisih kuadrat. Setelah itu RMSE akan didapat dari hasil kuadrat nilai rata-rata sebelumnya *[16]*. Formula RMSE dapat dinotasikan dengan persamaan berikut.

![RMSE formula](https://raw.githubusercontent.com/nfach98/FootballPredictor/refs/heads/main/images/RMSE_formula.png)

RMSE dipilih karena sesuai untuk pengukuran *error* pada data dengan distribusi normal *[17]*. Seperti yang terlihat pada grafik histogram, banyak variabel dalam dataset yang digunakan terdistribusi secara normal. Selain itu dengan mengkuadratkan selisih RMSE dapat menunjukkan *error* besar lebih baik. RMSE juga mudah dipahami karena memiliki satuan yang sama dengan variabel target. Besar RMSE mewakili berapa selisih rata-rata hasil prediksi dengan data sesungguhnya.

Setelah proses pelatihan model selesai, dilakukan penghitungan RMSE untuk tiap model. Berikut adalah hasilnya.

| Model | RMSE train | RMSE test |
|:------:|:-------:|:-------:|
| Linear Regression | 0.591 | 0.584 |
| Random Forest | 0.23 | 0.372 |
| SVR | 0.343 | 0.345 |
| MLP Regressor | 0.33 | 0.355 |

![Grafik error](https://raw.githubusercontent.com/nfach98/FootballPredictor/refs/heads/main/images/graph_error.png)

Dari hasil pengukuran RMSE terlihat bahwa model SVR adalah yang memiliki error test terkecil dan tidak jauh berbeda dengan error dengan dataset training. Sedangkan model Linear Regression memiliki error yang relatif jauh lebih besar dibandingkan model lainnya. Model Random Forest memiliki error pada data training yang paling kecil, namun berbeda jauh ketika diuji dengan data testing.

Pengujian juga dilakukan dengan memprediksi 20 sampel data testing menggunakan keempat model. Hasil prediksi berupa 2 nilai akan dibulatkan ke bilangan terdekat sehingga menjadi skor. Berikut adalah hasilnya beserta perbandingan dengan data sesungguhnya.

| y_true | LR | RF | SVR | MLP |
|:------:|:-------:|:-------:|:-------:|:-------:|
| **1-0** |1.07,0.63 **(1-1)**|1.11,0.07 **(1-0)**|1.10,0.00 **(1-0)**|1.16,0.00 **(1-0)**|
| **1-1** |0.8,1.03 **(1-1)**|0.28,1.19 **(0-1)**|0.04,1.06 **(0-1)**|0.07,1.04 **(0-1)**|
| **1-1** |1.77,1.81 **(2-2)**|1.18,1.31 **(1-1)**|1.07,1.17 **(1-1)**|1.06,1.17 **(1-1)**|
| **3-1** |2.19,1.10 **(2-1)**|2.95,1.47 **(3-1)**|2.96,1.11 **(3-1)**|2.97,1.05 **(3-1)**|
| **2-2** |1.00,1.89 **(1-2)**|1.08,2.02 **(1-2)**|1.10,2.10 **(1-2)**|1.22,2.20 **(1-2)**|
| **3-1** |1.8,1.36 **(2-1)**|2.14,1.07 **(2-1)**|2.08,1.08 **(2-1)**|2.14,1.05 **(2-1)**|
| **2-0** |2.35,-0.68 **(2--1)**|2.4,0.05 **(2-0)**|2.02,0.03 **(2-0)**|2.27,-0.06 **(2-0)**|
| **0-2** |0.28,1.57 **(0-2)**|0.24,2.08 **(0-2)**|0.1,2.06 **(0-2)**|0.36, 2.02 **(0-2)**|
| **0-1** |0.69,-0.37 **(1-0)**|0.19,0.04 **(0-0)**|0.11,0.06 **(0-0)**|0.44,0.07 **(0-0)**|
| **2-2** |1.72,2.26 **(2-2)**|2.28,2.03 **(2-2)**|2.0,2.02 **(2-2)**|2.24,1.93 **(2-2)**|
| **0-2** |-0.14,2.02 **(0-2)**|0.19,2.12 **(0-2)**|0.09,1.99 **(0-2)**|0.13,2.02 **(0-2)**|
| **1-1** |0.88,1.47 **(1-1)**|1.19,1.26 **(1-1)**|1.08,1.07 **(1-1)**|1.37,1.16 **(1-1)**|
| **1-0** |1.21,-0.16 **(1-0)**|1.11,0.05 **(1-0)**|1.09,0.08 **(1-0)**|1.25,0.1 **(1-0)**|
| **0-2** |0.38,2.15 **(0-2)**|0.11,2.48 **(0-2)**|0.07,2.15 **(0-2)**|0.11,2.3 **(0-2)**|
| **1-2** |0.9,2.49 **(1-2)**|1.2,2.22 **(1-2)**|1.01,2.1 **(1-2)**|1.0,2.07 **(1-2)**|
| **2-0** |2.06,0.63 **(2-1)**|2.16,0.09 **(2-0)**|2.06,0.11 **(2-0)**|2.17,-0.03 **(2-0)**|
| **0-1** |0.31,0.99 **(0-1)**|0.09,1.05 **(0-1)**|0.1,1.07 **(0-1)**|0.38,1.05 **(0-1)**|
| **0-1** |0.19,1.52 **(0-2)**|0.04,1.1 **(0-1)**|0.05,1.06 **(0-1)**|0.03,1.27 **(0-1)**|
| **0-1** |0.79,1.16 **(1-1)**|0.41,1.25 **(0-1)**|0.07,1.07 **(0-1)**|0.17,1.14 **(0-1)**|
| **2-3** |1.58,2.63 **(2-3)**|1.96,3.2 **(2-3)**|2.05,3.08 **(2-3)**|2.25,3.03 **(2-3)**|

Setelah diuji dan dibandingkan, akan dihitung berapa jumlah prediksi skor yang tepat dari setiap model dan persentase akurasi dari pengujian 20 sampel di atas. Berikut adalah jumlah prediksi benar dari masing-masing model.

| Model | Jumlah prediksi benar | Akurasi (dari 20 sampel) |
|:------:|:-------:|:-------:|
| Linear Regression | 10 | 50% |
| Random Forest | 16 | 80% |
| SVR | 16 | 80% |
| MLP Regressor | 16 | 80% |

Hasil ini menunjukkan performa model Linear Regression yang jauh di bawah model lainnya dengan hanya 10 dari 20 prediksi yang tepat. Sedangkan 3 model lain bersaing dengan akurasi yang sama yaitu 80%. Jika mempertimbangkan jumlah error, model Random Forest memiliki performa yang jauh berbeda saat training dan testing dengan selisih 0,14. Model MLP Regressor terlihat lebih baik dengan perbedaan error training dan testing yang hanya 0,025. Namun SVR jauh lebih baik dengan perbedaan error yang sangat kecil pada 2 proses itu.

Dengan memiliki RMSE terkecil, performa yang hampir tidak berbeda ketika proses training dan testing, serta kemampuan memprediksi 80% skor secara tepat, dapat ditarik kesimpulan model SVR adalah model terbaik dalam proyek ini.

## Referensi

1. [The football landscape](https://publications.fifa.com/en/vision-report-2021/the-football-landscape/)
2. [Charles Reep (1904-2002): pioneer of notational and performance analysis in football](https://doi.org/10.1080/026404102320675684)
3. [A survey of organizational structure and operational practices of elite youth football academies and national federations from around the world: A performance and medical perspective](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2022.1031721/full)
4. [Sports analytics: a guide for coaches, managers, and other decision makers](https://www.degruyterbrill.com/document/doi/10.7312/alam20520-011/html)
5. [Predicting Soccer Matches After Unconscious and Conscious Thought as a Function of Expertise](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2009.02451.x)
6. [Skill and Chance in Ball Games](https://academic.oup.com/jrsssa/article/134/4/623/7104572)
7. [Modelling association football scores](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9574.1982.tb00782.x)
8. [Data-driven prediction of soccer outcomes using enhanced machine and deep learning techniques](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-024-01008-2)
9. [Regional Analysis of the Shots in the Football Matches Played in the 2018 FIFA World Cup and Their Effect on Success](https://pjmhsonline.com/2021/feb/646.pdf)
10. [Factors Associated with Match Result and Number of Goals Scored and Conceded in the English Premier League](https://www.researchgate.net/publication/359293105_Factors_Associated_with_Match_Result_and_Number_of_Goals_Scored_and_Conceded_in_the_English_Premier_League)
11. [Linear Regression](https://link.springer.com/referenceworkentry/10.1007/978-3-319-31816-5_478-1)
12. [Simple Linear Regression](https://link.springer.com/chapter/10.1007/978-3-031-21480-6_4)
13. [The random forest algorithm for statistical learning](https://journals.sagepub.com/doi/pdf/10.1177/1536867X20909688)
14. [Support Vector Machines and Support Vector Regression](https://link.springer.com/chapter/10.1007/978-3-030-89010-0_9)
15. [Multilayer Perceptrons in Machine Learning: A Comprehensive Guide](https://www.datacamp.com/tutorial/multilayer-perceptrons-in-machine-learning)
16. [Root Mean Square Error (RMSE)](https://statisticsbyjim.com/regression/root-mean-square-error-rmse/)
17. [Root-mean-square error (RMSE) or mean absolute error (MAE): when to use them or not](https://gmd.copernicus.org/articles/15/5481/2022/)
