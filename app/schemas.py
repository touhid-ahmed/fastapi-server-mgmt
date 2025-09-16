from datetime import datetime
from pydantic import BaseModel, Field
from typing import Any, Dict



class Server(BaseModel):

    id : int
    hostname : str = Field(description="Server Hostname", example="localhost.darmstadt")
    configuration : Dict[str, Any] = Field(default_factory=dict, description="Server Configuration", example={"max_query" : 100})
    datacenter_id : int = Field(gt=0, description="id of the datacenter", example=3)
    created_at : datetime
    modified_at : datetime


class ServerCreate(BaseModel):
    hostname : str = Field(description="Server Hostname", example="localhost.darmstadt")
    configuration : Dict[str, Any] = Field(default_factory=dict, description="Server Configuration", example={"max_query" : 100})


class ServerUpdate(BaseModel):
    hostname : str = Field(description="Server Hostname", example="localhost.darmstadt")
    configuration : Dict[str, Any] = Field(default_factory=dict, description="Server Configuration", example={"max_query" : 100})
    datacenter_id : int = Field(gt=0, description="id of the datacenter", example=3)




    


