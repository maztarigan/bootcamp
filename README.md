## Odoo Sharing 
## History : 
## 1. 3 Feb 2025 @Univ Ciputra Surabaya
## 2. 17 Oct 2025 @STMIK Jayanusa Padang

<b>Day 1:</b><br>
<b>Comparasion:</b>
   1. https://www.odoo.com/id_ID/page/compare-odoo-vs-sap
   2. https://www.odoo.com/id_ID/page/erp-comparison
   3. https://www.odoo.com/id_ID/page/editions
<br>
<b>Learn Python:<b>https://www.netacad.com/courses/programming/pcap-programming-essentials-python<br>

<br>
<b>Installation:</b>

1. Docker Installation
   - Download Docker : https://www.docker.com/
   - Install (Windows/Mac)
   - Run Docker
   
 2. Install Odoo 18:
   - Install Database:
      - docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name=dberp18 postgres:16 
   - Install Odoo:
      - docker run -p 8069:8069 --name erp18 --link dberp18:db -t odoo:18 
   - Running Odoo:
      - docker start dberp18 
      - docker start erp18
      - http://localhost:8069
   - Install PgAdmin:
      - docker run -p 5050:80 -e "PGADMIN_DEFAULT_EMAIL=bootcamp” -e "PGADMIN_DEFAULT_PASSWORD=odoo" -d dpage/pgadmin4
      - docker start <nama_container_pgadmin_anda>
      - http://localhost:5050
      - Masukkan Email : bootcamp
      - Masukkan Password: odoo
      - Di Explorer PgAdmin, klik kanan Local dan Register Server
      - Masukkan data sebagai berikut:
        <img width="913" alt="Screenshot 2025-02-05 at 15 42 00" src="https://github.com/user-attachments/assets/274bdc5a-a286-44f5-aae9-f8201202f92e" />

        <img width="700" alt="Screenshot 2025-02-05 at 15 42 10" src="https://github.com/user-attachments/assets/f5169592-32b4-4bc0-abe0-32240f1a7fa4" />


 3. Docker Terminal:
   - Masuk ke docker : 
      - docker exec -u root -it erp17 /bin/bash
   - Copy new module:
      - Download Free Addons ke folder kerja anda, di :
        - https://apps.odoo.com/apps
        - https://odoo-community.org/shop/
      - Extract Zip File Addons yang baru di download, dan copykan masing-masing folder ke docker.
      - docker cp <nama_module> erp17:/mnt/extra-addons
      - docker stop erp17
      - docker start erp17
      - Masuk ke Odoo dan pastikan sudah mengaktifkan Developer Mode (Menu Setting --> Scroll page paling bawah --> Activate Developer Mode) 
      - Masuk Modul Apps, dan klik Update Apps List
      - Maka Addons Baru anda sudah masuk ke list apps, dan siap di Activate
   - Perintah operasi pada docker:
      - Menampilkan list container pada docker dari terminal:
         -  docker container l --all 
      - Menghapus container exsisting:
         - docker rm <nama_container>
        
 4. Setting pdf report agar tampil sempurna & ada logo:
      - System Configuration -> System Parameter
      - web.base.url = http://127.0.0.1:8069 
<br>
<b>Download:<b>
   
1. https://apps.odoo.com/apps/modules/17.0/om_account_accountant/
   
2. https://odoo-community.org/shop/account-reconciliation-widget-8893#attr=14598 --> pilih versi 17
   
3. https://apps.odoo.com/apps/modules/17.0/stock_no_negative/
    
