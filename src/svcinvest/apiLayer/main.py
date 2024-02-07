from fastapi import FastAPI, Request, APIRouter
from pydantic import BaseModel
from fastapi.openapi.docs import get_swagger_ui_html
from svcinvest.apiLayer.ReqReplyModel import (
    StockAdviceRequest,
    Response
)
from svcinvest.middleLayer import agents

app = FastAPI(root_path="/api/v1")
router = APIRouter()

@router.get("/", tags=["Healthcheck"])
def read_root():
    print('in default')
    return {"Hello": "world"}

@router.post("/stock", tags=["Stock"])
def read_root(request: StockAdviceRequest):
    
    openai_agent = agents.get_agent()
    openapi_request = {"input" : request.question}
    openai_response = openai_agent.invoke(openapi_request)
    return Response(input=openai_response['input'], 
                    output=openai_response['output'])

app.include_router(router)