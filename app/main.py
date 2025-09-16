from fastapi import FastAPI, Depends
from app.db import get_db_conn
from app.router_servers import router as servers_router
from app.router_datacenters import router as datacenter_router


app = FastAPI(

    title="Server Management API",
    version="1.0",
    description="Python web service that provides a RESTful API for managing servers",
)

@app.get('/status', summary="Status Check", tags=["Status"], status_code=200)
def status(db = Depends(get_db_conn)):
    
    with db.cursor() as cur:
        cur.execute("SELECT 1;")
        cur.fetchone()
    return{"status" : "ok"}

app.include_router(servers_router, prefix="/servers", tags=["Servers"])
app.include_router(datacenter_router, prefix="/datacenters", tags=["Datacenters"])



