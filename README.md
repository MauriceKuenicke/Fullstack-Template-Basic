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




# FAQs

**How can I run alembic migrations while the containers are running?**
Change the DB_HOST in the environment variables to `localhost`.
