from datetime import datetime
from pydantic import BaseModel, Field
from typing import Any, Dict



class Server(BaseModel):

    id : int
    hostname : str
    configuration : Dict[str, Any]
    datacenter_id : int
    created_at : datetime
    modified_at : datetime


class ServerCreate(BaseModel):
    hostname : str
    configuration : Dict[str, Any] = Field(default_factory=dict)


class ServerUpdate(BaseModel):
    hostname : str = Field(description="Hostname of the server", example="localhost.darmstadt")
    configuration : Dict[str, Any] = Field(default_factory=dict, description="Configuration of the server", example={"max_query" : 100})
    datacenter_id : int = Field(gt=0, description="id of the datacenter", example=3)




    


