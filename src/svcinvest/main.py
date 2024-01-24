from fastapi import FastAPI, Request, APIRouter
from typing import Union
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()
router = APIRouter()

@router.get("/", tags=["Healthcheck"])
def read_root():
    print('in default')
    return {"Hello": "world"}

@router.get("/stock", tags=["Stock"])
def read_root(request: Request):
    print('in test path ' + request.scope.get("root_path"))
    return {"Hello": "world"}

app.include_router(router)