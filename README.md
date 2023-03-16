# UdcRecSysProj
Программа для работы семантического рекомендательного сервиса присвоения кода универсальной десятичной классификации (УДК) математическим статьям на русском языке


Required: docker && docker compose V2

# docker_dev startup
Для сборки и поднятия контейнера:  
docker-compose -f docker-compose.yml up -d --build

Для наполнения БД в первый запуск:  
1) docker exec -it udc_dev tar -C ./udc_rec_sys/fixtures -xzvf ./media/service_data/urs_fixtures.tar.gz  
2) docker exec -it udc_dev python manage.py loaddata udc_rec_sys/fixtures/article_statuses.json  
3) docker exec -it udc_dev python manage.py loaddata udc_rec_sys/fixtures/resource_download_statuses.json  
4) docker exec -it udc_dev python manage.py loaddata udc_rec_sys/fixtures/resource_downloads.json  
5) docker exec -it udc_dev python manage.py loaddata udc_rec_sys/fixtures/udc_table.json  
6) docker exec -it udc_dev python manage.py loaddata udc_rec_sys/fixtures/ontology_table.json  
7) docker exec -it udc_dev python manage.py createsuperuser




