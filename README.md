## Enterprise IS Class @Jayanusa Padang:Oct 2024
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
   
 2. Install Odoo 14:
   - Install Database:
      - docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name=dberp14 postgres:14 
   - Install Odoo:
      - docker run -p 8069:8069 --name erp14 --link dberp14:db -t odoo:14 
   - Running Odoo:
      - docker start dberp14 
      - docker start erp14
      - http://localhost:8069
   - Install PgAdmin:
      - docker run -p 5050:80 -e "PGADMIN_DEFAULT_EMAIL=jayanusa” -e "PGADMIN_DEFAULT_PASSWORD=odoo" -d dpage/pgadmin4
      - docker start <nama_container_pgadmin_anda>
      - http://localhost:5050

 3. Docker Terminal:
   - Masuk ke docker : 
      - docker exec -u root -it erp14 /bin/bash
   - Copy new module:
      - docker cp <nama_module> erp14:/mnt/extra-addons
      - docker stop erp14
      - docker start erp14
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
   
1. https://apps.odoo.com/apps/modules/14.0/om_account_accountant/
   
2. https://odoo-community.org/shop/account-reconciliation-widget-8893#attr=14598
   
3. https://apps.odoo.com/apps/modules/14.0/stock_no_negative/
    
