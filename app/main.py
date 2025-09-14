from fastapi import FastAPI, Depends
from app.db import get_db_conn
from app.router_servers import router as servers_router

app = FastAPI()

@app.get('/status')
def status(db = Depends(get_db_conn)):
    
    with db.cursor() as cur:
        cur.execute("SELECT 1;")
        cur.fetchone()
    return{"status" : "ok"}

app.include_router(servers_router, prefix="/servers")



