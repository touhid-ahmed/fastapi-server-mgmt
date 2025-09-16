from fastapi import APIRouter, Depends,  HTTPException, Path, Body
from app.db import get_db_conn
from app.schemas import Server, ServerCreate
from typing import Optional
from psycopg.types.json import Jsonb


router = APIRouter()

@router.post("/{datacenter_id}/servers", response_model=Server, status_code=201)

def create_server(datacenter_id: int= Path(..., ge=1, description="Datacenter ID"),
                  payload: ServerCreate = Body(..., description="Server object",
                                               example={
                                                   "hostname": "rabbitmq.local.lan",
                                                    "configuration": {"max_queues": 1234},
                                                    },
                                            ),
                  db = Depends(get_db_conn)):
    

    
    
    with db.cursor() as cur:

        cur.execute("SELECT 1 FROM public.datacenter WHERE id = %s;", (datacenter_id,))
        
        if cur.fetchone() is None:
            
            raise HTTPException(status_code=404, detail="invalid datacenter id")

        cur.execute(

            """
            INSERT INTO public.server (hostname, configuration, datacenter_id)
            VALUES (%s, %s, %s)
            RETURNING id, hostname, configuration, datacenter_id, created_at, modified_at;
            """, (payload.hostname, Jsonb(payload.configuration), datacenter_id),
        )

        row =  cur.fetchone()
        db.commit()
        return row
    
