**Link :** [**klik disini**](http://20.189.113.153/)
Fauzan Hafiz Amandani - 5025241087


### Tugas Pertama NCC - Eksplorasi Docker



&#x09;Ditugas kali ini, saya akan menjelaskan secara singkat bagaimana saya Menyusun docker saya secara keseluruhan. Untuk tugas kali ini kami dibebaskan untuk memilih Bahasa/framework yang ada sehingga saya memilih menggunakan python untuk digunakan sebagai Bahasa main.py dengan menggunakan framework fastAPI. Alasan saya menggunakan fastAPI dikarenakan rekomendasi dari internet yang mengatakan bahwa fastAPI ditambah Alpine untuk python memberikan performa yang baik dengan mengambil sedikit storage. Lalu, selanjutnya mendeploy docker saya menggunakan Azure VM sebagai VPS (Link dapat diakses melalui tombol diatas).


1. #### Penjelasan endpoint /health

&#x09;Apabila kita mengakses dengan endpoint /health akan tertampil tampilan sebagai berikut

<img width="312" height="228" alt="image" src="https://github.com/user-attachments/assets/0cf864ba-48e2-4f9e-bc7c-ce555262b66e" />


&#x09;Yang juga mengembalikan 200 pada docker

<img width="918" height="249" alt="image" src="https://github.com/user-attachments/assets/faa47f3a-65f9-48fd-849d-ffa340fb540a" />


&#x09;\* untuk contoh ini diambil sebelum docker di deploy melalui VPS



#### 2\. Build dan Run Docker

&#x09;Seperti rekomendasi penggunaan multi-stage maka dapat dipisah sisi builder (persiapan) dan runner (eksekusi) pada dokumen dockerfile yang kita miliki. Dengan alasan optimasi, familiar dengan python, dan mengikuti rekomendasi internet maka saya menggunakan base image python dengan alpine. Disertai juga dengan port mapping untuk http serta restart policy. Untuk beberapa data saya menyimpannya di file .env yang didefinisikan pada file .yml



#### 3\. Deploy ke VPS

&#x09;Saya menggunakan plan termurah dari Microsoft Azure dengan menggunakan OS Ubuntu Server 22.04, lalu membuka port SSH (untuk saya dapat mengakses VM nya) dan port HTTP sehingga VMnya dapat saya akses melalui internet. Lalu saya memindahkan file docker yang sudah saya buat di WSL saya ke dalam VM yang sudah saya buat dan mengulangi cara untuk deploy docker seperti yang saya lakukan untuk mencobanya pada localhost



#### 4\. Kendala

&#x09;Pertama saya memiliki kendala dalam mencari cara untuk dapat membuka VM pada azure, lalu selanjutnya adalah beberapa kesalahan syntax dan pada beberapa saat saya tidak bisa mengakses docker yang saya buat.

