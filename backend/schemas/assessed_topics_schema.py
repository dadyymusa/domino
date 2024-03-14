from pydantic import BaseModel

class AssessedTopicsBase(BaseModel):
    date : str
    topics : str
    subject : str


class AssessedTopicsIn(AssessedTopicsBase):
    pass

class AssessedTopicsOut(AssessedTopicsBase):
    pass 

class AssessedTopicsDB(AssessedTopicsBase):
    id : int 