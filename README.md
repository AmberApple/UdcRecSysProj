# UdcRecSysProj
Программа для работы семантического рекомендательного сервиса присвоения кода универсальной десятичной классификации (УДК) математическим статьям на русском языке

check MASTER branch

Required: docker && docker compose V2

# docker_dev startup
docker-compose -f docker-compose.yml up -d --build

docker exec -it udc_dev bash


python manage.py flush

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py collectstatic

python manage.py loaddata udc_rec_sys/fixtures/article_statuses.json

python manage.py loaddata udc_rec_sys/fixtures/resource_download_statuses.json

python manage.py loaddata udc_rec_sys/fixtures/resource_downloads.json

python manage.py loaddata udc_rec_sys/fixtures/udc_table.json

python manage.py loaddata udc_rec_sys/fixtures/ontology_table.json
