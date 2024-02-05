from pydantic import BaseModel

class StockAdviceRequest(BaseModel):
    question: str 

class Response(BaseModel):
    input: str
    output: str