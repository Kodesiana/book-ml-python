# Fundamental Machine Learning menggunakan Python

## Dataset

Direktori **dataset** berisi semua dataset yang dibutuhkan dalam format CSV.
Khusus untuk dataset yang berupa gambar (Bab 16 - Klasifikasi Gambar Spesies Hewan),
dataset dapat diunduh dari https://www.kaggle.com/chetankv/dogs-cats-images.

## Menggunakan Kode pada Repositori

Pastikan Anda mengikuti petunjuk pada buku Fundamental Machine Learning menggunakan
Python agar dapat menggunakan kode pada repositori ini.

Pastikan Anda sudah memasang Visual Studio Code, Miniconda beserta *library* yang
dibutuhkan yang terdapat pada **spec** file.

## Folder pada Repositori

### Jupyter

Folder ini berisi Jupyter Notebook yang berisi kode pada buku.

### Model

Folder ini berisi model yang telah disimpan dari proses *training*.

### REST API

Folder ini berisi file Python untuk membuat server REST API.

### Web

Folder ini tiga contoh website menggunakan NodeJS, PHP, dan Python.
Anda dapat menjalankan website tersebut sama seperti petunjuk pada buku
atau dengan menjalankan perintah berikut.

NodeJS

```bash
npm install && npm run dev
```

PHP

```bash
php -S 127.0.0.1:5000 -t web/php
```

Python

```bash
conda activate ml
python web/python/app.py
```

## Lisensi

Semua kode pada repositori ini dilisensikan di bawah lisensi MIT.
