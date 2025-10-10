from pydantic import BaseModel

class VM(BaseModel):
    name : str
    state : str 
    memory_mb : int

