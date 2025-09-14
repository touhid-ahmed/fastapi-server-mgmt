from fastapi import APIRouter, Depends,  HTTPException
from app.db import get_db_conn
from app.schemas import Server
from typing import Optional


router = APIRouter()

@router.get("", response_model=list[Server])

def list_servers(db = Depends(get_db_conn)):
    
    with db.cursor() as cur:
        
        cur.execute(
            """
            Select id, hostname, configuration, datacenter_id, created_at, modified_at
            FROM public.server
            ORDER BY id;

            """)
        
        return cur.fetchall()
    

@router.get("/{server_id}", response_model=Server)
def get_server(server_id : int, db = Depends(get_db_conn)):
    
    with db.cursor() as cur:

        cur.execute(

            """
            Select id, hostname, configuration, datacenter_id, created_at, modified_at
            FROM public.server
            WHERE id = %s;
            """, (server_id,)
        )

        row =  cur.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="server not found")
    
    return row