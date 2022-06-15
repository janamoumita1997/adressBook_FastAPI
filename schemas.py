from pydantic import BaseModel

class Item(BaseModel):
    location:str
    longitude:float
    latitude:float
 