from pydantic import BaseModel, Field, constr, root_validator
from app.utils.custom_exception import *

class Contract(BaseModel):
    name: constr(max_length=64) 
    start: int = Field(..., ge=0)
    duration: int = Field(..., gt=0)
    price: int

        
class ContractList(BaseModel):
    __root__: list[Contract]
    
    @root_validator()
    def check_name_uniqueness(cls, values):
        names = [c.name for c in values["__root__"]]
        if len(set(names)) < len(names):
            raise DuplicateNameError("Contract names must be unique!")
        return values