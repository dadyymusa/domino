from pydantic import BaseModel

class RevisedTopicsBase(BaseModel):
    date : str
    topics : str
    subject : str


class RevisedTopicsIn(RevisedTopicsBase):
    pass

class RevisedTopicsOut(RevisedTopicsBase):
    pass 

class RevisedTopicsDB(RevisedTopicsBase):
    id : int 