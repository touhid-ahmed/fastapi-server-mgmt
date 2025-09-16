# fastapi-server-mgmt
Repository for a Python web service that provides a RESTful API for managing servers

## Project Structure

```
fastapi-server-mgmt/
├─ app/
│  ├─ __init__.py
│  ├─ main.py                   -> runs the FastAPI app
│  ├─ config.py                 -> loads .env and exposes DATABASE_URL
│  ├─ db.py                     -> psycopg connection helper and Exposes FastAPI dependency
│  ├─ schemas.py                -> Pydantic models for requests/responses
│  ├─ routers_servers.py        -> API endpoints for managing server
│  └─ routers_datacenters.py    -> API endpoint for creating server in a datacenter
├─ sql/
│  ├─ schema.sql
│  └─ sample_data.sql
├─ .env.example
├─ requirements.txt
├─ README.md
└─ .gitignore
```

## Prerequisites
- Python 3.10+
- PostgreSQL 13+ running locally (default port 5432)

## Setup (Linux/Windows PowerShell)

### 1) Create & activate a Virtual Environment
```bash
python -m venv .venv
# Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 2) Install the dependencies
```
pip install -r requirements.txt
```

### 3) Configure database URL

- Create a .env in the repo root (the app loads this automatically):

```bash
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/test_db
```
### 4) Create database & load schema + sample data

- Make sure that postgres is installed and then Start Postgres
```
psql
```
- Create Test DB
```
createdb test_db
```
- Load Schema and test data
```
psql -d test_db -f sql/schema.sql
psql -d test_db -f sql/sample_data.sql
```
### 5) Run the API Service
```
uvicorn app.main:app --reload
```
#### Open in browser:

- Swagger UI:
```bash
http://127.0.0.1:8000/docs
```
- Status check:
```bash
http://127.0.0.1:8000/status
```
### 6) Endpoints

| Method | Endpoint                                | Description                                   |
|--------|-----------------------------------------|-----------------------------------------------|
| GET    | /status                                 | Status check to verify the service is running |
| GET    | /servers                                | Retrieve all servers from the database        |
| GET    | /servers/{id}                           | Retrieve a single server by its ID.           |
| POST   | /datacenters/{datacenter_id}/servers    | Add a new server to a datacenter              |
| PUT    | /servers/{id}                           | Updating a server                             |
| DELETE | /servers/{id}                           | Deleting a server by its ID                   |


### 7) Notes

- DB driver: psycopg with raw SQL (no ORM).

- Each request uses a fresh connection (FastAPI dependency) and closes it safely.

- JSON field configuration is stored as jsonb.