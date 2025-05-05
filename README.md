# Computer Vision Project Progress Report (25%)

**Project Name**: Pendeteksi Jenis Motor (Motorcycle Type Detection)  
**Student Name**: Bethania Simangunsong  
**Course/Institution**: Computer Vision/Politeknik Caltex Riau  

## Latar Belakang**
- Computer vision berkembang pesat sebagai bagian dari otomatisasi modern.
- Salah satu penerapannya adalah dalam identifikasi kendaraan bermotor.
- Sistem ini dirancang untuk mengenali jenis motor berdasarkan citra visual guna mendukung efisiensi di bidang pengawasan, manajemen kendaraan, dan analisis lalu lintas.

**Perumusan Masalah**:
Bagaimana merancang dan membangun sistem berbasis YOLOv8 yang dapat mengidentifikasi jenis motor dari gambar atau video dengan klasifikasi yang akurat dan efisien?

## Batasan Masalah
- Jenis motor yang dikenali:
    a) Motor Bebek
    b) Motor Matic
    c) Motor Sport
    d) Motor Trail

- Input berupa gambar sisi samping motor
- Dataset berjumlah ±160 gambar per kategori di Roboflow
- Sistem dikembangkan menggunakan Python dan YOLOv8
  
## Tujuan
- Mendeteksi dan mengklasifikasikan jenis motor
- Menghasilkan hasil klasifikasi otomatis dengan akurasi tinggi

## Manfaat
- Mendukung sistem pengawasan dan manajemen kendaraan

## Target Sistem
- Mendeteksi objek motor dari citra atau video
- Mengklasifikasikan motor ke 4 jenis: Bebek, Matic, Sport, Trail
- Mencapai akurasi klasifikasi ≥ 80%
- Antarmuka sederhana untuk input dan output hasil
- Menggunakan dataset Roboflow (~160 gambar per label)

## Tools & Teknologi
- Bahasa Pemrograman: Python
- Object Detection: YOLOv8
- Dataset: Roboflow (4 label, ~160 image/label)
