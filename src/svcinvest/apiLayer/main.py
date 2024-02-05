from fastapi import FastAPI, Request, APIRouter
from pydantic import BaseModel
from fastapi.openapi.docs import get_swagger_ui_html
from src.svcinvest.apiLayer.ReqReplyModel import (
    StockAdviceRequest,
    Response
)

app = FastAPI()
router = APIRouter()

@router.get("/", tags=["Healthcheck"])
def read_root():
    print('in default')
    return {"Hello": "world"}

@router.post("/stock", tags=["Stock"])
def read_root(request: StockAdviceRequest):
   # print('in test path ' + request.scope.get("root_path"))
    return request

app.include_router(router)