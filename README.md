# Self-Contained Basic Fullstack Template



## Backend Setup
```
cd backend
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Frontend Setup
```
cd frontend
npm install
```


## Run Application In Dev-Mode

```
docker compose -f docker-compose.dev.yaml up --build
```

Services are by default accessible at:

| Service         | Host URL                   |
|-----------------|----------------------------|
| Frontend        | http://localhost:5173/     |
| Backend Swagger | http://localhost:8000/docs |
| Backend         | http://localhost:8000      |
| Redis Insight   | http://localhost:5540/     |



## Redis Insight
Connect the internal Redis DB using `redis://default@redis:6379`.


# FAQs

**How can I run alembic migrations while the containers are running?**
Change the DB_HOST in the environment variables to `localhost`.
