from fastapi import ( 
    FastAPI, 
    Request, 
    APIRouter,
    HTTPException )
from svcinvest.apiLayer.ReqReplyModel import (
    StockAdviceRequest,
    Response
)
from svcinvest.middleLayer import agents

app = FastAPI(root_path="/api/v1", title="Stock Info using AI")
router = APIRouter()

@router.get("/", tags=["Healthcheck"], summary="Health Check")
def read_root(request: Request):
    print('in default')
    return {"Hello": "world", "root_path": request.scope.get("root_path")}

@router.post("/stock", response_model=Response,
               tags=["Stock"], summary="Get current stock information")
def read_root(request: StockAdviceRequest):
    if request.question == "string":
        raise HTTPException(status_code=404, detail="Bad Request")
    
    openai_agent = agents.get_agent()
    openapi_request = {"input" : request.question}
    openai_response = openai_agent.invoke(openapi_request)
    return Response(input=openai_response['input'], 
                    output=openai_response['output'])

app.include_router(router)