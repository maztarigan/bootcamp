## ERP Bootcamp @Jayanusa Padang:June-July 2023
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
      - docker run -p 8989:8069 --name erp14 --link dberp14:db -t odoo:14 
   - Running Odoo:
      - docker start dberp14 
      - docker start erp14
      - http://localhost:8989

 3. Docker Terminal:
   - Masuk ke docker : 
      - docker exec -u root -it erp14 /bin/bash
   - Copy new module:
      - docker cp <nama_module> erp14:/mnt/extra-addons
      - docker stop erp14
      - docker start erp14     
