from datetime import datetime
from pydantic import BaseModel
from typing import Any, Dict



class Server(BaseModel):

    id : int
    hostname : str
    configuration : Dict[str, Any]
    datacenter_id : int
    created_at : datetime
    modified_at : datetime

    


