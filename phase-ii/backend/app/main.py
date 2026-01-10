from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.v1.endpoints import tasks
from app.api.v1.endpoints.auth import router as auth_router
from app.core.config import settings
from app.exceptions import TaskNotFoundError, ValidationError as AppValidationError
from pydantic import ValidationError as PydanticValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from datetime import datetime


app = FastAPI(
    title="Todo API",
    description="REST API for Todo application backend",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])


@app.exception_handler(TaskNotFoundError)
async def handle_task_not_found(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "message": exc.message,
            "code": "TASK_NOT_FOUND",
            "details": {"task_id": str(exc.task_id)},
            "timestamp": datetime.utcnow().isoformat()
        }
    )


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "code": f"HTTP_{exc.status_code}",
            "details": None,
            "timestamp": datetime.utcnow().isoformat()
        }
    )


@app.exception_handler(PydanticValidationError)
async def validation_exception_handler(request: Request, exc: PydanticValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation error",
            "code": "VALIDATION_ERROR",
            "details": {
                "errors": [
                    {
                        "field": str(err.get('loc', ['unknown'])[-1]),
                        "message": err.get('msg', 'Unknown error'),
                        "type": err.get('type', 'unknown')
                    }
                    for err in exc.errors()
                ]
            },
            "timestamp": datetime.utcnow().isoformat()
        }
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal server error",
            "code": "INTERNAL_ERROR",
            "details": None,
            "timestamp": datetime.utcnow().isoformat()
        }
    )


@app.get("/")
def read_root():
    return {"message": "Todo Backend API - Phase II Part 1"}


@app.on_event("startup")
async def startup_event():
    # Any startup tasks can go here
    pass


@app.on_event("shutdown")
async def shutdown_event():
    # Any cleanup tasks can go here
    pass