nginx -c /app/nginx.conf
mongod --fork --logpath /app/log/mongod.log
exec python /app/wsgi.py