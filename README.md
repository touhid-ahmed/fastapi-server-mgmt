# fastapi-server-mgmt
Repository for a Python web service that provides a RESTful API for managing servers

## Instructions for Running the API Service

- Create Test DB
```
createdb test_db
```
- Load Schema
```
psql -d test_db -f sql/schema.sql
psql -d test_db -f sql/sample_data.sql
```
- Start the API Service
```
uvicorn app.main:app --reload
```
