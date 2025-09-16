from fastapi import APIRouter, Depends,  HTTPException, Path, Body
from app.db import get_db_conn
from app.schemas import Server, ServerUpdate
from psycopg.types.json import Jsonb
from psycopg import errors


router = APIRouter()

@router.get("", response_model=list[Server], summary="Retrieve all servers")

def list_servers(db = Depends(get_db_conn)):
    
    with db.cursor() as cur:
        
        cur.execute(
            """
            Select id, hostname, configuration, datacenter_id, created_at, modified_at
            FROM public.server
            ORDER BY id;

            """)
        
        return cur.fetchall()
    

@router.get("/{server_id}", response_model=Server, summary="Retrieve a server by ID", status_code=200)
def get_server(server_id : int = Path(..., ge=1, description="Server ID"), db = Depends(get_db_conn)):
    
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


@router.put("/{server_id}", response_model=Server, status_code=200, summary="Update a server by ID")
def update_server(
    server_id: int= Path(..., ge=1, description="Server ID"),
    payload: ServerUpdate = Body(..., description="Server representation.",
                                 example={
                                     "hostname": "rabbitmq.local.lan",
                                    "configuration": {"max_queues": 5678},
                                    "datacenter_id": 3,
                                        },
                                    ),
                                    db = Depends(get_db_conn)):
       
       with db.cursor() as cur:
        
        cur.execute("SELECT 1 FROM public.server WHERE id = %s;", (server_id,))
        
        if cur.fetchone() is None:
            
            raise HTTPException(status_code=404, detail="server not found")

        cur.execute(

            """
            UPDATE public.server 
            SET datacenter_id = %s,
                hostname = %s,
                configuration = %s,
                modified_at = (now() AT TIME ZONE 'UTC') 
            WHERE id = %s
            RETURNING *;
            """, (payload.datacenter_id, payload.hostname, Jsonb(payload.configuration), server_id),
        )

        row =  cur.fetchone()

        if row is None:
            db.rollback()
            raise HTTPException(status_code=404, detail="server not found")


        db.commit()
        return row
    


@router.delete("/{server_id}",  summary="Delete a server by ID", status_code=200)
def delete_server(server_id : int = Path(..., ge=1, description="Server ID"), db = Depends(get_db_conn)):
    
    with db.cursor() as cur:

        try:

            cur.execute(

                """
                DELETE FROM public.server
                WHERE id = %s
                RETURNING id;
                """, (server_id,)
            )
        except errors.ForeignKeyViolation:
            db.rollback()
            raise HTTPException(
                status_code=409,
                detail="Server is linked in switch_to_server. Detach before deleting the server",
            )
        
        if cur.fetchone() is None:
            db.rollback()
            raise HTTPException(status_code=404, detail="server not found")
    
    db.commit()
    
    return {"message": f"Server {server_id} has been deleted successfully"}