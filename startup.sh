source /home/site/wwwroot/APIBACKEND/env/bin/activate

gunicorn --bind=0.0.0.0 --workers=4 src.app:app