
# GradeWise - Prediksi Kelulusan

Aplikasi prediksi kelulusan berbasis Machine Learning menggunakan algoritma Decision Tree.

## Deskripsi
GradeWise merupakan aplikasi berbasis web yang digunakan untuk memprediksi status kelulusan berdasarkan data akademik. Pengguna dapat memasukkan nilai semester, waktu belajar, jumlah kegagalan mata pelajaran, dan jumlah ketidakhadiran.

## Tujuan
Menerapkan algoritma Machine Learning untuk melakukan klasifikasi prediksi kelulusan berdasarkan data akademik.

## Algoritma
Algoritma yang digunakan adalah Decision Tree Classifier dari Scikit-learn.

## Fitur
- Input nilai semester 1 dan 2.
- Input waktu belajar.
- Input jumlah kegagalan mata pelajaran.
- Input jumlah ketidakhadiran.
- Menampilkan hasil prediksi kelulusan.

## Teknologi
- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML dan CSS

## Dataset
Dataset menggunakan Student Performance dari UCI Machine Learning Repository.

## Struktur Project
```text
prediksi-kelulusan/
├── templates/
│   └── index.html
├── app.py
├── model_kelulusan.pkl
├── requirements.txt
└── README.md
```

## Cara Menjalankan
1. Clone repository.
2. Install library:

```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:

```bash
python app.py
```

4. Buka browser:

```text
http://127.0.0.1:5000
```

## Pengembang
Nama: Rizki Pratama

Project Ujian Tengah Semester Machine Learning.
