# secure_chat

run

```
docker-compose up -d --build
```

for create migrations 
```
docker-compose exec backend bash
cd /code/app

alembic revision -m "create account table"
alembic revision --autogenerate 
```
for run migrations 
```
alembic upgrade head
```

